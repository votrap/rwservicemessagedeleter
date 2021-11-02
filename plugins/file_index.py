#----------------------------------- https://github.com/m4mallu/clonebot-ui -----------------------------------------#
import asyncio
from bot import Bot
from library.sql import *
from presets import Presets
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from plugins.clone import clone_medias
from library.buttons import reply_markup_skip_index, reply_markup_purge, reply_markup_skip_purge
from library.chat_support import calc_percentage, calc_progress, import_cfg_data

msg_id_index = []

# ------------- Function to find duplicate medias in the target chat ---------------------------- #
async def index_target_chat(client: Bot, message: Message):
    master_index.clear()
    msg_id_index.clear()
    id = int(message.chat.id)
    query = await query_msg(id)
    target_chat = int(query.d_chat)
    present_msg_id = last_msg_id = int()
    index_skip_key[id] = int(message.message_id)
    #
    target_id = str(target_chat).split("-100")[1]
    cfg_file = os.getcwd() + "/" + "cfg" + "/" + str(id) + "/" + str(target_id) + ".csv"
    if os.path.isfile(cfg_file):
        await import_cfg_data(id, target_chat)
        await message.edit(Presets.TARGET_CFG_LOAD_MSG)
        await asyncio.sleep(10)
        await clone_medias(client, message)
        return
    #
    test_msg = await client.USER.send_message(target_chat, Presets.TEST_MSG)
    last_msg_id = int(test_msg.message_id) - 1
    await test_msg.delete()
    await message.edit_text(Presets.INDEXING_MSG.format(present_msg_id, last_msg_id, len(msg_id_index)))
    await asyncio.sleep(1)
    msg2 = await message.reply_text(Presets.WAIT_MSG, reply_markup=reply_markup_skip_index)
    async for user_message in client.USER.iter_history(chat_id=target_chat, reverse=True):
        messages = await client.USER.get_messages(target_chat, user_message.message_id, replies=0)
        present_msg_id = messages.message_id
        if id not in index_skip_key:
            if msg_id_index:
                await msg2.delete()
                await message.edit_text(
                    Presets.PURGE_PROMPT.format(len(msg_id_index)),
                    reply_markup=reply_markup_purge
                )
            else:
                await msg2.delete()
                await clone_medias(client, message)
            return
        if user_message and (not user_message.empty):
            for file_type in file_types:
                pct = await calc_percentage(int(), last_msg_id, present_msg_id)
                media = getattr(messages, file_type, None)
                if media is not None:
                    uid = str(media.file_unique_id)
                    if uid not in master_index:
                        master_index.append(uid)
                    else:
                        msg_id_index.append(int(messages.message_id))
                    try:
                        await message.edit_text(Presets.INDEXING_MSG.format(present_msg_id,
                                                                            last_msg_id,
                                                                            len(msg_id_index)
                                                                            ))
                    except FloodWait as e:
                        await asyncio.sleep(e.x)
                    except Exception:
                        pass
                    progress = await calc_progress(pct)
                    try:
                        await msg2.edit(progress, reply_markup=reply_markup_skip_index)
                    except FloodWait as e:
                        await asyncio.sleep(e.x)
                    except Exception:
                        pass
                    await asyncio.sleep(60)
    #
    if msg_id_index:
        await msg2.delete()
        await message.edit_text(
            Presets.PURGE_PROMPT.format(len(msg_id_index)), reply_markup=reply_markup_purge)
    else:
        await msg2.delete()
        await clone_medias(client, message)


# ------------- Function to purge duplicate medias in the target chat ---------------------------- #
async def purge_media(client: Bot, message: Message):
    id = int(message.chat.id)
    purge_skip_key[id] = int(message.message_id)
    query = await query_msg(id)
    target_chat = int(query.d_chat)
    await message.edit_text(Presets.PROCESSING_PURGE.format(int(), msg_id_index[-1]))
    await asyncio.sleep(1)
    msg2 = await message.reply_text(Presets.WAIT_MSG, reply_markup=reply_markup_skip_purge)
    for i in msg_id_index:
        if not id in purge_skip_key:
            await msg2.delete()
            await clone_medias(client, message)
            return
        pct = await calc_percentage(int(), msg_id_index[-1], int(i))
        try:
            await client.USER.delete_messages(target_chat, int(i))
        except FloodWait as e:
            await asyncio.sleep(e.x)
        except Exception:
            pass
        try:
            await message.edit(Presets.PROCESSING_PURGE.format(i, msg_id_index[-1]))
        except FloodWait as e:
            await asyncio.sleep(e.x)
        except Exception:
            pass
        progress = await calc_progress(pct)
        try:
            await msg2.edit(progress, reply_markup=reply_markup_skip_purge)
        except FloodWait as e:
            await asyncio.sleep(e.x)
        except Exception:
            pass
        await asyncio.sleep(60)
    #
    await msg2.delete()
    await clone_medias(client, message)
