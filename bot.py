import discord
from discord.ext import commands
from bot_logic import pass_gen
from bot_emoji import emo_send

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
async def emoji(ctx):
    await ctx.send("Seu emoji é" + emo_send())

@bot.command()
async def gif(ctx):
    await ctx.send("https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExeXpwcW9iZWI4bXc4eWNjbmg4aGN3dmgybm9jbzNsMmRyd3lrM2FmbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/13hxeOYjoTWtK8/giphy.gif")

@bot.command()
async def membros(ctx):
    guild = ctx.guild
    await ctx.send(f'Esse servidor possui {guild.member_count} membros contando comigo!')

@bot.command()
async def id(ctx, member: discord.Member = None):
    member = member or ctx.author
    await ctx.send(f'O ID do membro {member.name} é {member.id}')


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

    

bot.run("Seu token aqui!!!")
