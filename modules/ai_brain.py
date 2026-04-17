from telethon import events
from main import bot
import os
from openai import OpenAI
import random

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@bot.on(events.NewMessage)
async def ai(event):
    if not event.is_group:
        return

    msg = event.raw_text

    # avoid commands
    if msg.startswith("."):
        return

    # random reply chance
    if random.randint(1,100) > 10:
        return

    try:
        res = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "Reply short, casual, Hindi/Hinglish allowed"},
                {"role": "user", "content": msg}
            ],
            max_tokens=80
        )

        reply = res.choices[0].message.content
        await event.reply(reply)

    except Exception as e:
        print("AI error:", e)
