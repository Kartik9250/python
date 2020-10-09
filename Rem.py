import discord
import mysql.connector as sql
from datetime import date
from tabulate import tabulate

records = [0]
sno = [0]
jades = [0]
events = [0]
dates = [0]
TOKEN = "NjcxNzg4NTI1OTM4NjcxNjQ3.XjCB0Q.Xs6FguVIF26eKpez3vsbh6Z-C0A"

mycon = sql.connect(host = "localhost", user = "kartik", password = "9250", database = "rem")
cur = mycon.cursor()
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    if message.content.startswith('$your name?'):
        await message.channel.send('Rem owo')
        
    if message.content.startswith('$addentry'):
        try:
            themessage = message.content.split(' ')
            jades.append(int(themessage[1]))
            events.append(themessage[2])
            sno.append(sno[-1]+1)
            dt = date.today()
            dates.append(dt.strftime('%Y/%m/%d'))
            records.append([sno[-1], jades[-1], events[-1], dates[-1]])
            
            await message.channel.send("Okay, done.\n\n"+tabulate(records[-1:], headers=["Sno.", "Jades", "Event", "Date"], tablefmt='simple')+"\n\nThis entry was added to the records")
            
        except:
            await message.channel.send("Error... record couldn't be added")
        sql = "insert into records values(, %s, %s, %s)"
        val = (int(themessage[1]), themessage[2], dt)
        cur.execute(sql, val)
        mycon.commit()
    
    if message.content.startswith('$showall'):
        try:
            print(jades)
            sums = 0
            for i in jades:
                sums += i
            print(records[1:])    
            await message.channel.send("Here's our guild jades records:\n\n"+tabulate(records[1:], headers=["Sno.", "Jades", "Event", "Date"], tablefmt='simple')+"\n\ncurrent balance:"+str(sums))
       
        except:
            await message.channel.send("Error... records couldn't be found")
    
    if message.content.startswith('$rmventry'):
        try:
            themessage = message.content.split(' ')
            sno.pop(int(themessage[1]))
            jades.pop(int(themessage[1]))
            events.pop(int(themessage[1]))
            dates.pop(int(themessage[1]))
            await message.channel.send("Okay, done.\n\n"+tabulate(records[int(themessage[1]):], headers=["Sno.", "Jades", "Event", "Date"], tablefmt='simple')+"\n\nThis entry was removed from the records")
            records.pop(int(themessage[1]))
        
        except:
            await message.channel.send("Error... record couldn't be removed")

client.run(TOKEN)