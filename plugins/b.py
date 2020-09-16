from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import time
s = -100
@app.on_message(filters.chat(s) & filters.edited)
async def main(client, message):
 file = open("ferrari.txt" , "r")
 lines = file.readlines()
 file.close()
 for line in lines:
  t = line.split()
  for m in t:
   files = open(str(m)+".txt" , "r")
   d = files.readlines()
   files.close()
   for c in d:
    x = c.split()
    id = str(message.message_id)
    if id in x:
     try:
      if message.text == ".":
       await client.delete_messages(int(m),int(x[x.index(id)+1]))
      else:
       await client.edit_message_text(int(m),int(x[x.index(id)+1]),message.text)
     except FloodWait as e:
       time.sleep(e.x)
