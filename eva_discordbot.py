import discord
import random
import configparser

client = discord.Client(intents=discord.Intents.default())
config = configparser.ConfigParser()
config.read('config.ini')

bot_token = config.get('discord', 'bot_token')

@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_message(message):
    # Check if the message was sent by the bot itself.
    if message.author.bot:
        return

    # Get the command and arguments from the message.
    parts = message.content.split()
    command = parts[1]
    args = parts[1:]

    # Check if the command is a known command.
    if command in commands:
        # Run the command.
        await commands[command](message, args)
    else:
        # The command is not known, so respond with an error message.
        await message.reply("Hi! I'm Eva. Sorry, I don't know that command. Type help to view all commands.")  # noqa: E501

# A function that responds to the "ping" command.
async def hello(message, args):
    await message.reply("Hi! I'm Eva.")

# A function that responds to the "ping" command.
async def ping(message, args):
    await message.reply("Pong!")

# A function that responds to the "help" command.
async def help(message, args):
    command_list = "\n".join(commands.keys())
    reply_message = f"Here is a list of commands:\n{command_list}"
    await message.reply(reply_message)

# A function that responds to the "roll" command.
async def roll(message, args):
    if not args:
        await message.reply("Please provide the number of sides for the dice.")
        return

    # Get the number of sides from the message.
    try:
        sides = int(args[1])
    except ValueError:
        await message.reply("Invalid number of sides. Please provide a valid integer.")
        return

    # Roll the die.
    result = random.randint(1, sides)

    # Respond with the result.
    await message.reply(f"You rolled a {result}.")

# A dictionary of commands.
commands = {
    "hello": hello,
    "ping": ping,
    "help": help,
    "roll": roll,
}

client.run(bot_token)
