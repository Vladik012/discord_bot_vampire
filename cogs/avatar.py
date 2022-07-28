import discord
from discord.ext import commands

class User(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print('test is connected')


	@commands.command()
	async def avatar(self, ctx, member: discord.Member = None):
		await ctx.send(member.avatar_url)
	
	@avatar.error
	async def avatar_error(self, ctx, error):
		if isinstance( error, commands.CommandInvokeError ):
			await ctx.send(f'{ctx.author.name} укажить чью аватарку вы хотите посмотреть')




def setup(client):
	client.add_cog(User(client))