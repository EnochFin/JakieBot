import os
import discord
import json

import json_manager
import util

from dotenv import load_dotenv

from todo import ToDo, Status, ToDoManager
from commands import Command

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

manager = ToDoManager()
GENERAL_CHANNEL = {}

async def send(msg):
    await GENERAL_CHANNEL.send(msg)

@client.event
async def on_ready():
    global GENERAL_CHANNEL
    global data
    print(f'{client.user} has connected to Discord!')
    GENERAL_CHANNEL = client.get_channel(838901558116352022)
    data = json_manager.read_json()
    await send('I have connected!')

@client.event
async def on_message(message):
    global manager
    global data
    if message.author == client.user or message.content[0] != '~':
        return
    
    commands = message.content[1:].split(' ')
    command = commands[0]

    if command == 'add':
        task_name = ' '.join(commands[1:])
        manager.items.append(ToDo(task_name))
        await send(f'added: {task_name}')
    elif command == 'list':
        result = '```\n'
        for item in manager.items:
            line = f'{item.status}| {item.title}\n'
            result += line
        await send(result + '```')
    elif command == 'save':
        json_manager.save_json(util.manager_to_json(manager))
        await send('saved the list!')
    else:
        await send(f'command not recognized: {command}')

client.run(TOKEN)