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
	async def bug(self, ctx, *, reason):
		channel = self.bot.get_channel(988903598786240592)
		await channel.send(f'{reason} \n отправил {ctx.message.author}')
		#await ctx.message.delete() #delay = 10
		await ctx.send('Вы успешно отправили баг')
		await ctx.message.delete(delay = 10)


	@commands.command()
	async def idea(self, ctx, *, reason):
		id = str(ctx.guild.id)
		if id == '978007902742790154':
			channel = self.bot.get_channel(989030529036861520)
			await channel.send(f'{reason}\n отправил {ctx.author.mention}')
			await ctx.message.delete()
			await ctx.send('Вы успешно отправили идею')
			await ctx.message.delete(delay=10)
		else:
			pass

	@bug.error
	async def bug_error( self, ctx, error ):
		if isinstance( error, commands.MissingRequiredArgument ):
			await ctx.send( f'{ctx.author.name} пожалуйста укажите баг' )
		if isinstance( error, commands.MissingPermissions ):
			await ctx.send( f'{ctx.author.name} вы не можете использовать данную команду' )



	
	


def setup(client):
	client.add_cog(User(client))
