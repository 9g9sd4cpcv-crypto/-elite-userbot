from telethon import TelegramClient, events
import os
from config import *

bot = TelegramClient("userbot", API_ID, API_HASH).start(string_session=STRING)

# Load all modules
for file in os.listdir("modules"):
    if file.endswith(".py"):
        __import__(f"modules.{file[:-3]}")

print("🚀 Bot Running...")

bot.run_until_disconnected()
