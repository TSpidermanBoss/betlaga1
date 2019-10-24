from pyrogram import Client, Filters
from pyrogram.errors import FloodWait
import time

k = -1001276271867
u = 876549651
bot = "947122434:AAGEIyLLZ-izEihY7-pmxumsvsZXnBQpz-g"

app =Client("mn",bot_token= bot ,api_id=605563,api_hash="7f2c2d12880400b88764b9b304e14e0b") 

@app.on_message( Filters.text & ~Filters.edited & Filters.channel)
def forward(client, Message):
 fil = open("source.txt" , "r")
 lins = fil.readlines()
 fil.close()
 for t in lins:
  if int(t) == Message.chat.id:
   mes = client.send_message(k,Message.text.markdown)
   fie = open("ids.txt","a")
   fie.write(" " + str(Message.message_id) + " " + str(mes.message_id))
   fie.close()   
@app.on_message( Filters.text & Filters.edited & Filters.channel)
def forward(client, Message):
 fil = open("source.txt" , "r")
 lins = fil.readlines()
 fil.close()
 for t in lins:
  if int(t) == Message.chat.id:
   file = open("ids.txt" , "r")
   lines = file.readlines()
   file.close()
   for line in lines:
    x = line.split()
    id = str(Message.message_id)
    if id in x:
     try:
      if Message.text == ".":   
       client.delete_messages(k,int(x[x.index(id)+1]))
      else:
       client.edit_message_text(k,int(x[x.index(id)+1]),Message.text.markdown)
     except FloodWait as e:
      time.sleep(e.x)
@app.on_message(Filters.command("set") & Filters.user(u))
def forward(client, message):
  x = message.text.split(" ")[1]
  if x.casefold() == "ferrari".casefold():
   with open("source.txt" , "w") as file:
    file.write("-1001165875030")
    file.close()
    message.reply("☢️ Service Bot ** " + x + " **✅✅")
  elif x.casefold() == "bullet".casefold():
   with open("source.txt" , "w") as file:
    file.write("-1001483523101")
    file.close()
    message.reply("☢️ Service Bot ** " + x + " **✅✅")
  elif x.casefold() == "live".casefold():
   with open("source.txt" , "w") as file:
    file.write("-1001224667055")
    file.close()
    message.reply("☢️ Service Bot ** " + x + " **✅✅")
  elif x.casefold() == "prince".casefold():
   with open("source.txt" , "w") as file:
    file.write("-1001403061160")
    file.close()
    message.reply("☢️ Service Bot ** " + x + " **✅✅")
  elif x.casefold() == "off".casefold():
   with open("source.txt" , "w") as file:
    file.write("555844444919193103")
    file.close()
    message.reply("☢️ Service Bot ** " + x + " **✅✅")
  else:
    Message.reply(" **Line not exist !!** ")
@app.on_message(Filters.command("Clear") & Filters.user(u))
def forward(client, message):
  with open("ids.txt" , "w") as file:
   file.write("0001")
   file.close() 
   message.reply("☢️ Done, Editing data cleared ✅✅")
@app.on_message(Filters.command("help") & Filters.user(u))
def forward(client, message):
 message.reply("""🤖 Bot version 0.2.0 :

Available Commands:
👉 1. ```/set x```
 
 X in line name available lines - Ferrari , Bullet , Live, Prince , off

ex. ```/set ferrari``` to set line as ferrari

👉 2. ```/clear```
 
 use this command after every match to make bot clear and fast 

For more info - @Google_Console """)

app.run()
