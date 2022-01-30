import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from SeiraRobot.events import register as MEMEK
from SeiraRobot import telethn as tbot

PHOTO = "https://telegra.ph/file/e97ec5658f72c4a54438b.jpg"

@MEMEK(pattern=("/alive"))
async def awake(event):
  tai = event.sender.first_name
  LUNA = "**Holla I'm ᴍᴀᴢʜᴜɪxɪ ʀᴏʙᴏᴛ!** \n\n"
  LUNA += "💎 **I'm Working Properly** \n\n"
  LUNA += "💎 **My Master : [ᴀʀᴅᴇx★](https://t.me/siardx)** \n\n"
  LUNA += f"💎 **Telethon Version : {tlhver}** \n\n"
  LUNA += f"💎 **Pyrogram Version : {pyrover}** \n\n"
  LUNA += "**Terima kasih sudah menambahkan ᴍᴀᴢʜᴜɪxɪ ʀᴏʙᴏᴛ 💜**"
  BUTTON = [[Button.url("ʜᴇʟᴘ", "https://t.me/mzxirobot?start=help"), Button.url("ʀᴇᴘᴏ", "www.xnxx.com")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LUNA,  buttons=BUTTON)

