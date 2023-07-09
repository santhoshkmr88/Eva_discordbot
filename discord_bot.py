import os
import discord
from discord.ext import commands
import configparser
import bot_commands 

# Get the absolute path of the script file
script_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(script_dir, 'config.ini')
config = configparser.ConfigParser()
config.read(config_path)
bot_token = config.get('discord', 'bot_token')

intents=discord.Intents.default()
intents.message_content = True
client=commands.Bot(command_prefix = '!', intents=intents)

@client.event
async def on_ready():
    print("Bot is ready!")

@client.command()
async def eva(ctx, *, arg):
    # Convert all args to lower case
    args = arg.lower()

    try:
        for command_prefix, command_func in bot_commands.commands.items():
            if args.startswith(command_prefix):
                # Extract the arguments after the prefix
                command_args = args[len(command_prefix):].strip()
                # Execute the command function with the arguments
                response = bot_commands.commands[command_prefix](command_args)
                await ctx.send(response)
                return
    except KeyError:
        await ctx.send("An error occurred while executing the command.")


client.run(bot_token)
