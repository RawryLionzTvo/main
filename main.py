import discord
from botmantik import gen_pass

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$Hoş Geldiniz!'):
        await message.channel.send("Selam!")
    elif message.content.startswith('$Daha Sonra Görüşürüz!'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith("/pass"):
        await message.channel.send(gen_pass(15))
    else:
        await message.channel.send(message.content)

client.run("")
