from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import time

@app.on_message(filters.command('remove') & filters.user(491634139))
async def forward(client, message):
 if len(message.text.split(' ')) > 2:
  if len(message.text.split(' ')[1]) == 14:
   file = open(message.text.split(" ")[2] + ".txt" , "r")
   u = file.readlines()
   file.close()
   for v in u:
     lines = v.split() 
     del lines[lines.index(message.text.split(' ')[1])]
     y = " ".join(str(x) for x in lines)
     files = open(message.text.split(" ")[2] + ".txt" , "w") 
     files.write(y)
     files.close()
     await message.reply("💾 Done, The chat_id  ```" + message.text.split(' ')[1] +"```🌐 has been removed to my database. ✅✅")
  else:
    await message.reply("💼 Please write a valid chat id. ✅✅ ")
 else:
    await message.reply("💼 Please write a valid chat id. ✅✅ ")
