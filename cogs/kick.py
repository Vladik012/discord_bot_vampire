import discord
from discord.ext import commands
from asyncio import sleep

class User(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print('kick is connected')
	@commands.command( pass_context = True )
	@commands.has_permissions( kick_members=True )

	async def kick( self, ctx, member: discord.Member, *, reason ):
		await ctx.channel.purge( limit = 1 )
		channel = self.bot.get_channel(978523327083728896)
		await channel.send(f'Был кикнут пользователь **{member.mention}** \n На сервере **{ctx.guild.name}** \n По причине: **{reason}**  ')


		await member.kick( reason = reason )
		await ctx.send(f'Был кикнут { member.mention }! По причине: {reason}' )

	#errors
	@kick.error
	async def kick_error( self, ctx, error ):
		if isinstance( error, commands.MissingRequiredArgument ):
			await ctx.send( f'{ctx.author.name} пожалуйста укажите учасника которого нужно кикнуть!' )
		if isinstance( error, commands.MissingPermissions ):
			await ctx.send( f'{ctx.author.name} вы не можете использовать данную команду' )


def setup(client):
	client.add_cog(User(client))