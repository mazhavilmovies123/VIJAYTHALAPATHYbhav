import asyncio, os, sys
from info import ADMINS
from pyrogram import Client, filters

@Client.on_message(filters.command("restart") & filters.user(ADMINS))
async def stop_button(bot, message):
    msg = await message.reply(text="♨️")       
    await asyncio.sleep(3)
    await msg.edit("✅")
    os.execl(sys.executable, sys.executable, *sys.argv)
