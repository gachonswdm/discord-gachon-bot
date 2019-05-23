import discord

from discord.ext import commands

bot = commands.Bot(command_prefix=';;;')
KEY = "please_type_a_discord_key"

print('Discord Gachon-Bot Online.')

bot.remove_command('help')


@bot.command()
async def help(ctx):
    await ctx.send('난 아직 아무것도 못해! 미안!')

@bot.command(name="안녕")
async def _hi(ctx):
    await ctx.send('안녕!')

bot.run(KEY)