import os
import discord

class Client(discord.Client):
    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.type == discord.MessageType.thread_created:
            await message.channel.send(f"<@{message.author.id}> started a thread: <#{message.id}> (<https://discord.com/channels/{message.guild.id}/{message.channel.id}/threads/{message.id}>)", allowed_mentions=discord.AllowedMentions.none())
            await message.delete()

def main():
    intents = discord.Intents.default()
    intents.message_content = True
    client = Client(intents=intents)
    client.run(os.environ["DISCORD_TOKEN"])

if __name__ == "__main__":
    main()
