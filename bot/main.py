import discord
from discord.ext import commands
import random
OriginalListofPetNames = ["pookiebear", "malewife", "prince charming", "sweetiepie", "sugarplum", "babygirl", "babyboy"]

FormattedRandomPetNames = (random.choices(OriginalListofPetNames, k=10))
print(*FormattedRandomPetNames, sep = ", ")

# Replace 'YOUR_TOKEN' with your Discord bot token
TOKEN = 'MTE1OTM5NzMyMzg2OTI3MDAxNw.GmDg8h.19kkhhXWvdsXKgx9cyJAPmUdC7wxvsaJhsYwNU'

# Define your intents
intents = discord.Intents.default()
intents.message_content = True  # Enable the message content intent

# Create an instance of the bot with the defined intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Define your keyword-reaction dictionary
keyword_reactions = {
    'kys': 'dont kys bbg 🥺🥺🥺🥺',
    'winter': '... winter?? like... **winter wonder world**',
    'gay': '## DON\'T MENTION THOSE THINGS HERE',
    'meow': 'meowww',
}


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    await bot.change_presence(activity=discord.Game(name='on the tailsland grind'))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  # Ignore messages sent by the bot itself
    
    if bot.user in message.mentions:
        FormattedRandomPetNames = random.choices(OriginalListofPetNames, k=10)
        SepFormattedRandomPetnames = ', '.join(FormattedRandomPetNames)
        print(SepFormattedRandomPetnames)  # Print the formatted pet names
        
        # Remove bot's mention from message content
        mentioned_users = message.mentions
        message_content_without_mention = message.content
        for user in mentioned_users:
            message_content_without_mention = message_content_without_mention.replace(user.mention, "")
        
        response = f"{message_content_without_mention.strip()}, my {SepFormattedRandomPetnames}!"
        await message.channel.send(response)
    

    for keyword, reaction in keyword_reactions.items():
        if keyword in message.content.lower():
            # Send the corresponding reaction when a keyword is detected
            await message.channel.send(reaction)

    await bot.process_commands(message)

@bot.event
async def on_voice_state_update(member, before, after):
# Check if the user joined an empty voice channel
    if after.channel is not None and len(after.channel.members) == 1:
        channel_to_update = bot.get_channel("954730195053584434")
        if channel_to_update:
            message = f"{member.display_name} joined an empty voice channel: {after.channel.name}."
            await channel_to_update.send(message)

bot.run(TOKEN)
