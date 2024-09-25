from telethon import TelegramClient, events
import re

# Replace with your own API ID and API Hash
api_id = '23841507'
api_hash = '541a69b3329264ba3cbe1f94e75b7e52'
phone_number = '+2347084441982'  # Replace with your actual phone number

# Create a client
client = TelegramClient('session_name', api_id, api_hash)

# Define the chat IDs you want to monitor
monitored_chats = [
     -1001942325191
]

async def main():
    await client.start(phone_number)
    
    @client.on(events.NewMessage(chats=monitored_chats))
    async def handler(event):
        text = event.message.message
        # Extract only Telegram links
        links = re.findall(r'https://', text)
        for link in links:
            print(f"New Telegram link found: {link}")

with client:
    client.loop.run_until_complete(main())
