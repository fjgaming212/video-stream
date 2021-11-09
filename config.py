import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Kyy Music")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "IDnyaKosong")
ALIVE_NAME = getenv("ALIVE_NAME", "Kyy")
BOT_USERNAME = getenv("BOT_USERNAME", "Kyymusiicbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Kyymusicassistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "FlicksSupport")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ahhsudahlahhh")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/2b610c918dec590d2777b.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
