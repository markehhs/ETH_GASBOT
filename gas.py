# gas.py
import os
import requests
import json
import discord
from dotenv import load_dotenv

try:    
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    ETHAPIKEY = os.getenv('ETH_GAS_KEY')
except Exception as e:
    print("Setup error. Make sure your .env file is setup correctly. Checkout the readme for more help.\n" + e)

##discord part...

def main():
    client = discord.Client()

    @client.event
    async def on_message(message):
        if message.author == client.user:
            ##dont want the bot to pickup its own messages
            return

        ##check if the msg == !gas
        if message.content == "!gas":
            ##this is our trigger to display the gas
            response = getGasPrices()
            await message.channel.send(response)

    client.run(TOKEN)


def getGasPrices():
    baseURL = "https://ethgasstation.info/api/ethgasAPI.json?api-key="
    fullURL = baseURL + ETHAPIKEY

    headers = {"Accept": "application/json"}

    response = requests.request("GET", fullURL, headers=headers)

    json_object = json.loads(response.text)

    json_formatted_str = json.dumps(json_object, indent=2)
    ##################################################### parse the gwei values from the json
    fast = float(json_object["fast"]) / 10 ## < 2 mins
    fastest = float(json_object["fastest"]) / 10 ## < 30 seconds
    slow = float(json_object["safeLow"]) / 10 ## 30 mins
    average = float(json_object["average"]) / 10 ## 5 mins
    ##################################################### parse the gwei times from the json
    fastTime = float(json_object["fastWait"])
    fastestTime = float(json_object["fastestWait"])
    slowTime = float(json_object["safeLowWait"])
    averageTime = float(json_object["avgWait"])
    ##################################################### display all values
    print("Slow: " + str(slow) + " gewi expected in: " + str(slowTime) + " minutes.")
    print("Fast: " + str(fast) + " gwei expected in: " + str(fastTime) + " minutes.")
    print("Fastest: " + str(fastest) + " gwei expected in: " + str(fastestTime) + " minutes.")
    print("Average: " + str(average) + " gwei expected in: " + str(averageTime) + " minutes.")
    ##################################################### put all values into 1 string and return the string
    returnStr = "**Slow:** " + str(slow) + " gwei expected in: " + str(slowTime) + " minutes.\n**Fast:** " + str(fast) + " gwei expected in: " + str(fastTime) + " minutes.\n**Fastest:** " + str(fastest) + " gwei expected in: " + str(fastestTime) + " minutes.\n**Average:** " + str(average) + " gwei expected in: " + str(averageTime) + " minutes."
    return returnStr

main()