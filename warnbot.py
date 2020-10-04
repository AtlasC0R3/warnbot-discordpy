import asyncio
import sys

# Imports discord.py
try:
    import discord
except ImportError:
    sys.exit("Discord.py has not been installed, or at least I failed to load it. This Python app requires it. Please install it using:\n  pip install discord.py\n")

from discord.ext.commands import Bot
from discord.ext import commands

cogs = ['cogs.warn']

def get_prefix(client, message):

    prefixes = ['?']    # sets the prefixes, you can keep it as an array of only 1 item if you need only one prefix

    if not message.guild:
        prefixes = ['']   # Only allow '+' as a prefix when in DMs, this is optional

    # Allow users to @mention the bot instead of using a prefix when using a command. Also optional
    # Do `return prefixes` if you don't want to allow mentions instead of prefix.
    return commands.when_mentioned_or(*prefixes)(client, message)

    # Special thanks to user EvieePy on GitHub for this snippet of code! https://gist.github.com/EvieePy/

print_messages = True
# Decides whether or not the bot shall print every message to the command prompt.
# False means that it will not print any of the user messages to the terminal
# True means that it will (at the expense of your user members' privacy, from a certain point of view).

bot = commands.Bot(                                                                                                       # Create a new bot
    command_prefix=get_prefix,                                                                                            # Set the prefix
    description='AtlasC0R3\'s Warn-bot, written in Discord.py (https://github.com/AtlasC0R3/warnbot-discordpy/)',         # Set a description for the bot
    case_insensitive=True                                                                                                 # Make the commands case insensitive
)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

@bot.event
async def on_ready():
    print('My name is {0.user}.\n'.format(bot))
    # Prints out the bot's name.
    for cog in cogs:
        bot.load_extension(cog)
        # Loads every cog provided.
    return

@bot.listen()
async def on_message(message):
    global print_messages
    if print_messages:
        if message.content == (""):
            print(f'{bcolors.OKBLUE}{message.author}{bcolors.ENDC} {bcolors.OKGREEN}(#{message.channel}, {message.channel.id} in {message.guild}){bcolors.ENDC}: (no comments included)')
            if not message.attachments == "[]":
                print(message.attachments)
        else:
            print(f'{bcolors.OKBLUE}{message.author}{bcolors.ENDC} {bcolors.OKGREEN}(#{message.channel}, {message.channel.id} in {message.guild}){bcolors.ENDC}:\n{message.content}')
            if message.attachments:
                print(message.attachments)


bot.run(open("data/token.txt", "rt").read(), bot=True, reconnect=True)
# Reads the token from an external file. The bot argument is to determine whether or not the token provided is for a bot or for a user.
# The reconnect argument is for whether or not you want your bot to reconnect if it does disconnect at some time.
