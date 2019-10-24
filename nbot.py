from pyrogram import Client, Filters
import time
from pyrogram.errors import FloodWait
k = -1001478028300
bot = "922312177:AAEx5q8NXF698oiahS-UU94D3B6MlzMLd2g"
app = Client (session_name="rr",api_id=814511,api_hash="44462f0f278503255d5cc30941b617a9",bot_token = bot)                                   
bullet = -1001289914295                                                                                           
@app.on_message(Filters.chat(bullet) & ~ Filters.edited & Filters.channel)
def main(client, Message):
 mes = client.send_message( k,Message.text)
 with open("sure.txt", "r") as f:
  x = f.readlines()
 y = [j for j in x[0].split(" ")]
 del y[:2]
 y = " ".join(str(x) for x in y)
 o = open("sure.txt","w")
 o.write(y + " " +str(Message.message_id) + " " + str(mes.message_id))
 o.close() 
@app.on_message(Filters.chat(bullet) & Filters.edited & Filters.channel)
def main(client, Message):
 files = open("ids.txt" , "r")
 d = files.readlines()
 files.close()
 for c in d:
  x = c.split()
  id = str(Message.message_id)
  if id in x:
   try:
     if Message.text == ".":   
      client.delete_messages(k,int(x[x.index(id)+1]))
     else:
      client.edit_message_text(k,int(x[x.index(id)+1]),Message.text)
   except FloodWait as e:
     time.sleep(e.x)
@app.on_message(Filters.command("clear1"))
def main(client, message):
 with open("sure.txt" , "w") as files:
  files.write("000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000")
  files.close()
  message.reply("Done")
app.run()
