import discord
from discord.ext import commands
from bot_logic import pass_gen


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

    
@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! eu sou um bot {bot.user}!')

@bot.command()
async def bye(ctx):    
    await ctx.send("\U0001f642")

@bot.command()
async def senha(ctx):
    await ctx.send("Sua senha é " + pass_gen(10))

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

    

bot.run("Seu token aqui!!!")
