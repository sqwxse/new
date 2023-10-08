import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)


@bot.event
async def on_ready():
  print("Я готов!")


@bot.command()
async def hello(ctx):
  await ctx.send("Привет, человек!")


@bot.command()
async def bye(ctx):
  await ctx.send("Пока, человек!")

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')




bot.run("MTE1Nzk3NTIwMjEyMzIzMTI4Mg.G-Wmg_.1mWoxiErZpSOZW3lxmJE_fylLqdc4hxBifa1C4")