import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","‹ السورس ›","الزعيم","مطور السورس", "السورس "])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/caeef4bf2ba9bf4f723cd.jpg",
        caption=f"""╭──── • ◈ • ────╮
么 [َ  قناة السورس (t.me/VVV5P)
么 [َ جروب الزعيم](t.me/EEEW2)
么 [َ مطور السورس ](t.me/T_5_G)
╰──── • ◈ • ────╯
⍟ 𝙎𝙐𝙍𝙎 𝙈𝙄𝙐𝙕𝙄𝙆 𝘼𝙇𝙕𝘼𝙀𝙄𝙈  """,
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "‹  مطور السورس  . 🕷 › ", url=f"https://t.me/T_5_G"),
                ],[
                    InlineKeyboardButton(
                        "‹ قناة السورس›", url=f"https://t.me/VVV5P"), 
                    InlineKeyboardButton(
                        "‹ جروب السورس›", url=f"https://t.me/EEEW2"),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف البوت لمجموعتك ›", url=f"https://t.me/A_Rn_obot?startgroup=true"),
            ]
        ]
         ),
     )
  
