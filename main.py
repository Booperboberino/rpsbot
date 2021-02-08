import constants
import discord

token = constants.token
prefix = "."
client = discord.Client()

print("Working!")


async def doRPSCheck(content, channel, user,):
    for a in content.split():
        if a[0] == "<":
            await channel.send("Confirm, you want to rps with " + a + "? Reply with `y` to confirm.")
            global waitingForResponse
            waitingForResponse = {}
            waitingForResponse[user] = a
        else:
            print("")


async def doRPS(channel, challenger, challengee):
    await channel.send("Confirm, you want to rps with " + a + "? Reply with `y` to confirm.")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('.honk'):
        await message.channel.send("honk")

    if message.content.startswith(".rps"):
        await doRPSCheck(message.content, message.channel, message.author)
    
    if message.content.startswith("y") and message.author in waitingForResponse.keys:
        await doRPS(message.channel)

    if message.content.startswith(".test"):
        print ("test")


client.run(token)