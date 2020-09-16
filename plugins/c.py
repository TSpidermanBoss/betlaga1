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
@app.on_message(filters.command('clear') & filters.user(491634139))
async def forward(client, message):
    file = open(message.text.split(" ")[1] + ".txt" , "r")
    lines = file.readlines()
    file.close()
    for line in lines:
     p = line.split()
     for x in p:
        fie = open(str(x)+".txt","w")
        fie.write("001 002")
        fie.close()
        await message.reply("☢️ Done, Editing data cleared ✅✅")
@app.on_message(filters.command('list') & filters.user(491634139))
async def forward(client, message):
  file = open(message.text.split(" ")[1] + ".txt" , "r")
  u = file.readlines()
  file.close()
  for v in u :
      await message.reply("🏘️ List of Chat_ids in my database are ```" + str(v) + "```. Its can be change. ✅✅")
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

@app.on_message(filters.command('reset') & filters.user(491634139))
async def forward(client, message):
 with open("ferrari.txt" , "w") as g:
  g.write("-1001353340635")
  g.close()
 with open("bullet.txt" , "w") as g:
  g.write("-1001353340635")
  g.close()
 with open("ids.txt" , "w") as g:
  g.write("-1001353340635")
  g.close()
 await message.reply("done")


@app.on_message(filters.command("start"))
async def forward(client, message):
 if message.from_user.id == 491634139:
   await message.reply("♻️ Welcome to your LineBot . ✅✅")
 else:
   await message.reply("♻️ You need admins permission to use my functions. ✅✅")
@app.on_message(Filters.private)
async def forward(client, message):
 if not message.from_user.id == 491634139:
   message.reply("♻️ You need admins permission to use my functions. ✅✅")
