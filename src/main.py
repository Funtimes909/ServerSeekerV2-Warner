from javascript import require, On
mineflayer = require('mineflayer')

bot = mineflayer.createBot({
  'host': 'mc.example.com',
  'port': 25565,
  'username': "ServerSeekerV2"
})

@On(bot, 'login')
def warn(*args):
    bot.chat('test')