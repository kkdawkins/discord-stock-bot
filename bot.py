import discord
import requests
import os

class MyClient(discord.Client):
    iexKey = os.environ('IEX_KEY')
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
                url = 'https://cloud.iexapis.com/stable/stock/' + symbol + '/quote?token=iexKey'
                response = requests.get(url).json()
                answer = symbol + ' is trading at $' + str(response['iexRealtimePrice']) + ". "
                if (response['change'] >= 0):
                    answer = answer + 'It is up ' + str(response['changePercent'] * 100) + '% ($' + str(response['change']) + ').'
                else:
                    answer = answer + 'It is down ' + str(response['changePercent'] * 100) + '% ($' + str(response['change']) + ').'
                await message.channel.send(answer)
            else:
                await message.channel.send('Error processing stock symbol.')
print ('starting')
bot = MyClient()
bot.run(os.environ('DISCORD_KEY'))