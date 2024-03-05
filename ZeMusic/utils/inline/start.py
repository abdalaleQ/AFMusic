from pyrogram.types import InlineKeyboardButton

import config
from ZeMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضف البوت الى مجموعتك",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="الأوامر", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="مطور السورس", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="قناة السورس", url=config.SUPPORT_CHANNEL),
        ],
        [
         
            InlineKeyboardButton(text="𝗠𝗜𝗨𝗭𝗜𝗞 𝗔𝗟𝗭𝗔𝗘𝗜𝗠", url=f"https://t.me/T_5_G"),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضف البوت الى مجموعتك",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="الأوامر", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="مطور السورس", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="قناة السورس", url=config.SUPPORT_CHANNEL),
        ],
        [
         
            InlineKeyboardButton(text="𝗠𝗜𝗨𝗭𝗜𝗞 𝗔𝗟𝗭𝗔𝗘𝗜𝗠", url=f"https://t.me/EEEW2"),
        ],
    ]
    return buttons
