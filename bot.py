import os
import logging
import traceback
import sys

import discord

import json_manager

from dotenv import load_dotenv

from todo import ToDoManager
from commands.manager_commands import MANAGER_COMMANDS

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL = os.getenv('DISCORD_CHANNEL')
client = discord.Client()

manager = ToDoManager()
GENERAL_CHANNEL = {}

logging.basicConfig(filename=os.getenv('LOGGING_FILE'), encoding='utf-8', level=logging.DEBUG)
json_manager.FILE_NAME = os.getenv('SAVE_FILE')

async def send(msg):
    await GENERAL_CHANNEL.send(msg)

@client.event
async def on_ready():
    global GENERAL_CHANNEL
    global data
    GENERAL_CHANNEL = client.get_channel(int(CHANNEL))
    try:
        data = json_manager.read_json()
    except FileNotFoundError:
        logging.info(f'couldn\'t read file: {json_manager.FILE_NAME}')
    await send('I have connected!')

@client.event
async def on_message(message):
    global manager
    global data
    if message.author == client.user or message.content[0] != '~':
        return
    
    commands = list(message.content[1:].split(' '))
    command = commands[0]

    try:
        await send(MANAGER_COMMANDS[command](manager, commands))
    except:
        logging.error(' '.join(traceback.format_exception(*sys.exc_info())))
        await send(f'command not recognized: {command}')

client.run(TOKEN)