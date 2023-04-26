import discord
import random
from data import ValorantCharacter
from data import MessageStore
import waifu 
import chatgpt
from dotenv import load_dotenv
import os

load_dotenv()


def run_discord_bot():
    TOKEN = os.getenv("TOKEN")
    intents = discord.Intents.default()
    intents.members = True
    intents.presences = True
    intents.guild_messages = True
    intents.message_content = True

    client = discord.Client(intents=intents)
    members = []
    member_list2 = []
    filename = "theboys.txt"
    store = MessageStore(filename)
    vcmembers = []

    
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        guild = client.guilds[0]
        member_list = guild.members

        # store the members in an array
        for member in member_list:
            members.append(member.name)
            member_list2.append(member)

    @client.event
    async def on_voice_state_update(member, before, after):
        # Check if the user has joined a voice channel
        if before.channel is None and after.channel is not None:
            # Get the list of members in the voice channel
            vcmembers = after.channel.members

    @client.event
    async def on_message(message):
        # Make sure bot doesn't get stuck in an infinite loop
        if message.author == client.user:
            return

        # Get data about the user
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel) 

        if channel == 'waifu':
            response = waifu.send_message(user_message)
            await message.channel.send(response)
        elif channel == 'chatgpt':
            response = chatgpt.send_message(user_message)
            await message.channel.send(response)
        else:
            if message.content.startswith('!roulette'):
                index = random.randrange(0,len(members)-1)
                channel = message.channel
                await channel.send(responses.remove_hash(members[index]))
                new_nick = f"{message.content[6:]}"
                await member_list2[index].edit(nick=new_nick)
            elif user_message == '!roll':
                random_character = random.choice(list(ValorantCharacter))
                await message.channel.send(f'Slave: {random_character.value}')
            elif message.content.startswith('!write'):
                # Write the message content to the file
                store.add_message(f"{message.content[6:]}\n")
                print('name added')
            elif message.content.startswith('!fetch'):
                pass

    

    # Remember to run your bot with your personal TOKEN
    client.run(TOKEN)