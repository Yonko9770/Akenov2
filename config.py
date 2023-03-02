from os import getenv

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    LOGGER = True

    API_ID = int(getenv("API_ID", 6))
    API_HASH = getenv("API_HASH", None)
    ARQ_API_KEY = " VVNCDW-NIBQUU-QKDTOM-JTRWBQ-ARQ"
    STRING_SESSION = getenv("STRING_SESSION", None)
    SPAMWATCH_API = None
    TOKEN = getenv("TOKEN", None)
    OWNER_ID = int(getenv("OWNER_ID", "5700727404"))  # sᴛᴀʀᴛ @Exon_Robot ᴛʏᴘᴇ /id
    OWNER_USERNAME = getenv("OWNER_USERNAME", "YeahKakashi")
    SUPPORT_CHAT = getenv("SUPPORT_CHAT", "Devs_discuissons")
    LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001809288523"))
    MONGO_URI = getenv("MONGO_DB_URI")
    REDIS_URL = "redis://Kakashi:.Sonu1234@redis-19899.c60.us-west-1-2.ec2.cloud.redislabs.com:19899"
    DATABASE_URL = getenv("DATABASE_URL")

    # ɴᴏ ᴇᴅɪᴛ ᴢᴏɴᴇ
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://")


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
