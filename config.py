from os import environ


# BOT CONFIG
API_ID = environ.get("API_ID", 23054736)  # api id
API_HASH = environ.get("API_HASH", "d538c2e1a687d414f5c3dce7bf4a743c")  # api hash
BOT_TOKEN = environ.get("BOT_TOKEN", "7054995045:AAF0J-BWYqKxYFyPRMpHFrapjMuhQINbsFA")  # bot token

# REDIS
REDIS_HOST = environ.get("REDIS_HOST", "localhost")  # redis host uri
REDIS_PORT = environ.get("REDIS_PORT", 12345)  # redis port
REDIS_PASSWORD = environ.get(
    "REDIS_PASSWORD", "q8vcRgGfoZgwKT6irvJ6AixPs1lFZdW8"
)  # redis password


ADMINS = [6791744215]
OWNER_ID = 6791744215  # Replace with your Telegram user ID
PRIVATE_CHAT_ID = -100  # CHAT WHERE YOU WANT TO STORE VIDEOS
USER_CHANNEL = -100
DUMP_CHANNEL = -100


# Config
COOKIE = environ.get("COOKIE", "")
