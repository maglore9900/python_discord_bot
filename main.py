import discord
import environ

# Replace 'YOUR_BOT_TOKEN' with the bot token you copied from the Developer Portal

env = environ.Env()
environ.Env.read_env()
TOKEN = env('DISCORD_TOKEN')

# Initialize the client (your bot)
intents = discord.Intents.default()

client = discord.Client(intents=intents)

# Define a command prefix, for example, '!'
command_prefix = '!'

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    
@client.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    # Check if the bot is mentioned in the message
    if client.user in message.mentions:
        # Extract the message (assuming it follows the mention)
        received_message = message.content.replace(f'<@{client.user.id}>', '').strip()

        # Execute command on the server
        try:
            output = f"Here is your command {received_message}"
            # result = subprocess.run(command, shell=True, capture_output=True, text=True)
            # output = result.stdout if result.returncode == 0 else result.stderr
        except Exception as e:
            output = f"Error: {e}"

        # Send the output back to Discord
        await message.channel.send(f'```\n{output}\n```')

client.run(TOKEN)