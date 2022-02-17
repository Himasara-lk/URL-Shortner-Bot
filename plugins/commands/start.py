# Author: TRTECHGUIDE (https://github.com/TR-TECH-GUIDE) (@TR-TECH-GUIDE)

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

START_TEXT = """
Hello {} 🌿
I'm link shortner Bot 

🌼 Url Types 

• http://Clck.ru
• https://da.gd/lgNjp
• http://Is.gd
• http://Osdb.link
• http://GPLinks.in

"""






START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🍃 Join My Updates 🍃', url='https://telegram.me/AltexUpdates')
        ]]
    )

@Client.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        reply_markup=START_BUTTONS,
        disable_web_page_preview=True
    )
