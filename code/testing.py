import instances, ai, discord
from discord.ext import commands

token = str(open("C:/Users/kazen/Desktop/kazenoko/fishlang/kaz-ai/source/data/token.txt", "r").read())
name = input("NAME: ")
time_lim = input("TIME LIMIT: ")
embed = ""
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="kai ")
AI = ai.AI(username=name, model=1)

@bot.event
async def on_ready():
    print("LOGGED IN AS {0.user}".format(bot))
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(f"Talking to {name}"))

@bot.event
async def on_message(msg):
    global embed
    if msg.author == bot.user:
        pass
    elif str(msg.author).lower() != name:
        embed = discord.Embed(title=f"Chat with {AI.getModel()}", description=f"Only {name} can talk with the user.", colour=discord.Colour.teal(), type='rich')
    else:
        async with msg.channel.typing():
            username = str(msg.author)
            user_message = str(msg.content)
            channel = str(msg.channel)
            print(f"username: {username}\nmessage: {user_message}\nchannel: {channel}")
            ans = AI.ask(prompt=user_message)
            embed = discord.Embed(title=f"Chat with {AI.getModel()}", description=ans,
                                  colour=discord.Colour.teal())
            embed.set_footer(text=f"This chat has a {time_lim} time limit.")
            await msg.channel.send(embed=embed)

bot.run(token=token)