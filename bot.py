import discord
import requests
import os

from modules import iex_module

class MyClient(discord.Client):
    iexKey = os.environ['IEX_KEY']

    async def on_ready(self):
        print('Logged in as ', self.user)

    async def on_message(self, message):
        # Skip messages that we sent
        if message.author == self.user:
            return
        
        if message.content == 'StockBotPing':
            await message.channel.send('Bot is active')

        if message.content == "StockBotHelp":
            await message.channel.send('Hello! I am Jimmy\'s stock bot! I response to messages like $msft')
        
        if message.content.startswith('$'):
            symbol = message.content.replace('$','')
            # We only want to react to symbols - other things should be ignored
            if symbol.isalpha():
                response = iex_module.get_quote(symbol, self.iexKey)
                await message.channel.send(embed=response)
            else:
                await message.channel.send('Error processing stock symbol.')
print ('starting')
bot = MyClient()
bot.run(os.environ['DISCORD_KEY'])