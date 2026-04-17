from telethon import events
from main import bot
import time

users = {}

@bot.on(events.NewMessage)
async def spam(event):
    if not event.is_group:
        return

    user = event.sender_id
    now = time.time()

    if user not in users:
        users[user] = []

    users[user].append(now)

    users[user] = [t for t in users[user] if now - t < 5]

    if len(users[user]) > 5:
        await event.delete()
        await event.reply("🚫 Spam detected")
