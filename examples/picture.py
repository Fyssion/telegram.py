import pygram
import logging

logging.basicConfig(level=logging.INFO, format="(%(asctime)s) %(levelname)s %(message)s", datefmt="%m/%d/%y - %H:%M:%S %Z")
logger = logging.getLogger("pygram")

# Make sure never to share your token
bot = pygram.Bot("token here")

# Create and register a command called "image".
# Note that you can specify the command name
# in the command decorator.
@bot.command(name="image")
async def image_command(ctx):
    # Make the bot start typing
    await ctx.send_action("typing")

    # Open an image...
    with open("file path here", "rb") as f:
        # ...convert it to a sendable photo...
        photo = pygram.Photo(file=f, caption="This is a photo")

    # ...and upload/send it.
    await ctx.send(file=photo)

bot.run()
