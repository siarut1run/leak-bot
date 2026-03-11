import discord
from deep_translator import GoogleTranslator
import os

TOKEN = os.getenv("TOKEN")

SOURCE_CHANNEL_ID = 1481195903309316128
TARGET_CHANNEL_ID = 1481198820917248041

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.channel.id == SOURCE_CHANNEL_ID and not message.author.bot:
        translated = GoogleTranslator(source='en', target='ja').translate(message.content)
        target = client.get_channel(TARGET_CHANNEL_ID)
        files = [await a.to_file() for a in message.attachments]
        await target.send(f"🌐自動翻訳\n{translated}", files=files)

client.run(TOKEN)