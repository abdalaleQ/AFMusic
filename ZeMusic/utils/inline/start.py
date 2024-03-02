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
            InlineKeyboardButton(text="ᗪEᐯEᒪOᑭEᖇ", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="ᑕᕼᗩᑎᑎEᒪ", url=config.SUPPORT_CHANNEL),
        ],
        [
         
            InlineKeyboardButton(text="سورس الزعيم", url=f"https://t.me/T_5_G"),
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
            InlineKeyboardButton(text="ᗪEᐯEᒪOᑭEᖇ", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="ᑕᕼᗩᑎᑎEᒪ", url=config.SUPPORT_CHANNEL),
        ],
        [
         
            InlineKeyboardButton(text="سورس الزعيم", url=f"https://t.me/EEEW2"),
        ],
    ]
    return buttons
