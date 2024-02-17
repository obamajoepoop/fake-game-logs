import discord
import asyncio
import random
import aiohttp
import uuid

# add webhook in quotes
WEBHOOK_URL = "WEBHOOK HERE"

# replace the fucking links retard
embeds = {
    "so crying rn": "https://tr.rbxcdn.com/df9e15201bd43d7923c14a9ef9e45aee/768/432/Image/Png", 
    "Teamwork Puzzles Obby": "https://tr.rbxcdn.com/124b8f15b3fe6ec19a5d341780432147/768/432/Image/Png",
    "[17th Floor] Guess The Logo!": "https://tr.rbxcdn.com/dd58535c90e1eee7b59f902bcf06e13f/768/432/Image/Png",
    "Sonic.EXE: The Disaster": "https://tr.rbxcdn.com/9078f190ddc213b67ec305b28acfd2b1/768/432/Image/Png",
    "Fling Things and People": "https://tr.rbxcdn.com/fcf9eeb8d3e87f7150587c752d3a7982/768/432/Image/Png",
    "Realistic Hand RP 🖐🤏 Without VR": "https://tr.rbxcdn.com/d8e2623b3c69419466db1a75b8ab886b/768/432/Image/Png",
    "MIC UP 🔊": "https://tr.rbxcdn.com/3eec5d043164892b758edd816117e55e/768/432/Image/Png",
    "LifeTogether 🏠 RP [UPD15]": "https://tr.rbxcdn.com/185ec6dcac0a9937bc2a3469aa3bea7f/768/432/Image/Png",
    "Berry Avenue 🏠 RP": "https://tr.rbxcdn.com/1e9a1b7e91d643b113e61fcbea91f475/768/432/Image/Png",
    "[EGG BOIZ] Verbalase 50K Chase": "https://tr.rbxcdn.com/9138e61a4eaac0b2b1326a19aa4069ac/768/432/Image/Png",
    "Murderers vs Sheriffs 2": "https://tr.rbxcdn.com/a54bd06248095712a08e399c29161842/768/432/Image/Png",
    "Guess the easy logo! [NEW]": "https://tr.rbxcdn.com/ac40a035795fd345e10b9acef1b9141b/768/432/Image/Png"
}

# values here for visits n shit 
def create_random_embed():
    name = random.choice(list(embeds.keys()))
    url = embeds[name]

    embed = discord.Embed(title=name, color=discord.Color.random())
    embed.set_image(url=url)
    embed.add_field(name="Visits", value=f"`{random.randint(1000000, 45000000):,}`", inline=True)
    embed.add_field(name="Players Active", value=f"`{random.randint(800, 1499):,}`", inline=True)
    embed.add_field(name="Server Size", value=f"`{random.randint(10, 100):,}`", inline=True)
    embed.add_field(name="Favorites", value=f"`{random.randint(4000, 12000):,}`", inline=True)
    embed.add_field(name="Likes", value=f"`{random.randint(12000, 90000):,}`", inline=True)
    embed.add_field(name="Dislikes", value=f"`{random.randint(12000, 90000):,}`", inline=True)
    embed.add_field(name="Job ID", value=f"`{str(uuid.uuid4())}`", inline=True)

    return embed


async def send_embed(webhook_url, embed):
    async with aiohttp.ClientSession() as session:
        async with session.post(webhook_url, json={"embeds": [embed.to_dict()]}):
            pass


async def send_embeds():
    while True:
        embed = create_random_embed()
        await send_embed(WEBHOOK_URL, embed)
        await asyncio.sleep(5)  # Adjust timing here

# Run the bot
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_embeds())
