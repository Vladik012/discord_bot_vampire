from turtle import title
import discord
from discord.ext import commands
from asyncio import sleep

class User(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print('vote is connected')
    
	@commands.command()
	async def vote(self, ctx):

		server = 'https://top.gg/bot/768178624431652934?s=013d77ab51e13'
		embed = discord.Embed( title = 'Проголосовать за бота:',
				description = f"[top.gg]({server})",
			)
		await ctx.send(embed = embed)

	
	


def setup(client):
	client.add_cog(User(client))