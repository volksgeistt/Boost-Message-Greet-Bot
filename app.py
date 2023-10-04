import discord
from discord.ext import commands
import json

token = "ADD_YOUR_BOT_TOKEN"
prefix = "ADD_YOUR_BOT_PREFIX"

volks =  commands.Bot(command_prefix=prefix,intents=discord.Intents.all())

try:
    with open('boost_msg.json', 'r') as f:
        boost_msg = json.load(f)
except FileNotFoundError:
    boost_msg = {}

@volks.event
async def on_ready():
    print(f"Logged in as: {volks.user}")
    await volks.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"Boosters"))

######################### Copyrights @ Volksgeist #########################
"""
All Commands:

1. boostmsg enable -> enables boost message
2. boostmsg disable -> disables boost message

"""
@volks.event
async def on_message(message):
    await volks.process_commands(message)
    member = message.author
    if not message.guild:
        return
    if message.type == discord.MessageType.premium_guild_subscription and boost_msg.get(str(message.guild.id), False):
        await message.channel.send(f"🎉 Thanks For Boosting! {member.mention}")

@volks.group()
async def boostmsg(ctx):
    pass

@boostmsg.command(name="enable")
async def volksgeist_daddy_1(ctx):
    boost_msg[str(ctx.guild.id)] = True
    await ctx.send(f"✅ | Boost Greeting Has Been Enabled")
    with open('boost_msg.json', 'w') as f:
        json.dump(boost_msg, f)

@boostmsg.command(name="disable")
async def volksgeist_daddy_2(ctx):
    boost_msg[str(ctx.guild.id)] = False
    await ctx.send(f"✅ | Boost Greeting Has Been Disabled")
    with open('boost_msg.json', 'w') as f:
        json.dump(boost_msg, f)

volks.run(token)

