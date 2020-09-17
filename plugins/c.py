from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import time
@app.on_message(filters.command('add') & filters.user(491634139) )
async def forward(client, message):
 if len(message.text.split(' ')) > 2:
  if len(message.text.split(' ')[1]) == 14:
   with open(message.text.split(" ")[2] + ".txt" , "r") as file:
    lines = file.readlines()
    file.close()
    for line in lines:
     files = open(message.text.split(" ")[2] + ".txt" , "w") 
     files.write(line + " " + message.text.split(' ')[1])
     files.close()
     with open(message.text.split(' ')[1]+".txt" , "w") as g:
       g.write("001 002")
       g.close()
     await message.reply("💾 Done, The chat_id  ```" + message.text.split(' ')[1] +"```🌐 has been added to my database. ✅✅")
  else:
    await message.reply("💼 Please write a valid chat id. ✅✅ ")
 else:
   await message.reply("💼 Please write a valid chat id. ✅✅ ")

   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   with concurrent.futures.ThreadPoolExecutor(max_workers=100000) as executor:
 executor.map(coder,lines[0].split())
