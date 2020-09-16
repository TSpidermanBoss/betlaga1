from pyrogram import Client, filters
s = -100
@app.on_message(filters.chat(s) & ~ filters.edited)
async def main(client, message):
 file = open("ferrari.txt","r")
 lines = file.readlines()
 file.close()
 for line in lines:
  p = line.split()
  for r in p: 
    mes = await client.send_message(int(r),message.text)
    fie = open(str(r)+".txt","a")
    fie.write(" " + str(message.message_id) + " " + str(mes.message_id))
    fie.close()
