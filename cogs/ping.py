import discord
from discord.ext import commands
from asyncio import sleep

class User(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print('ping is connected')

	@commands.command()
	async def ping(self, ctx):

		await ctx.send(f'**🏓Понг:  {self.bot.ws.latency * 1000:.0f}**')


def setup(client):
	client.add_cog(User(client))