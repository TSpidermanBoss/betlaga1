from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import time
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
