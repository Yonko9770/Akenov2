import re
from pyrogram import filters
from pyrogram.types import message
from Exon import abishnoi

@pbot.on_message(

    filters.text

    & filters.regex(r"\b[Kk][Aa][Kk][Aa][Ss][Hh][Ii]\b")

    & ~filters.via_bot

    & ~filters.bot,

)

async def upvote(_, message: Message):

    text = message.text

    match = re.search(r"(?<=\b[Kakashi]\b\s)\w+", text)

    if match:

        word = match.group()

        word = word.lower().capitalize()

        return await message.reply_text(f"Hello {word}! I am Dad.")

    return
