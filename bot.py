import discord
import responses


# Send messages
async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'MTEyMzA1OTMxMjMwNzIyNDY2Ng.Gn1Y3s.Iaj1u1QFdUxy4z6bIsmb9aFHfTjf1Nsfp4E3aI'
    client = discord.Client(intents=discord.Intents.all())
    

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')



    @client.event
    async def on_message(message):
        # Make sure bot doesn't get stuck in an infinite loop
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        # Debug printing
        print(f"{username} said: '{user_message}' ({channel})")

        # If the user message contains a '?' in front of the text, it becomes a private message
        if user_message[0] == '?':
            user_message = user_message[1:]  # [1:] Removes the '?'
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    # Remember to run your bot with your personal TOKEN
    client.run(TOKEN)