from telethon import TelegramClient, events

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
        # Print the raw message object
        print("Received message object:")
        print(event.message)
        
        # Print the message text
        text = event.message.message
        print("Message text:")
        print(text)
        
        # Print message metadata
        print("Message metadata:")
        print(f"Chat ID: {event.chat_id}")
        print(f"Sender ID: {event.message.sender_id}")
        print(f"Message ID: {event.message.id}")
        
        # Optional: Print message data in a formatted way
        print("Formatted message data:")
        print(f"Date: {event.message.date}")
        print(f"Message text: {text}")

with client:
    client.loop.run_until_complete(main())
