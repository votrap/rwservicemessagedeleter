import asyncio

from bot import Bot
from library.sql import *
from presets import Presets
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from library.chat_support import find_msg_id, find_dc
from library.buttons import reply_markup_start, reply_markup_home
from pyrogram.types import Message

import os
if os.environ.get("ENV", False):
    from sample_config import Config
    from sample_config import LOGGER
else:
    from config import Config
    from config import LOGGER

# ----------------------------- Start Message command function --------------------------- #
@Bot.on_message(filters.private & filters.command(['start', 'help', 'h']))
async def start(client: Bot, message: Message):
    await message.reply_text(
        Presets.START_TEXT.format(message.from_user.first_name, Config.CHANGE_DELAY_COMMAND),
        reply_markup=reply_markup_start
    )

# --------------------------------- Delay changing function ------------------------------ #
@Bot.on_message(filters.private & filters.command([Config.CHANGE_DELAY_COMMAND]))
async def chdelay(client: Bot, message: Message):
    setdelay = None
    if " " in message.text:
        setdelay = message.text.split(" ")
        try:
            Config.DELAY_SECS = int(setdelay[1])
            send = await message.reply_text(
                quote=True,text=f"Delay set to: <code>{str(Config.DELAY_SECS)}</code> succesfully.")
        except:
            send = await message.reply_text(
                quote=True,text=f"Delay can not be set. Example: <code>/{Config.CHANGE_DELAY_COMMAND} 4</code>")
    else:
        send = await message.reply_text(quote=True,text=f"Delay is <code>{str(Config.DELAY_SECS)}</code> at now.\n" + \
        f"If you want to change it 7 secs, type <code>/{Config.CHANGE_DELAY_COMMAND} 7</code>\n" +\
        f"7 is an example :D You can change delay to what you want.\n\n" + \
        f"If you want to see delay at now, type only <code>/{Config.CHANGE_DELAY_COMMAND}</code>")
    await asyncio.sleep(10)
    await send.delete()
    await message.delete()


# --------------------------------------- Main Window ------------------------------------ #
async def start_options(client: Bot, message: Message):
    await message.reply_text(
        Presets.WELCOME_TEXT,
        parse_mode='html',
        disable_web_page_preview=True,
        reply_markup=reply_markup_home
    )


