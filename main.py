import discord
import feedparser
import asyncio

# Parse the RSS feed
d = feedparser.parse('rss_url')

# Store the latest post
latest = d.entries[0]

# Create an instance of the discord client
client = discord.Client()

async def check_feed():
    global latest
    while True:
        # Parse the RSS feed
        d = feedparser.parse('rss_url')
        
        # Check if there is a new post
        if d.entries[0].updated_parsed > latest.updated_parsed:
            # Update the latest post
            latest = d.entries[0]
            
            # Get the desired channel
            channel = client.get_channel('channel_id')
            
            # Create the message
            msg = f"{latest.title}\n{latest.link}"
            
            # Send the message
            await channel.send(msg)
        
        # Wait before checking again
        await asyncio.sleep(60)  # 60 seconds

@client.event
async def on_ready():
    # Start checking the feed
    client.loop.create_task(check_feed())

# Run the bot
client.run('your_bot_token')
