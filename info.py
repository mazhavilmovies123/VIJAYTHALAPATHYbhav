import re
from os import environ
from dotenv import load_dotenv
from Script import script 

# load_dotenv("./config.env")
load_dotenv("./dynamic.env", override=True)

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '25578852'))
API_HASH = environ.get('API_HASH', '1c8e30eae03f9600dfdee4408db4811a')
BOT_TOKEN = environ.get('BOT_TOKEN', '5828891683:AAELYQDiZT6np5Z42yBHNaOr2BeDjRRwy-U')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS' ,'https://graph.org/file/df17e1fad3d856caf5df8.jpg https://graph.org/file/4db7c2e38f273e3b239dd.jpg https://graph.org/file/e4ead277c0bb7ab445c31.jpg https://graph.org/file/10d81181913c5d4237640.jpg https://graph.org/file/40fef09781fb9ded8cd13.jpg https://graph.org/file/b7b5a32ea575fa7ff50ee.jpg https://graph.org/file/bca1ca2c91828161aa247.jpg https://graph.org/file/bcea1a4ae0176d38a68b7.jpg https://graph.org/file/18a9f945534afa9db5036.jpg https://graph.org/file/89975fb3c157c1ae01e43.jpg https://graph.org/file/c548df4d4a42a8646aa04.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '683891378 6105017520 5845960615').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001833339939 -1002038316280').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_grp = environ.get('AUTH_GROUP')
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID', '-1001693527538')
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://MONGOO:MONGOO@cluster0.rh6p7y3.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "MONGOO:MONGOO")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# FSUB
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
# Set to False inside the bracket if you don't want to use Request Channel else set it to Channel ID

REQ_CHANNEL=environ.get("REQ_CHANNEL")
REQ_CHANNEL = (int(REQ_CHANNEL) if REQ_CHANNEL and id_pattern.search(REQ_CHANNEL) else False) if REQ_CHANNEL is not None else None
JOIN_REQS_DB = environ.get("JOIN_REQS_DB", DATABASE_URI)

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001857768683'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'MLZ_BOTZ_SUPPORT')
MAX_B_TN = environ.get("MAX_B_TN", "8")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "False")), False)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "False")), True)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', 'False')), False)
IMDB = is_enabled((environ.get('IMDB', 'False')), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', 'True')), False)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", f"{script.CAPTION}")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "🏷 𝖳𝗂𝗍𝗅𝖾: <a href={url}>{title}</a> \n🔮 𝖸𝖾𝖺𝗋: {year} \n⭐️ 𝖱𝖺𝗍𝗂𝗇𝗀𝗌: {rating}/ 10 \n🎭 𝖦𝖾𝗇𝖾𝗋𝗌: {genres} \n\n🎊 𝖯𝗈𝗐𝖾𝗋𝖾𝖽 𝖡𝗒 [ᴀᴍ_ᴛᴇᴄʜ](https://t.me/Am_RoBots)")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
