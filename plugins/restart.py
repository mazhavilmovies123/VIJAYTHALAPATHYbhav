import sys
import asyncio
from os import environ, execle, system
from pyrogram import Client, filters, enums
from info import ADMINS

@Client.on_message(filters.command(['restart']) & filters.user(ADMINS))
async def restart(client, message):
    msg = await message.reply_text(
        text="<b>Bot Restarting ...</b>"
    )
    await asyncio.sleep(5)
    await msg.edit("<b>Restart Successfully Completed ✅</b>")
    system("git pull -f && pip3 install --no-cache-dir -r requirements.txt")
    execle(sys.executable, sys.executable, "bot.py", environ)
