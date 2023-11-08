import sys, asyncio 
from os import environ, execle, system
from pyrogram import Client, filters, enums
from info import ADMINS

@Client.on_message(filters.command(['restart']) & filters.user(ADMINS))
async def restart(client, message):
    await message.reply_text("Rᴇꜱᴛᴀᴛɪɴɢ........")
    await asyncio.sleep(2)
    system("git pull -f && pip3 install --no-cache-dir -r requirements.txt")
    execle(sys.executable, sys.executable, "bot.py", environ)
