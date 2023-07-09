import random

# A function that responds to the "ping" command.
def hello(command_args):
    return("Hi! I'm Eva.")

# A function that responds to the "ping" command.
def ping(command_args):
    return("Pong!")

# A function that responds to the "help" command.
def help(command_args):
    command_list = "\n".join(commands.keys())
    reply_message = f"Here is a list of commands:\n{command_list}"
    return(reply_message)

# A function that responds with random int to the "roll" command.
def roll(command_args):
    if not command_args:
        return("Please provide the number of sides for the dice.")

    # Get the number of sides from the message.
    try:
        sides = int(command_args)
    except ValueError:
        return("Invalid number of sides. Please provide a valid integer.")

    # Roll the die.
    result = random.randint(1, sides)

    # Respond with the result.
    return(f"You rolled a {result}.")

commands = {
    "hello": hello,
    "ping": ping,
    "help": help,
    "roll": roll,
}

# Send 1 on 1 user messages
# async def send_message(message, user_message, is_private):
#     try:
#         response = bot_commands.help(message)
#         await message.author.send(response) if is_private else await message.channel.send(response)  # noqa: E501
#     except Exception as e:
#         print(e)
#     # If the user message contains '?' in front of the text, it becomes a private message  # noqa: E501
#     if message.content[0] == '?':
#         user_message = message.content[1:]  # [1:] Removes the '?'
#         await send_message(message, user_message, is_private=True)
#     else:
#         await send_message(message, user_message, is_private=False)