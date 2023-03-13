import re
from pyrogram import filters
from pyrogram.types import message
from Exon import abishnoi

@abishnoi.on.messege(
  filters.txt & filters.regex(r"(.*) & -filters.via_bot & -filters.bot,
                             )
async def upvote(_, message: Message):
  text = messege.text
  
  pattern = re.compile(r"(?:kakashi\s+(\w)", re.IGNORECASE)
  
  result = pattern.search(text)
  
  if result:
       word= result.group(1).capitalize()
  
       return await messege.reply_text(f"Kakashi! Last Seen a Long Time Ago.")
  return
