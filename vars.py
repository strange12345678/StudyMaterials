import os
from typing import List

API_ID = int(os.getenv("API_ID", "22582906"))
API_HASH = os.getenv("API_HASH", "e3096dde3e27c72a50e0e53d8ab23d6a")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
MONGO_URI = os.getenv("MONGO_URI", " ")
DATABASE_CHANNEL_ID = int(os.getenv("DATABASE_CHANNEL_ID", "-1002739849822"))
ADMIN_ID = int(os.getenv("ADMIN_ID", "7861690278"))
PICS = (os.environ.get("PICS", "https://i.ibb.co/ZRd3qRjS/photo-2025-08-02-18-04-42-7537167412588707856.jpg")).split()
LOG_CHNL = int(os.getenv("LOG_CHNL", "-1002789550852"))
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "DadyIsCalling") # Without @
IS_FSUB = bool(os.environ.get("FSUB", False))
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "").split()))
DATABASE_CHANNEL_LOG = int(os.getenv("DATABASE_CHANNEL_LOG", "-1002789550852"))
FREE_VIDEO_DURATION = int(os.getenv("FREE_VIDEO_DURATION", "240"))
