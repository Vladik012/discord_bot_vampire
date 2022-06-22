import discord
from discord.ext import commands
from asyncio import sleep


class User(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print('report info is connected')

	@commands.command()
	async def report(self, ctx, *, reason):
		channel = self.bot.get_channel(988903598786240592)
		await channel.send(f'{reason}')
		await ctx.message.delete() #delay = 10
		await ctx.send('Вы успешно отправили репорт')



	
	


def setup(client):
	client.add_cog(User(client))