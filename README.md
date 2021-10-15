# ETH_GASBOT
Discord bot written in python to display current gas values and estimated wait times for Ethereum transactions. Values are pulled from the ethgasstation API.

Example
!gas

Slow: 102.0 gewi expected in: 16.5 minutes.

Fast: 146.0 gwei expected in: 0.4 minutes.   

Fastest: 150.0 gwei expected in: 0.4 minutes.

Average: 111.0 gwei expected in: 1.7 minutes.


Installation and execution
1. Create a .env file in the same directory as gas.py and fill in with your values. You'll need the Discord bot token and the API key for ethgasstation.
2. DISCORD_TOKEN=YOUR_TOKEN_HERE
   
   ETH_GAS_KEY=YOUR_KEY_HERE
3. Run gas.py (may need to install dependencies based on your setup)
4. In Discord type "!gas" and the bot will display the current gas prices.

That's it.
