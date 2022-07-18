import discord
from discord.ext import commands
from asyncio import sleep

class User(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print('mute is connected')
	@commands.command()
	@commands.has_permissions(manage_messages=True)
	async def mute(self, ctx, member: discord.Member, time: int, *, reason ):
		mute_role = discord.utils.get(ctx.message.guild.roles, name = 'muted')

		await member.add_roles(mute_role)
		await ctx.send(f'Был кинут в мут пользователь {member.mention}, на время {time} м')
		await sleep(time * 60)
		await member.remove_roles(mute_role)

	@commands.command()
	@commands.has_permissions(manage_messages=True)
	async def mute_h(self, ctx, member: discord.Member, time: int, *, reason ):
		mute_role = discord.utils.get(ctx.message.guild.roles, name = 'muted')

		await member.add_roles(mute_role)
		await ctx.send(f'Был кинут в мут пользователь {member.mention}, на время {time} ч')
		await sleep(time * 360)
		await member.remove_roles(mute_role)

	@commands.command()
	@commands.has_permissions(manage_messages=True)
	async def unmute(self, ctx, member: discord.Member):
		mute_role = discord.utils.get(ctx.message.guild.roles, name = 'muted')
		await member.remove_roles(mute_role)

		await ctx.send(f'Был снят мут с пользователя **{member.mention}**')
		

	@mute.error
	async def mute( self, ctx, error ):
		if isinstance( error, commands.MissingRequiredArgument ):
			await ctx.send( f'{ctx.author.name} пожалуйста укажите кого кинуть в мут' )
		if isinstance( error, commands.MissingPermissions ):
			await ctx.send( f'{ctx.author.name} вы не можете использовать данную команду' )
	@mute_h.error
	async def mute_h( self, ctx, error ):
		if isinstance( error, commands.MissingRequiredArgument ):
			await ctx.send( f'{ctx.author.name} пожалуйста укажите кого кинуть в мут' )
		if isinstance( error, commands.MissingPermissions ):
			await ctx.send( f'{ctx.author.name} вы не можете использовать данную команду' )
	@unmute.error
	async def unmute_error(self, ctx, error):
		if isinstance( error, commands.MissingRequiredArgument ):
			await ctx.send( f'{ctx.author.name} пожалуйста укажите у кого убрать мут' )
		if isinstance( error, commands.MissingPermissions ):
			await ctx.send( f'{ctx.author.name} вы не можете использовать данную команду' )



def setup(client):
	client.add_cog(User(client))