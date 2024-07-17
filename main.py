import discord
from discord.ext import commands
from wakeonlan import send_magic_packet

# Token do bot do Discord
BOT_TOKEN = ''
MAC_ADDRESS = ''  # Endereço MAC do dispositivo que você deseja acordar

# Configura o bot
intents = discord.Intents.default()
intents.message_content = True  # Ativa a intenção de conteúdo de mensagens
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.command()
async def wake(ctx):
    send_magic_packet(MAC_ADDRESS)
    await ctx.send(f'Wake-on-LAN packet enviado para o dispositivo com IP 192.168.0.60 e MAC {MAC_ADDRESS}')

# Inicia o bot
bot.run(BOT_TOKEN)
