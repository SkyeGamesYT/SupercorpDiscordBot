import discord
import os
import asyncio
import datetime
import sqlite3
import aiohttp
import random
import roblox
import roblox.thumbnails
from typing import Optional
from key_generator.key_generator import generate
from wonderwords import RandomSentence
from discord import ui, ButtonStyle, client, member
from discord.app_commands.commands import describe
from discord.ext import commands
from roblox import Client, utilities, thumbnails, groups, members
from roblox.thumbnails import AvatarThumbnailType



connection = sqlite3.connect("database.sqlite")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS warningsdb (user_id INTEGER, reason TEXT, moderator TEXT, warn_id TEXT)")
connection.commit()


help_command = commands.DefaultHelpCommand(
  no_category = 'Misc'
)



bot = commands.Bot(
  command_prefix = "!",
  intents = discord.Intents.all(),
  help_command = help_command,
  activity = discord.Activity(type=discord.activity.ActivityType.watching, name = "Supercorp Employees", status = discord.Status.idle)
)

@bot.event
async def setup_hook():
  for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
      await bot.load_extension(f'cogs.{filename[:-3]}')
      print('Loaded cog: {filename[:-3]}')
    else:
      print("Unable to load pycache folder.")




@bot.event
async def on_ready():
  print("Bot is ready.")
  print('Logged in as {bot.user}')



bot.run("TOKEN")
      
