import nextcord, json
from nextcord.ext import commands

class myBot(commands.Bot):
    def __init__(self):
        with open("botconfig/config.json") as cf:
            self.config = json.load(cf)
        with open("botconfig/token.0") as tf:
            self.bot_token = tf.read()
        super().__init__(
            command_prefix = self.config['prefix'],
            description = self.config['description']
        )
    
    async def on_ready(self):
        print(f"{self.user.name} is klaar om door kleine kinderen gespamt te worden!")
    
bot = myBot()

@bot.command()
async def ping(ctx):
    await ctx.reply("Pong!")

bot.run(bot.bot_token)