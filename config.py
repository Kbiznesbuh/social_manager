import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_MASTER_CHAT_ID = os.getenv("TELEGRAM_MASTER_CHAT_ID")

VK_GROUP_TOKEN = os.getenv("VK_GROUP_TOKEN")
VK_GROUP_ID = os.getenv("VK_GROUP_ID")
VK_CONFIRMATION_TOKEN = os.getenv("VK_CONFIRMATION_TOKEN")