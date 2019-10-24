from pyrogram import Client, Filters
import time
from pyrogram.errors import FloodWait
k = -1001346922022
bot = "776837328:AAEt8G_RynqZavp72pB3XwH3bbnN8ZDfei4"
app = Client(session_name="rr",api_id=814511,api_hash="44462f0f278503255d5cc30941b617a9",bot_token = bot)                                   
bullet = -1001378725482                                                                                           
@app.on_message(Filters.chat(bullet) & ~ Filters.edited & Filters.channel)
def main(client, Message):
 mes = client.send_message(k,Message.text.markdown)
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
      client.edit_message_text(k,int(x[x.index(id)+1]),Message.text.markdown)
   except FloodWait as e:
     time.sleep(e.x)
@app.on_message(Filters.command("clear1"))
def main(client, message):
 with open("sure.txt" , "w") as files:
  files.write("000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000")
  files.close()
  message.reply("Done")
app.run()
