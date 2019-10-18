from pyrogram import Client, Filters
from pyrogram.errors import FloodWait
import time
app = Client("session",bot_token="863961400:AAG3kaHMrOsklKBP3fGEn7T4rTyC1dXkRTc",api_id=605563,api_hash="7f2c2d12880400b88764b9b304e14e0b") 
k = -1001289914295
@app.on_message(Filters.command("clr"))
def forward(client, message):
  with open("ids.txt" , "w") as file:
   file.write("0001")
   file.close() 
   message.reply("kk")
@app.on_message( Filters.text & ~Filters.edited)
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
@app.on_message( Filters.text & Filters.edited)
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
@app.on_message(Filters.command("set") & Filter.user("705138975"))
def forward(client, message):
  x = message.text.split(" ")
  if x.casefold() == "ferrari".casefold()
   with open("source.txt" , "w") as file:
    file.write("-1001452956784")
    file.close()
    message.reply("☢️ Done, Line has been changed to** " + x + " **✅✅")
  elif x.casefold() == "bullet".casefold()
   with open("source.txt" , "w") as file:
    file.write("-1001152344101")
    file.close()
    message.reply("☢️ Done, Line has been changed to** " + x + " **✅✅")
  elif x.casefold() == "live".casefold()
   with open("source.txt" , "w") as file:
    file.write("-1001468447534")
    file.close()
    message.reply("☢️ Done, Line has been changed to** " + x + " **✅✅")
  else:
   Message.reply("**Line not exist !!**")
app.run()
