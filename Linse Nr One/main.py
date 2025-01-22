from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message, File

# .env und so
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# Set up
intents: Intents = Intents.default()
intents.message_content = True 
client: Client = Client(intents=intents)


async def send_message(message: Message, user_message: str) -> None:
    try:
        if "bild" in user_message.lower():
            await message.channel.send(file=File('Käse.png'))
        else:
            response = "Hallo"
            await message.channel.send(response)
    except Exception as e:
        print(e)

#start bot
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running')

# zuschauer
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return  # Ignore messages from the bot itself
    
    user_message = message.content
    print(f'[{message.channel}] {message.author}: "{user_message}"')
    await send_message(message, user_message)


def main() -> None:
    client.run(TOKEN)

if __name__ == '__main__':
    main()
