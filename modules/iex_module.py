import requests
import discord
import os
import uuid

def get_quote(symbol, iex_key):
    print('Received request for ' + symbol)
    embed = discord.Embed()

    url = 'https://cloud.iexapis.com/stable/stock/' + symbol + '/quote?token=' + iex_key

    response = requests.get(url)

    if response.status_code != 200:
        error_tracking = uuid.uuid4()
        print('[' + str(error_tracking) + '] HTTP Error ' + str(response.status_code) + ' message: ' + str(response.content))
        embed.add_field(name="IEX HTTP Error", value=str(response.status_code))
        embed.add_field(name="Tracking Number", value=str(error_tracking))
        return embed
    
    response = response.json()

    if float(response['change']) >= 0:
        embed.colour = 0x007213
        indicator = '+'
    else:
        embed.colour = 0xAB1212
        indicator = "-"

    embed.add_field(name=symbol.upper(), value=response["companyName"], inline=True)
    embed.add_field(name="Price", value="${:.2f}".format(response["latestPrice"]), inline=False)
    embed.add_field(name="Change", value=indicator + "{:.2f} | ({:.2f}%)".format(float(response["change"].__abs__()), response["changePercent"] * 100), inline=True)

    return embed



