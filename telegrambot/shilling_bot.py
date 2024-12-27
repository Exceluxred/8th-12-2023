# # # from telethon import TelegramClient, events
# # # import re

# # # # Replace with your own API ID and API Hash
# # # api_id = '23841507'
# # # api_hash = '541a69b3329264ba3cbe1f94e75b7e52'
# # # phone_number = '+2347084441982'  # Replace with your actual phone number

# # # # Create a client
# # # client = TelegramClient('session_name', api_id, api_hash)

# # # # Define the chat IDs you want to monitor
# # # monitored_chats = [
# # #      -1001942325191
# # # ]

# # # async def main():
# # #     await client.start(phone_number)
    
# # #     @client.on(events.NewMessage(chats=monitored_chats))
# # #     async def handler(event):
# # #         text = event.message.message
# # #         # Extract only Telegram links
# # #         links = re.findall(r'https://', text)
# # #         for link in links:
# # #             print(f"New Telegram link found: {link}")

# # # with client:
# # #     client.loop.run_until_complete(main())


# # import matplotlib.pyplot as plt
# # import matplotlib.dates as mdates
# # from datetime import datetime

# # # Data for the timeline
# # timestamps = [
# #     "11/01/2024 09:45", "11/01/2024 09:46", "11/01/2024 10:05", 
# #     "11/01/2024 10:07", "11/01/2024 10:15", "11/01/2024 10:30", 
# #     "11/01/2024 10:50", "11/01/2024 11:10", "11/01/2024 11:30", "11/01/2024 12:00"
# # ]

# # events = [
# #     "HTTP GET request initiated", 
# #     "File flagged by Snort", 
# #     "Communication with C2 server begins", 
# #     "SSL/TLS sessions initiated with Dridex C2 servers", 
# #     "Continued communication with C2 servers", 
# #     "Snort alerts on Dridex malware", 
# #     "Remcos RAT check-ins observed", 
# #     "Outgoing connections with SSL encryption", 
# #     "Data exfiltration suspected", 
# #     "Intermittent communications, possible completion of attack"
# # ]

# # # Convert timestamps to datetime objects
# # dates = [datetime.strptime(ts, "%d/%m/%Y %H:%M") for ts in timestamps]

# # # Create the figure and axis
# # fig, ax = plt.subplots(figsize=(10, 6))

# # # Plot the events on the timeline
# # ax.scatter(dates, [1]*len(dates), color='blue', zorder=5)

# # # Draw the timeline line
# # ax.plot(dates, [1]*len(dates), color='gray', linewidth=2, zorder=1)

# # # Label the events on the timeline
# # for i, (date, event) in enumerate(zip(dates, events)):
# #     ax.text(date, 1.02, event, rotation=45, ha='right', fontsize=9)

# # # Formatting the timeline
# # ax.get_yaxis().set_visible(False)
# # ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))
# # ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

# # # Set titles and labels
# # plt.title("Timeline of Events - 11/01/2024", fontsize=14)
# # plt.xlabel("Time", fontsize=12)

# # plt.xticks(rotation=45)
# # plt.tight_layout()

# # # Show the plot
# # plt.show()
# # Re-attempting to plot the timeline without file save

# import matplotlib.pyplot as plt
# import matplotlib.dates as mdates
# from datetime import datetime

# # Data for the timeline
# timestamps = [
#     "11/01/2024 09:45", "11/01/2024 09:46", "11/01/2024 10:05", 
#     "11/01/2024 10:07", "11/01/2024 10:15", "11/01/2024 10:30", 
#     "11/01/2024 10:50", "11/01/2024 11:10", "11/01/2024 11:30", "11/01/2024 12:00"
# ]

# events = [
#     "HTTP GET request initiated", 
#     "File flagged by Snort", 
#     "Communication with C2 server begins", 
#     "SSL/TLS sessions initiated with Dridex C2 servers", 
#     "Continued communication with C2 servers", 
#     "Snort alerts on Dridex malware", 
#     "Remcos RAT check-ins observed", 
#     "Outgoing connections with SSL encryption", 
#     "Data exfiltration suspected", 
#     "Intermittent communications, possible completion of attack"
# ]

# # Convert timestamps to datetime objects
# dates = [datetime.strptime(ts, "%d/%m/%Y %H:%M") for ts in timestamps]

# # Create the figure and axis
# fig, ax = plt.subplots(figsize=(10, 6))

# # Plot the events on the timeline
# ax.scatter(dates, [1]*len(dates), color='blue', zorder=5)

# # Draw the timeline line
# ax.plot(dates, [1]*len(dates), color='gray', linewidth=2, zorder=1)

# # Label the events on the timeline
# for i, (date, event) in enumerate(zip(dates, events)):
#     ax.text(date, 1.02, event, rotation=45, ha='right', fontsize=9)

# # Formatting the timeline
# ax.get_yaxis().set_visible(False)
# ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

# # Set titles and labels
# plt.title("Timeline of Events - 11/01/2024", fontsize=14)
# plt.xlabel("Time", fontsize=12)

# plt.xticks(rotation=45)
# plt.tight_layout()

# # Show the plot
# plt.show()
import pandas as pd

# Load the CSV file to examine its structure and prepare it for a timeline representation in Excel
file_path = '/mnt/data/packet for time stamp.csv'
packet_data = pd.read_csv(file_path)

# Display the first few rows to understand the data structure
packet_data.head()