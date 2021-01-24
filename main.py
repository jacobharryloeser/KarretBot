import discord
import logging


class KarretClient(discord.Client):
    async def on_ready(self):
        logger.info('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        logger.info('Message from {0.author}: {0.content}'.format(message))
        channel = message.channel
        logger.debug('BRAKOLI User is {0} and author is {1}'.format(self.user, message.author))
        if (message.author != self.user):
            await channel.send('I only say lovely things')
            await channel.send('Eat Eggs')

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = KarretClient()
client.run('no-peeking')