# ------------------------------------ All-n-One Input fn --------------------------------- #
@Client.on_message(filters.private & filters.text & filters.reply)
async def force_reply_msg(client: Bot, message: Message):
    chat_info = message.text
    id = int(message.from_user.id)
    chat_status = []
    member_status = []
    user_bot_me = await client.USER.get_me()
    query = await query_msg(id)
    a = int(query.s_chat_msg_id)
    b = int(query.d_chat_msg_id)
    c = int(query.from_msg_id)
    d = int(query.to_msg_id)
    e = int(query.s_chat)
    f = int(query.d_chat)
    g = int(query.last_msg_id)
    if "https://t.me/joinchat" in message.text:
        chat_info = message.text
    elif "https://t.me/" in message.text:
        chat_info = str(message.text).split('/')[-1]
    elif str(message.text).startswith('-100') and message.text[1:].isdigit():
        chat_info = int(message.text)
    elif ("-100" not in str(message.text)) and str(message.text).isdigit():
        chat_info = int('-100' + str(message.text))
    else:
        pass
    bot_msg = await message.reply_text(Presets.WAIT_MSG)
    if message.reply_to_message.message_id == a:
        try:
            chat_status = await client.USER.get_chat(chat_info)
        except FloodWait as e:
            await asyncio.sleep(e.x)
        except Exception:
            await client.delete_messages(message.chat.id, a)
            await message.delete()
            await bot_msg.edit(Presets.INVALID_CHAT_ID)
            await asyncio.sleep(10)
            await bot_msg.edit_text(Presets.WELCOME_TEXT, reply_markup=reply_markup_home)
            return
        chat_id = int(chat_status.id)
        user_name = chat_status.username
        dc_id = await find_dc(chat_status)
        await asyncio.sleep(1)
        try:
            if chat_id == f:
                await client.delete_messages(message.chat.id, a)
                await message.delete()
                await bot_msg.edit(Presets.CHAT_DUPLICATED_MSG)
                await asyncio.sleep(5)
                await bot_msg.edit_text(Presets.WELCOME_TEXT, reply_markup=reply_markup_home)
                return
        except Exception:
            pass
        await client.delete_messages(message.chat.id, a)
        await message.delete()
        await source_cnf_db(id, chat_id)
        await del_from_to_ids(id)
        clone_btn_count[id] = id
        await bot_msg.edit(Presets.SOURCE_CONFIRM.format(chat_status.title,
                                                         chat_id,
                                                         chat_status.type,
                                                         '@' + str(user_name) if bool(user_name) else "𝘗𝘳𝘪𝘷𝘢𝘵𝘦 𝘤𝘩𝘢𝘵",
                                                         dc_id if bool(dc_id) else "𝘊𝘩𝘢𝘵 𝘱𝘩𝘰𝘵𝘰 𝘳𝘦𝘲𝘶𝘪𝘳𝘦𝘥",
                                                         chat_status.members_count
                                                         )
                           )
        await start_options(client, message)
        await find_msg_id(client, id, chat_id)
    elif message.reply_to_message.message_id == b:
        await asyncio.sleep(1)
        try:
            chat_status = await client.USER.get_chat(chat_info)
        except FloodWait as e:
            await asyncio.sleep(e.x)
        except Exception:
            await bot_msg.edit(Presets.USER_ABSENT_MSG)
            await client.delete_messages(message.chat.id, b)
            await message.delete()
            await asyncio.sleep(10)
            await bot_msg.edit_text(Presets.WELCOME_TEXT, reply_markup=reply_markup_home)
            return
        chat_id = int(chat_status.id)
        user_name = chat_status.username
        dc_id = await find_dc(chat_status)
        try:
            if chat_id == e:
                await client.delete_messages(message.chat.id, b)
                await message.delete()
                await bot_msg.edit(Presets.CHAT_DUPLICATED_MSG)
                await asyncio.sleep(5)
                await bot_msg.edit_text(Presets.WELCOME_TEXT, reply_markup=reply_markup_home)
                return
        except Exception:
            pass
        member = await client.USER.get_chat_member(chat_id, user_bot_me.id)
        if str(chat_status.type) in ('supergroup' or 'group'):
            if member.status != 'administrator':
                await client.delete_messages(message.chat.id, b)
                await message.delete()
                await bot_msg.edit(Presets.IN_CORRECT_PERMISSIONS_MESSAGE_DEST_POSTING)
                await asyncio.sleep(10)
                await bot_msg.edit_text(Presets.WELCOME_TEXT, reply_markup=reply_markup_home)
                return
            await client.delete_messages(message.chat.id, b)
            await message.delete()
            await target_cnf_db(id, chat_id)
            await bot_msg.edit(Presets.DEST_CNF.format(chat_status.title,
                                                       chat_id,
                                                       chat_status.type,
                                                       '@' + str(user_name) if bool(user_name) else "𝘗𝘳𝘪𝘷𝘢𝘵𝘦 𝘤𝘩𝘢𝘵",
                                                       dc_id if bool(dc_id) else "𝘊𝘩𝘢𝘵 𝘱𝘩𝘰𝘵𝘰 𝘳𝘦𝘲𝘶𝘪𝘳𝘦𝘥",
                                                       chat_status.members_count
                                                       )
                               )
            await asyncio.sleep(2)
            await start_options(client, message)
        else:
            if member.can_post_messages:
                await client.delete_messages(message.chat.id, b)
                await message.delete()
                await target_cnf_db(id, chat_id)
                await bot_msg.edit(Presets.DEST_CNF.format(chat_status.title,
                                                           chat_id,
                                                           chat_status.type,
                                                           '@' + str(user_name) if bool(user_name) else "𝘗𝘳𝘪𝘷𝘢𝘵𝘦 𝘤𝘩𝘢𝘵",
                                                           dc_id if bool(dc_id) else "𝘊𝘩𝘢𝘵 𝘱𝘩𝘰𝘵𝘰 𝘳𝘦𝘲𝘶𝘪𝘳𝘦𝘥",
                                                           chat_status.members_count
                                                           )
                                   )
                await asyncio.sleep(2)
                await start_options(client, message)
            else:
                await client.delete_messages(message.chat.id, b)
                await message.delete()
                await bot_msg.edit(Presets.IN_CORRECT_PERMISSIONS_MESSAGE_DEST_POSTING)
                await asyncio.sleep(10)
                await bot_msg.edit_text(Presets.WELCOME_TEXT, reply_markup=reply_markup_home)
    elif message.reply_to_message.message_id == c:
        msg = int()
        if str(message.text).isdigit():
            await asyncio.sleep(1)
            try:
                msg = int(query.last_msg_id)
                if bool(msg) and (int(message.text) > msg):
                    await client.delete_messages(message.chat.id, c)
                    await message.delete()
                    await bot_msg.edit(Presets.OVER_FLOW)
                    await asyncio.sleep(5)
                    await bot_msg.edit_text(Presets.WELCOME_TEXT, reply_markup=reply_markup_home)
                    return
            except Exception:
                pass
            await from_msg_id_cnf_db(id, message.text)
            await client.delete_messages(message.chat.id, c)
            await message.delete()
            await bot_msg.edit(Presets.FROM_MSG_ID_CNF.format(message.text))
            await asyncio.sleep(3)
            await bot_msg.edit_text(Presets.WELCOME_TEXT, reply_markup=reply_markup_home)
        else:
            await client.delete_messages(message.chat.id, c)
            await message.delete()
            await bot_msg.edit_text(Presets.INVALID_MSG_ID)
            await asyncio.sleep(5)
            await bot_msg.edit_text(Presets.WELCOME_TEXT, reply_markup=reply_markup_home)
    elif message.reply_to_message.message_id == d:
        if str(message.text).isdigit():
            if (g != 0) and int(message.text) > g:
                await client.delete_messages(message.chat.id, d)
                await message.delete()
                await bot_msg.edit(Presets.OVER_FLOW)
                await asyncio.sleep(5)
                await bot_msg.edit_text(Presets.WELCOME_TEXT, reply_markup=reply_markup_home)
                return
            await asyncio.sleep(1)
            await to_msg_id_cnf_db(id, message.text)
            await client.delete_messages(message.chat.id, d)
            await message.delete()
            await bot_msg.edit(Presets.END_MSG_ID_CNF.format(message.text))
            await asyncio.sleep(3)
            await bot_msg.edit_text(Presets.WELCOME_TEXT, reply_markup=reply_markup_home)
        else:
            await client.delete_messages(message.chat.id, d)
            await message.delete()
            await bot_msg.edit_text(Presets.INVALID_MSG_ID)
            await asyncio.sleep(5)
            await bot_msg.edit_text(Presets.WELCOME_TEXT, reply_markup=reply_markup_home)
    else:
        await client.delete_messages(message.chat.id, message.reply_to_message.message_id)
        await message.delete()
        await bot_msg.edit_text(Presets.INVALID_REPLY_MSG)
        await asyncio.sleep(5)
        await bot_msg.edit_text(Presets.WELCOME_TEXT, reply_markup=reply_markup_home)
