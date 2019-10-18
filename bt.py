from pyrogram import Client, Filters
from pyrogram.errors import FloodWait
import time
app =Client("mn",bot_token= "957765060:AAHnyj00seUNDAAWe4dYAeUoLMNx15PE6PY",api_id=605563,api_hash="7f2c2d12880400b88764b9b304e14e0b") 
k = -1001418036927
u = 1243874983
@app.on_message( Filters.text & ~Filters.edited & Filters.channel)
def forward(client, message):
 fil = open("source.txt" , "r")
 lins = fil.readlines()
 fil.close()
 for t in lins:
  if int(t) == message.chat.id:
   mes = client.send_message(k,message.text)
   fie = open("ids.txt","a")
   fie.write(" " + str(message.message_id) + " " + str(mes.message_id))
   fie.close()   
@app.on_message( Filters.text & Filters.edited & Filters.channel)
def forward(client, message):
 fil = open("source.txt" , "r")
 lins = fil.readlines()
 fil.close()
 for t in lins:
  if int(t) == message.chat.id:
   file = open("ids.txt" , "r")
   lines = file.readlines()
   file.close()
   for line in lines:
    x = line.split()
    id = str(message.message_id)
    if id in x:
     try:
      client.edit_message_text(k,int(x[x.index(id)+1]),message.text)
     except FloodWait as e:
      time.sleep(e.x)
@app.on_message(Filters.command("set") & Filters.user(u))
def forward(client, message):
  x = message.text.split(" ")[1]
  if x.casefold() == "ferrari".casefold():
   with open("source.txt" , "w") as file:
    file.write("-1001452956784")
    file.close()
    message.reply("☢️ Service Bot ** " + x + " **✅✅")
  elif x.casefold() == "bullet".casefold():
   with open("source.txt" , "w") as file:
    file.write("-1001152344101")
    file.close()
    message.reply("☢️ Service Bot ** " + x + " **✅✅")
  elif x.casefold() == "live".casefold():
   with open("source.txt" , "w") as file:
    file.write("-1001468447534")
    file.close()
    message.reply("☢️ Service Bot ** " + x + " **✅✅")
  elif x.casefold() == "Prince".casefold():
   with open("source.txt" , "w") as file:
    file.write("-1001391066413")
    file.close()
  elif x.casefold() == "off".casefold():
   with open("source.txt" , "w") as file:
    file.write("offline")
    file.close()
    message.reply("☢️ Service Bot ** " + x + " **✅✅")
  else:
   Message.reply("**Line not exist !!**")
@app.on_message(Filters.command("Clear") & Filters.user(u))
def forward(client, message):
  with open("ids.txt" , "w") as file:
   file.write("0001")
   file.close() 
   message.reply("Done,editing Data cleared !!")
@app.on_message(Filters.command("help") & Filters.user(u))
def forward(client, message):
 message.reply("""🤖 Bot version 0.2.0 :

Available Commands:
👉 1. ```/set x```
 
x in line name available lines - Ferrari , Bullet , Live, Prince , off

ex. ```/set ferrari`` to set line as ferrari

👉 2. ```/clear```
 
 use this command after every match to make bot clear and fast 

For more info - @Google_Console """

app.run()
