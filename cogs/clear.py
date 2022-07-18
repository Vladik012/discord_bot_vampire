import discord
from discord.ext import commands
from asyncio import sleep

class User(commands.Cog):
	def __init__(self, bot):
		self.bot = bot





	@commands.Cog.listener()
	async def on_ready(self):
		print('clear is connected')

	

	

	@commands.command( pass_context = True )
	@commands.has_permissions(manage_messages=True)
	
	async def clear( self, ctx, amount : int ):
		await ctx.channel.purge( limit = amount+1 )

		await ctx.send(embed = discord.Embed(description = f':white_check_mark: Удалено {amount} сообщений', color = 0x0c0c0c))





	#error
	@clear.error
	async def clear_error( self, ctx, error ):
		if isinstance( error, commands.MissingRequiredArgument ):
			await ctx.send( f'{ctx.author.name} пожалуйста укажите количество очищаемых сообщений!' )
		if isinstance( error, commands.MissingPermissions ):
			await ctx.send( f'{ctx.author.name} вы не можете использовать данную команду' )


def setup(client):
	client.add_cog(User(client))