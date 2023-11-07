import asyncio, os, sys
from info import ADMINS
from pyrogram import Client, filters

@Client.on_message(filters.command("restart") & filters.user(ADMINS))
async def restart_bot(bot, msg):
    await msg.reply("Rᴇꜱᴛᴀᴛɪɴɢ........")
    await asyncio.sleep(2)
    await sts.delete()
    os.execl(sys.executable, sys.executable, *sys.argv)
