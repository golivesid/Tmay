from os import environ


# BOT CONFIG
API_ID = environ.get("API_ID", 23054736)  # api id
API_HASH = environ.get("API_HASH", "d538c2e1a687d414f5c3dce7bf4a743c")  # api hash
BOT_TOKEN = environ.get("BOT_TOKEN", "7054995045:AAE28DVn868-Q0dC5vZMLXHhJAeWzSfGUdI")  # bot token

# REDIS
REDIS_HOST = environ.get("REDIS_HOST", "redis-18149.c238.us-central1-2.gce.redns.redis-cloud.com")  # redis host uri
REDIS_PORT = environ.get("REDIS_PORT", 18149)  # redis port
REDIS_PASSWORD = environ.get(
    "REDIS_PASSWORD", "O4HBLjcseISfJUrqarK7C81dTt5TVAlW"
)  # redis password


ADMINS = [1352497419]
OWNER_ID = 1352497419  # Replace with your Telegram user ID
PRIVATE_CHAT_ID = -1002146782406 # CHAT WHERE YOU WANT TO STORE VIDEOS
USER_CHANNEL = -1002146782406
DUMP_CHANNEL = -1002146782406


# Config
COOKIE = environ.get("COOKIE", "csrfToken=2Xt_GjKVx2fFHprVbYihHl08; browserid=mDwNyi7Q175GXXV9cgXemTb0X-itapo0iPC0S_kml8xEp94Ln6Tm4ozsQhk=; lang=en; TSID=cjd0jehIubIkD9IGhwhfI341JoOWu306; __bid_n=18f8a3e8186ead07d44207; _ga=GA1.1.904130167.1716011304; ndus=YfaJ0KyteHuixkwlCxCenK87CvgUl7kFXg0GSnFF; ndut_fmt=877293CD19D538C40B83219E9F41B02C17B3893E5E3937E532ABACF2B53CF496; _ga_06ZNKL8C2E=GS1.1.1716041697.3.0.1716042291.60.0.0")
