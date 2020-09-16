from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import time

@app.on_message(filters.command('get') & filters.user(491634139) )
async def forward(client, message):
 if len(message.text.split(' ')) > 1:
  if len(message.text.split(' ')[1]) == 14:
      x = client.get_chat(int(message.text.split(' ')[1])).title
      await message.reply("📶 This chat name is - "+str(x)+" ✅")
  else:
    await message.reply("💼 Please write a valid chat id. ✅✅ ")
 else:
    await message.reply("💼 Please write a valid chat id. ✅✅ ")
