# (c) @biisal
from os import getenv
import re

id_pattern = re.compile(r"^.\d+$")


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


ADMIN = int(getenv("ADMIN", "6230062482"))
API_ID = int(getenv("API_ID", "28341884"))
API_HASH = str(getenv("API_HASH", "ca0c9295ce3ec910fd6f49e99970d9a8"))
BOT_TOKEN = str(getenv("BOT_TOKEN", ""))
MONGO_DB = str(
    getenv(
        "MONGO_DB",
        "mongodb+srv://ashuroy761:YYBzDc7XWi85sRPE@cluster0.umhohdy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    )
)
DEF_CAP = str(
    getenv(
        "DEF_CAP",
        "<b><a href='telegram.me/LDC_OFFICIAL'>{file_name} Telegram : @LDC_OFFICIAL\n\nForward the file before Downloading.</a></b>",
    )
)
