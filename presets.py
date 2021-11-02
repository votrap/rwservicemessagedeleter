# ----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
if os.environ.get("ENV", False):
    from sample_config import Config
    from sample_config import LOGGER
else:
    from config import Config
    from config import LOGGER

class Presets(object):
    START_TEXT = """
𝙃𝙚𝙡𝙡𝙤... {}
𝐼 𝑐𝑎𝑛 𝑐𝑙𝑜𝑛𝑒 𝑚𝑒𝑑𝑖𝑎 𝑓𝑟𝑜𝑚 𝑎𝑛𝑦 𝑐ℎ𝑎𝑡 𝑡𝑜 𝑦𝑜𝑢𝑟 𝑝𝑒𝑟𝑠𝑜𝑛𝑎𝑙 𝑐ℎ𝑎𝑡 ! 𝐶𝑙𝑖𝑐𝑘 𝑠𝑒𝑡𝑡𝑖𝑛𝑔𝑠 𝑡𝑜 𝑐𝑜𝑛𝑓𝑖𝑔𝑢𝑟𝑒 𝑚𝑒.
You can set clone delay with /{} command. Click it for more information.
𝐼𝑓 𝑦𝑜𝑢 𝑙𝑖𝑘𝑒 𝑚𝑒, 𝑝𝑙𝑒𝑎𝑠𝑒 𝑔𝑖𝑣𝑒 𝑎 𝑠𝑡𝑎𝑟 𝑖𝑛 𝑚𝑎 𝐺𝑖𝑡𝐻𝑢𝑏 𝑟𝑒𝑝𝑜. 𝑇ℎ𝑎𝑛𝑘𝑠
    """
    WELCOME_TEXT = "⭑⭑★✪ HELP for more info: ✪★⭑⭑"
    MESSAGE_COUNT = """
𝙇𝙞𝙫𝙚: <code>{}\n{}\n{}</code>\n
𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐈𝐝 - <b>{}</b>
𝐍𝐨𝐰@         - <b>{}</b>
𝐄𝐧𝐝𝐢𝐧𝐠 𝐈𝐝   - <b>{}</b>

𝐂𝐥𝐨𝐧𝐞 𝐃𝐞𝐥𝐚𝐲                  - {}
𝐃𝐞𝐟𝐚𝐮𝐥𝐭 𝐂𝐚𝐩𝐭𝐢𝐨𝐧           - {}
𝐅𝐢𝐥𝐞 𝐧𝐚𝐦𝐞 𝐚𝐬 𝐂𝐚𝐩𝐭𝐢𝐨𝐧  - {}

𝕋𝕠𝕥𝕒𝕝 ℂ𝕠𝕡𝕚𝕖𝕕              - <b>{}</b>
𝕋𝕠𝕥𝕒𝕝 ℂ𝕠𝕞𝕡𝕝𝕖𝕥𝕖𝕕      - <b>{} %</b> 󠀥

📚 𝐃𝐨𝐜𝐮𝐦𝐞𝐧𝐭𝐬             - <b>{}</b>
🎞 𝐕𝐢𝐝𝐞𝐨𝐬                     - <b>{}</b>
🔊 𝐀𝐮𝐝𝐢𝐨𝐬                     - <b>{}</b>
📸 𝐏𝐡𝐨𝐭𝐨𝐬                     - <b>{}</b>
🗣 𝐕𝐨𝐢𝐜𝐞                        - <b>{}</b>
🧩 𝐃𝐮𝐩𝐥𝐢𝐜𝐚𝐭𝐞 𝐅𝐢𝐥𝐞𝐬       - <b>{}</b>

⏳ 𝐓𝐢𝐦𝐞 𝐓𝐚𝐤𝐞𝐧            - <b>{}</b>
🆙 𝐁𝐨𝐭 𝐔𝐩𝐭𝐢𝐦𝐞             - <b>{}</b>
📲 𝐂𝐥𝐨𝐧𝐞 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 𝐀𝐭    - <b>{}</b>
📌 𝐋𝐚𝐬𝐭 𝐔𝐩𝐝𝐚𝐭𝐞𝐝 𝐎𝐧   - <b>{}</b>

🔰 <a href='t.me/RMProjects'><b>@RMProjects</b></a>     🏅 <a href='https://github.com/m4mallu/clonebot-ui'><b>@Github</b></a>
    """
    INFO_CHAT_TYPES = """
𝙔𝙤𝙪 𝙘𝙖𝙣 𝙚𝙣𝙩𝙚𝙧 𝙩𝙝𝙚 𝙛𝙤𝙡𝙡𝙤𝙬𝙞𝙣𝙜 𝙩𝙮𝙥𝙚𝙨:

𝐈𝐝           : 𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗 (-𝟏𝟎𝟎 𝐧𝐨𝐭 𝐫𝐞𝐪.)
𝐈𝐧𝐯𝐢𝐭𝐞 𝐥𝐢𝐧𝐤𝐬  : 𝐡𝐭𝐭𝐩𝐬://𝐭.𝐦𝐞/𝐣𝐨𝐢𝐧𝐜𝐡𝐚𝐭/
𝐏𝐮𝐛𝐥𝐢𝐜 𝐥𝐢𝐧𝐤𝐬 : 𝐡𝐭𝐭𝐩𝐬://𝐭.𝐦𝐞/𝐩𝐲𝐭𝐡𝐨𝐧
𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞𝐬  : @𝐩𝐲𝐭𝐡𝐨𝐧
    """
    SELECTED_TYPE = """
𝙔𝙤𝙪 𝙝𝙖𝙫𝙚 𝙨𝙚𝙡𝙚𝙘𝙩𝙚𝙙:
------------------------------
𝐃𝐨𝐜𝐮𝐦𝐞𝐧𝐭 : {}
𝐀𝐮𝐝𝐢𝐨         : {}
𝐕𝐢𝐝𝐞𝐨         : {}
𝐏𝐡𝐨𝐭𝐨         : {}
𝐕𝐨𝐢𝐜𝐞          : {}
    """
    VIEW_CONF = """
𝐒𝐨𝐮𝐫𝐜𝐞 𝐈𝐝 : {}
𝐓𝐚𝐫𝐠𝐞𝐭 𝐈𝐝 : {}
𝐅𝐫𝐨𝐦 𝐦𝐬𝐠 𝐈𝐝 : {} | 𝐓𝐨 𝐦𝐬𝐠 𝐈𝐝 : {}
𝐃𝐞𝐥𝐚𝐲𝐞𝐝 : {} | 𝐂𝐚𝐩𝐭𝐢𝐨𝐧 : {} | 𝐅𝐍 𝐂𝐚𝐩𝐭𝐢𝐨𝐧: {}
𝐓𝐲𝐩𝐞𝐬: 📚:{} | 🎞:{} | 🔊:{} | 📸:{} | 🗣:{}
    """
    COPIED_MESSAGES = "<b><a href='https://github.com/m4mallu/clonebot'>Medias Copied</a></b>"
    IN_CORRECT_PERMISSIONS_MESSAGE_DEST_POSTING = "A̶c̶c̶e̶s̶s̶ ̶D̶e̶n̶i̶e̶d̶\n\n𝘜𝘴𝘦𝘳 𝘪𝘴 𝘯𝘰𝘵 𝘢𝘯 𝘢𝘥𝘮𝘪𝘯 𝘰𝘳 𝘥𝘰𝘦𝘴𝘯'𝘵 𝘩𝘢𝘷𝘦\n" \
                                                  "𝘱𝘰𝘴𝘵𝘪𝘯𝘨 𝘱𝘳𝘪𝘷𝘪𝘭𝘢𝘨𝘦𝘴 𝘪𝘯 𝘵𝘩𝘦 𝘨𝘪𝘷𝘦𝘯 𝘤𝘩𝘢𝘵"
    USER_ABSENT_MSG = "𝙎𝙚𝙨𝙨𝙞𝙤𝙣 𝙪𝙨𝙚𝙧 𝙞𝙨 𝙣𝙤𝙩 𝙞𝙣 𝙩𝙝𝙚 𝙩𝙖𝙧𝙜𝙚𝙩 𝙘𝙝𝙖𝙩 𝙜𝙞𝙫𝙚𝙣"
    CANCEL_CLONE = "𝙎𝙩𝙤𝙥𝙥𝙞𝙣𝙜 𝙩𝙝𝙚 𝙥𝙧𝙤𝙘𝙚𝙨𝙨... 𝙋𝙡𝙯 𝙬𝙖𝙞𝙩 🕚"
    CANCELLED_MSG = "⚠      𝙐𝙨𝙚𝙧 𝙘𝙖𝙣𝙘𝙚𝙡𝙡𝙚𝙙 𝙘𝙡𝙤𝙣𝙞𝙣𝙜      ⚠"
    INITIAL_MESSAGE_TEXT = "🔎  𝙄𝙣𝙞𝙩𝙞𝙖𝙡𝙞𝙯𝙞𝙣𝙜 𝙘𝙡𝙤𝙣𝙚  🔎"
    WAIT_MSG = "♻️ 𝙋𝙧𝙤𝙘𝙚𝙨𝙨𝙞𝙣𝙜... 𝙥𝙡𝙯 𝙬𝙖𝙞𝙩 "
    SOURCE_CONFIRM = """
𝐂𝐡𝐚𝐭 𝐍𝐚𝐦𝐞: {}
𝐂𝐡𝐚𝐭 𝐈𝐝: <code> {}</code>
𝐂𝐡𝐚𝐭 𝐓𝐲𝐩𝐞: {}
𝐂𝐡𝐚𝐭 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞: {}
𝐋𝐨𝐜𝐚𝐭𝐢𝐨𝐧: {}
𝐌𝐞𝐦𝐛𝐞𝐫𝐬: {}
\xad                                                              \xad
S̶o̶u̶r̶c̶e̶ C̶h̶a̶t̶ 𝐒𝐚𝐯𝐞𝐝  ✅
                     """
    DEST_CNF = """
𝐂𝐡𝐚𝐭 𝐍𝐚𝐦𝐞: {}
𝐂𝐡𝐚𝐭 𝐈𝐝: <code> {}</code>
𝐂𝐡𝐚𝐭 𝐓𝐲𝐩𝐞: {}
𝐂𝐡𝐚𝐭 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞: {}
𝐋𝐨𝐜𝐚𝐭𝐢𝐨𝐧: {}
𝐌𝐞𝐦𝐛𝐞𝐫𝐬: {}
\xad                                                              \xad
T̶a̶r̶g̶e̶t̶ C̶h̶a̶t̶ 𝐒𝐚𝐯𝐞𝐝  ✅
               """
    SESSION_START_INFO = """
𝐔𝐬𝐞𝐫 𝐬𝐞𝐬𝐬𝐢𝐨𝐧 𝐬𝐭𝐚𝐫𝐭𝐞𝐝:

𝐃𝐚𝐭𝐞     :  {}
𝐓𝐢𝐦𝐞    :  {}

𝘈 𝘶𝘴𝘦𝘳 𝘴𝘦𝘴𝘴𝘪𝘰𝘯 𝘪𝘴 𝘴𝘵𝘢𝘳𝘵𝘦𝘥 𝘪𝘯 𝘺𝘰𝘶𝘳
𝘢𝘤𝘤𝘰𝘶𝘯𝘵, 𝘪𝘧 𝘺𝘰𝘶 𝘬𝘯𝘰𝘸 𝘵𝘩𝘪𝘴, 𝘬𝘦𝘦𝘱
𝘵𝘩𝘪𝘴 𝘣𝘰𝘵 𝘶𝘯𝘣𝘭𝘰𝘤𝘬𝘦𝘥, 𝘺𝘰𝘶 𝘤𝘢𝘯 𝘪𝘨𝘯𝘰𝘳𝘦
𝘵𝘩𝘪𝘴 𝘮𝘦𝘴𝘴𝘢𝘨𝘦, 𝘐𝘧 𝘺𝘰𝘶 𝘧𝘦𝘦𝘭𝘴 𝘭𝘪𝘬𝘦
𝘧𝘶𝘤𝘬𝘦𝘥-𝘶𝘱, ᴛᴇʀᴍɪɴᴀᴛᴇ 𝘵𝘩𝘪𝘴 𝘴𝘦𝘴𝘴𝘪𝘰𝘯
𝘢𝘯𝘥 𝘣𝘭𝘰𝘤𝘬 𝘵𝘩𝘪𝘴 𝘣𝘰𝘵 𝘵𝘰 𝘢𝘷𝘰𝘪𝘥 𝘶𝘴𝘢𝘨𝘦
𝘰𝘧 𝘺𝘰𝘶𝘳 𝘴𝘦𝘴𝘴𝘪𝘰𝘯 𝘢𝘨𝘢𝘪𝘯. Y̶o̶u̶ c̶a̶n̶
s̶e̶e̶ t̶h̶i̶s̶ m̶e̶s̶s̶a̶g̶e̶ a̶g̶a̶i̶n̶ w̶h̶e̶n̶
H̶e̶r̶o̶k̶u̶ f̶r̶e̶e̶ d̶y̶n̶o̶s̶ r̶e̶s̶t̶a̶r̶t̶s̶ .
    """
    NOT_CONFIGURED = "𝙎𝙤𝙪𝙧𝙘𝙚 & 𝙏𝙖𝙧𝙜𝙚𝙩 𝙘𝙝𝙖𝙩𝙨 𝙣𝙤𝙩 𝙘𝙤𝙣𝙛𝙞𝙜𝙪𝙧𝙚𝙙 ⚠"
    NOT_AUTH_TEXT = "𝙔𝙤𝙪 𝙖𝙧𝙚 𝙣𝙤𝙩 𝙖𝙪𝙩𝙝𝙤𝙧𝙞𝙯𝙚𝙙  ⚠ "
    BOT_BLOCKED_MSG = "Bot is blocked by the  session user !"
    NOT_CONFIGURED_CLONE = "𝙉𝙤 𝙘𝙝𝙖𝙩 𝙘𝙤𝙣𝙛𝙞𝙜𝙪𝙧𝙖𝙩𝙞𝙤𝙣 𝙛𝙤𝙪𝙣𝙙 ⚠\n\n𝘾𝙤𝙣𝙛𝙞𝙜𝙪𝙧𝙚 𝙩𝙝𝙚 𝙎𝙤𝙪𝙧𝙘𝙚 & 𝘿𝙚𝙨𝙩𝙞𝙣𝙖𝙩𝙞𝙤𝙣 𝙘𝙝𝙖𝙩𝙨 𝙗𝙚𝙛𝙤𝙧𝙚 𝙮𝙤𝙪 𝙘𝙡𝙤𝙣𝙚 🤷"
    FINISHED_TEXT = "𝘾𝙡𝙤𝙣𝙚  𝙘𝙤𝙢𝙥𝙡𝙚𝙩𝙚𝙙 𝙨𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮  ✅"
    TERMINATED_MSG = "🚫 𝘽𝙤𝙩 𝙏𝙚𝙧𝙢𝙞𝙣𝙖𝙩𝙚𝙙 🚫\n𝘍𝘦𝘦𝘭𝘴 𝘴𝘰𝘮𝘦𝘵𝘩𝘪𝘯𝘨 𝘧𝘪𝘴𝘩𝘺? 𝘉𝘭𝘰𝘤𝘬 𝘵𝘩𝘪𝘴 𝘣𝘰𝘵 𝘵𝘰 𝘢𝘷𝘰𝘪𝘥 𝘵𝘩𝘦 𝘶𝘴𝘢𝘨𝘦 𝘰𝘧 𝘺𝘰𝘶𝘳 𝘴𝘦𝘴𝘴𝘪𝘰𝘯 𝘢𝘨𝘢𝘪𝘯 !"
    COPY_ERROR = "𝙎𝙤𝙢𝙚𝙩𝙝𝙞𝙣𝙜 𝙬𝙚𝙣𝙩 𝙬𝙧𝙤𝙣𝙜 !\n\n𝘊𝘰𝘱𝘺𝘪𝘯𝘨 𝘢𝘣𝘰𝘳𝘵𝘦𝘥 𝘣𝘺 𝘵𝘩𝘦 𝘴𝘺𝘴𝘵𝘦𝘮\n𝘊𝘩𝘦𝘤𝘬 𝘢𝘭𝘭 𝘵𝘩𝘦 𝘶𝘴𝘦𝘳 𝘱𝘦𝘳𝘮𝘪𝘴𝘴𝘪𝘰𝘯𝘴."
    INVALID_CHAT_ID = "<u>𝙄𝙣𝙫𝙖𝙡𝙞𝙙 𝙘𝙝𝙖𝙩 𝙥𝙖𝙧𝙖𝙢𝙚𝙩𝙚𝙧 𝙛𝙤𝙪𝙣𝙙</u>\n\n𝐂𝐚𝐮𝐬𝐞𝐬:\n1. 𝘚𝘦𝘴𝘴𝘪𝘰𝘯 𝘶𝘴𝘦𝘳 𝘯𝘰𝘵 𝘪𝘯 𝘗𝘳𝘪𝘷𝘢𝘵𝘦 𝘤𝘩𝘢𝘵\n" \
                      "2. 𝘍𝘰𝘳 𝘱𝘶𝘣𝘭𝘪𝘤 𝘤𝘩𝘢𝘵𝘴, 𝘶𝘴𝘦 '@𝘶𝘴𝘦𝘳𝘯𝘢𝘮𝘦'\n𝘰𝘳 𝘭𝘪𝘯𝘬 𝘪𝘯𝘴𝘵𝘦𝘢𝘥 𝘰𝘧 '𝘪𝘥'"
    ASK_SOURCE = "𝙂𝙞𝙫𝙚 𝙩𝙝𝙚 𝙨𝙤𝙪𝙧𝙘𝙚 𝙘𝙝𝙖𝙩 𝙞𝙣𝙛𝙤:\n𝑌𝑜𝑢 ℎ𝑎𝑣𝑒 30𝑆𝑒𝑐 𝑡𝑜 𝑑𝑜 𝑡ℎ𝑖𝑠.."
    ASK_DESTINATION = "𝙂𝙞𝙫𝙚 𝙩𝙝𝙚 𝘿𝙚𝙨𝙩𝙞𝙣𝙖𝙩𝙞𝙤𝙣 𝙘𝙝𝙖𝙩 𝙞𝙣𝙛𝙤:\n𝑌𝑜𝑢 ℎ𝑎𝑣𝑒 30𝑆𝑒𝑐 𝑡𝑜 𝑑𝑜 𝑡ℎ𝑖𝑠.."
    ASK_START_MSG_ID = "𝙂𝙞𝙫𝙚 𝙩𝙝𝙚 𝙨𝙩𝙖𝙧𝙩𝙞𝙣𝙜 𝙢𝙚𝙨𝙨𝙖𝙜𝙚 𝙄𝙙:\n𝑌𝑜𝑢 ℎ𝑎𝑣𝑒 30𝑆𝑒𝑐 𝑡𝑜 𝑑𝑜 𝑡ℎ𝑖𝑠.."
    ASK_END_MSG_ID = "𝙂𝙞𝙫𝙚 𝙩𝙝𝙚 𝙚𝙣𝙙 𝙢𝙚𝙨𝙨𝙖𝙜𝙚 𝙄𝙙\n𝑌𝑜𝑢 ℎ𝑎𝑣𝑒 30𝑆𝑒𝑐 𝑡𝑜 𝑑𝑜 𝑡ℎ𝑖𝑠.."
    CHAT_DUPLICATED_MSG = "𝙎𝙤𝙪𝙧𝙘𝙚 & 𝘿𝙚𝙨𝙩𝙞𝙣𝙖𝙩𝙞𝙤𝙣 𝙘𝙝𝙖𝙩 𝙄𝙙𝙨 𝙘𝙖𝙣'𝙩 𝙗𝙚 𝙨𝙖𝙢𝙚 "
    FROM_MSG_ID_CNF = "𝐒𝐭𝐚𝐫𝐭 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐈𝐝:👉 <code>{}</code> 👈 𝐒𝐚𝐯𝐞𝐝  ✅"
    END_MSG_ID_CNF = "𝐄𝐧𝐝 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐈𝐝:👉 <code>{}</code> 👈 𝐒𝐚𝐯𝐞𝐝  ✅"
    INVALID_MSG_ID = "𝙈𝙚𝙨𝙨𝙖𝙜𝙚 𝙞𝙙 𝙨𝙝𝙤𝙪𝙡𝙙 𝙗𝙚 𝙖𝙣 𝙄𝙣𝙩𝙚𝙜𝙚𝙧 ❗️"
    INVALID_REPLY_MSG = "𝙄𝙣𝙫𝙖𝙡𝙞𝙙 𝙧𝙚𝙥𝙡𝙖𝙮 𝙢𝙚𝙨𝙨𝙖𝙜𝙚 ❗️"
    CNF_SOURCE_FIRST = "𝘾𝙤𝙣𝙛𝙞𝙜𝙪𝙧𝙚 𝙩𝙝𝙚 𝙨𝙤𝙪𝙧𝙘𝙚 𝙘𝙝𝙖𝙩 𝙛𝙞𝙧𝙨𝙩  ❗️"
    DELAY_OFF = "𝘿𝙚𝙡𝙖𝙮𝙚𝙙 𝙘𝙡𝙤𝙣𝙚 : 𝘿𝙚𝙖𝙘𝙩𝙞𝙫𝙖𝙩𝙚𝙙 🚫"
    DELAY_ON = "𝘿𝙚𝙡𝙖𝙮𝙚𝙙 𝙘𝙡𝙤𝙣𝙚 : 𝘼𝙘𝙩𝙞𝙫𝙖𝙩𝙚𝙙 [𝟏𝟎 𝐬𝐞𝐜] ✅"
    ADD_DOC = "𝙁𝙞𝙡𝙚 𝙩𝙮𝙥𝙚 👉 𝘿𝙤𝙘𝙪𝙢𝙚𝙣𝙩 👈 𝙖𝙙𝙙𝙚𝙙"
    RM_DOC = "𝙁𝙞𝙡𝙚 𝙩𝙮𝙥𝙚 👉 𝘿𝙤𝙘𝙪𝙢𝙚𝙣𝙩 👈 𝙞𝙜𝙣𝙤𝙧𝙚𝙙 "
    ADD_VID = "𝙁𝙞𝙡𝙚 𝙩𝙮𝙥𝙚 👉 𝙑𝙞𝙙𝙚𝙤 👈 𝙖𝙙𝙙𝙚𝙙"
    RM_VID = "𝙁𝙞𝙡𝙚 𝙩𝙮𝙥𝙚 👉 𝙑𝙞𝙙𝙚𝙤 👈 𝙞𝙜𝙣𝙤𝙧𝙚𝙙 "
    ADD_AUD = "𝙁𝙞𝙡𝙚 𝙩𝙮𝙥𝙚 👉 𝘼𝙪𝙙𝙞𝙤 👈 𝙖𝙙𝙙𝙚𝙙"
    RM_AUD = "𝙁𝙞𝙡𝙚 𝙩𝙮𝙥𝙚 👉 𝘼𝙪𝙙𝙞𝙤 👈 𝙞𝙜𝙣𝙤𝙧𝙚𝙙 "
    ADD_PIC = "𝙁𝙞𝙡𝙚 𝙩𝙮𝙥𝙚 👉 𝙋𝙝𝙤𝙩𝙤 👈 𝙖𝙙𝙙𝙚𝙙"
    RM_PIC = "𝙁𝙞𝙡𝙚 𝙩𝙮𝙥𝙚 👉 𝙋𝙝𝙤𝙩𝙤 👈 𝙞𝙜𝙣𝙤𝙧𝙚𝙙 "
    ADD_VOI = "𝙁𝙞𝙡𝙚 𝙩𝙮𝙥𝙚 👉 𝙑𝙤𝙞𝙘𝙚 👈 𝙖𝙙𝙙𝙚𝙙"
    RM_VOI = "𝙁𝙞𝙡𝙚 𝙩𝙮𝙥𝙚 👉 𝙑𝙤𝙞𝙘𝙚 👈 𝙞𝙜𝙣𝙤𝙧𝙚𝙙 "
    BLANK = "➖➖➖➖➖➖➖➖➖➖➖➖➖"
    BLOCK = "ᴘʀᴏɢʀᴇꜱꜱ ꜰᴀɪʟᴇᴅ ᴛᴏ ᴅɪꜱᴘʟᴀʏ :👉 ʜᴇʟᴘ"
    CAPTION_ON = "𝘾𝙖𝙥𝙩𝙞𝙤𝙣 𝙤𝙣 𝙛𝙞𝙡𝙚𝙨 : 𝘼𝙘𝙩𝙞𝙫𝙖𝙩𝙚𝙙 ✅"
    CAPTION_OFF = "𝘾𝙖𝙥𝙩𝙞𝙤𝙣 𝙤𝙣 𝙛𝙞𝙡𝙚𝙨 : 𝘿𝙚𝙖𝙘𝙩𝙞𝙫𝙖𝙩𝙚𝙙 🚫"
    FN_AS_CAPT_ON = "𝙁𝙞𝙡𝙚 𝙣𝙖𝙢𝙚 𝙖𝙨 𝙘𝙖𝙥𝙩𝙞𝙤𝙣 : 𝘼𝙘𝙩𝙞𝙫𝙖𝙩𝙚𝙙 ✅"
    FN_AS_CAPT_OFF = "𝙁𝙞𝙡𝙚 𝙣𝙖𝙢𝙚 𝙖𝙨 𝙘𝙖𝙥𝙩𝙞𝙤𝙣 : 𝘿𝙚𝙖𝙘𝙩𝙞𝙫𝙖𝙩𝙚𝙙 🚫"
    NOT_REQUIRED = "𝙏𝙝𝙞𝙨 𝙛𝙞𝙚𝙡𝙙 𝙞𝙨 𝙣𝙤𝙩 𝙈𝙖𝙙𝙖𝙩𝙤𝙧𝙮  ⚠"
    RST_MSG = "𝙍𝙚𝙨𝙚𝙩 𝙩𝙤 𝘽𝙤𝙩 𝙙𝙚𝙛𝙖𝙪𝙡𝙩𝙨 .. 𝘾𝙤𝙣𝙛𝙞𝙧𝙢𝙚𝙙 ✅"
    TEST_MSG = f"Test Message. Delay set: <code>{str(Config.DELAY_SECS)}</code>"
    OVER_FLOW = "𝙈𝙖𝙭𝙞𝙢𝙪𝙢 𝙡𝙞𝙢𝙞𝙩 𝙞𝙨 𝙚𝙭𝙘𝙚𝙚𝙙𝙚𝙙 !\n𝘾𝙝𝙚𝙘𝙠 𝙩𝙝𝙚 𝙖𝙡𝙡𝙤𝙬𝙚𝙙 𝙡𝙞𝙢𝙞𝙩, 𝙏𝙧𝙮 𝙖𝙜𝙖𝙞𝙣 !"
    SELECT_TYPE = "👉 𝙎𝙚𝙡𝙚𝙘𝙩𝙞𝙤𝙣 𝙬𝙞𝙡𝙡 𝙗𝙚 𝙩𝙤𝙜𝙜𝙡𝙚𝙙 𝙤𝙣 𝙩𝙖𝙥\n𝘈𝘭𝘭 𝘢𝘳𝘦 𝘴𝘦𝘭𝘦𝘤𝘵𝘦𝘥 𝘣𝘺 𝘥𝘦𝘧𝘢𝘶𝘭𝘵 !"
    INDEXING_MSG = "𝙋𝙡𝙚𝙖𝙨𝙚 𝙬𝙖𝙞𝙩..\n<i>Finding duplicate messages in the\ntarget chat. This will " \
                   "take some\ntime to figure out.</i>\n\n<b><u>Message id</u>:-\n🔷Now@: {}\n🔷End@ : {}\n\n" \
                   "<u>Duplicates</u>:-\n⚠Total: {}</b>"
    PURGE_PROMPT = "👉 <b>{}</b>  👈 <i>Duplicate files found in your target chat. Do you wish to purge it now ?</i>"
    PROCESSING_PURGE = "<b>🔷Now@: {}        🔷End@: {}</b>\n\n<i>𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠.. Please Wait</i>"
    TARGET_CFG_LOAD_MSG = "<b><u>Imported</u>  ✅</b>\n\n<code>An index of the given target chat found in my database. " \
                          "It has been loaded to ma memory.</code>\n\n<b><i>Proceeding to clone..</i></b>"
