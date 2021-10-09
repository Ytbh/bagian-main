import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix='?', intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)



client.run ("ODk2NDc4NjczMzEyNTc1NTQw.YWHs0w.1Vm0m1oQp2eYYjcfkCTgDsRs0C8")
