from telethon import events
from main import bot

bad_words = ["mc", "bc", "chutiya", "gandu"]

@bot.on(events.NewMessage)
async def filter(event):
    if not event.is_group:
        return

    msg = event.raw_text.lower()

    for word in bad_words:
        if word in msg:
            await event.delete()
            await event.reply("🚫 Bad language not allowed")
            break
