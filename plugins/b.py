from pyrogram import Client, Filters
from pyrogram.errors import FloodWait
s = -100
@app.on_message(Filters.chat(s) & Filters.edited)
def main(client, message):
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
       client.delete_messages(int(m),int(x[x.index(id)+1]))
      else:
       client.edit_message_text(int(m),int(x[x.index(id)+1]),message.text.markdown )
     except FloodWait as e:
       time.sleep(e.x)
