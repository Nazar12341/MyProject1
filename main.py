
import discord
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

bot.run("MTIzNjMwMjY5ODk0OTY0MDIxNA.Gjffh-.YhOgE4Siri7XWjC5_kXSuVXn2hAHxlLuIVPcEg")
