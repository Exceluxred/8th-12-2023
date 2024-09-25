from telethon import TelegramClient, events
import re

# Replace with your own API ID and API Hash
api_id = '23841507'
api_hash = '541a69b3329264ba3cbe1f94e75b7e52'
phone_number = '+2347084441982'

# Create a client
client = TelegramClient('session_name', api_id, api_hash)

# Define the chat IDs you want to monitor
monitored_chats = [-1001942325191, -1002012097496]

async def main():
    await client.start(phone_number)
    
    @client.on(events.NewMessage(chats=monitored_chats))
    async def handler(event):
        text = event.message.message
        print(f"New message in chat {event.chat_id}: {text}")
        # Extract only Telegram links
        links = re.findall(r'https://t\.me/[^\s]+', text)
        if links:
            print(f"Extracted links: {links}")
        else:
            print("No links found in the message.")

with client:
    client.loop.run_until_complete(main())
