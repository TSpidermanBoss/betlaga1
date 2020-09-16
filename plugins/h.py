from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import time

@app.on_message(filters.command('reset') & filters.user(491634139))
async def forward(client, message):
 with open("ferrari.txt" , "w") as g:
  g.write("-1001353340635")
  g.close()
 with open("bullet.txt" , "w") as g:
  g.write("-1001353340635")
  g.close()
 with open("ids.txt" , "w") as g:
  g.write("-1001353340635")
  g.close()
 await message.reply("done")

