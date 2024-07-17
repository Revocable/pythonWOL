import discord
from discord.ext import commands
from wakeonlan import send_magic_packet
import os

# Token do bot do Discord
BOT_TOKEN = ''
MAC_ADDRESS = ''
IP_ADDRESS = '192.168.0.60'  

# Configura o bot
intents = discord.Intents.default()
intents.message_content = True  
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.command()
async def wake(ctx):
    send_magic_packet(MAC_ADDRESS)
    await ctx.send(f'Wake-on-LAN packet enviado para o dispositivo com IP {IP_ADDRESS} e MAC {MAC_ADDRESS}')

@bot.command()
async def ping(ctx):
    response = os.system(f'ping -c 1 {IP_ADDRESS}')
    if response == 0:
        await ctx.send(f'O dispositivo com IP {IP_ADDRESS} está online.')
    else:
        await ctx.send(f'O dispositivo com IP {IP_ADDRESS} está offline.')

# Inicia o bot
bot.run(BOT_TOKEN)
