import discord
import random
from discord.ext import commands
from random import randint

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

pet = {
    'health': 100,
    'defence': 10,
    'strength': 10
}

@bot.command('feed')
async def feed(message):
    pet['health'] +=10
    pet['defence'] +=10
    await message.send('Ваш питомец хорошо поел:' + str(pet))

@bot.command('train')
async def train(message):
    pet['health'] -=10
    pet['defence'] +=10
    pet['strength'] +=10
    await message.send('Ваш питомец потренировался:' + str(pet))

@bot.command('fight')
async def fight(message):
    enemy = {
    'health': randint(1,100),
    'defence': randint(1,10),
    'strength': randint(1,10)
    }
    await message.send('Бой начался')
    while enemy['health'] >= 0 and pet['health'] >= 0:
        pet['health'] -= enemy['strength'] - pet['defence']
        enemy['health'] -= pet['strength'] - enemy['defence']
        await message.send('ваш питомец:' + str(pet))
        await message.send('ваш враг:' + str(pet))
    if enemy['health'] > pet['health']:
        await message.send('Вы проиграли')
    else:
        await message.send('Вы выйграли')
        
@bot.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Да, бот крутой.')


bot.run("Token")
