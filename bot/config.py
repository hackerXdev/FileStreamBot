from os import environ as env

class Telegram:
    API_ID = int(env.get("TELEGRAM_API_ID", 20632966))
    API_HASH = env.get("TELEGRAM_API_HASH", "a2883dd57af2754c591c0374bae10402")
    OWNER_ID = int(env.get("OWNER_ID", 5191354193))
    ALLOWED_USER_IDS = env.get("ALLOWED_USER_IDS", "").split()
    BOT_USERNAME = env.get("TELEGRAM_BOT_USERNAME", "File_to_link_vobix_bot")
    BOT_TOKEN = env.get("TELEGRAM_BOT_TOKEN", "6989863418:AAHGbxzYTP76XEnpb4IrJYPxMhL5sp4u1uw")
    CHANNEL_ID = int(env.get("TELEGRAM_CHANNEL_ID", -1002094999032))
    SECRET_CODE_LENGTH = int(env.get("SECRET_CODE_LENGTH", 12))

class Server:
    BASE_URL = env.get("BASE_URL", "https://filededebhai.onrender.com")
    BIND_ADDRESS = env.get("BIND_ADDRESS", "0.0.0.0")
    PORT = int(env.get("PORT", 8080))

# LOGGING CONFIGURATION
LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'event-log.txt',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'uvicorn': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'uvicorn.error': {
            'level': 'WARNING',
            'handlers': ['file_handler', 'stream_handler']
        },
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}
