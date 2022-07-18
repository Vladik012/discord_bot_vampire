import discord
from discord.ext import commands
from asyncio import sleep


class User(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print('ban is connected')


	#banM
	@commands.command()
	@commands.has_permissions(ban_members = True)
	async def ban_m(self, ctx, member: discord.Member, time: int, *, reason=None):
		await ctx.send(f'{member.mention} **забанен** \n Продолжительность бана: *{time}m* \n Причина бана: *{reason}*')
		await member.send(f'Тебя забанили на сервере {ctx.guild.name} по причине {reason} на *{time}m*')

		channel = self.bot.get_channel(978309732349673532)
		await channel.send(f'Был забанен пользователь **{member.mention}** \n На сервере **{ctx.guild.name}** \n По причине: **{reason}** \n На время: ** {time}m ** ')

		await member.ban(reason=reason)
		await sleep(time * 60)
		await member.unban()
		await ctx.send(f'*У {member.mention} закончился бан*')
		link = await ctx.channel.create_invite(max_age=300)
		await member.send(f'Тебя разбанили на сервере {ctx.guild.name}! {link}')

	#banH
	@commands.command()
	@commands.has_permissions(ban_members = True)
	async def ban_h(self, ctx, member: discord.Member, time: int, *, reason):
		await ctx.send(f'{member.mention} **забанен** \n Продолжительность бана: *{time}h* \n Причина бана: *{reason}*')
		await member.send(f'Тебя забанили на сервере {ctx.guild.name} по причине {reason} на *{time}h*')

		channel = self.bot.get_channel(978309732349673532)
		await channel.send(f'Был забанен пользователь **{member.mention}** \n На сервере **{ctx.guild.name}** \n По причине: **{reason}** \n На время: ** {time}h ** ')

		await member.ban(reason=reason)
		await sleep(time * 3600)
		await member.unban()
		await ctx.send(f'*У {member.mention} закончился бан*')
		link = await ctx.channel.create_invite(max_age=300)
		await member.send(f'Тебя разбанили на сервере {ctx.guild.name}! {link}')
	#banD
	@commands.command()
	@commands.has_permissions(ban_members = True)
	async def ban(self, ctx, member: discord.Member, time: int, *, reason):
		await ctx.send(f'{member.mention} **забанен** \n Продолжительность бана: *{time}d* \n Причина бана: *{reason}*')
		await member.send(f'Тебя забанили на сервере {ctx.guild.name} по причине {reason} на *{time}d*')

		channel = self.bot.get_channel(978309732349673532)
		await channel.send(f'Был забанен пользователь **{member.mention}** \n На сервере **{ctx.guild.name}** \n По причине: **{reason}** \n На время: ** {time}d ** ')

		await member.ban(reason=reason)
		await sleep(time * 86400)
		await member.unban()
		await ctx.send(f'*У {member.mention} закончился бан*')
		link = await ctx.channel.create_invite(max_age=300)
		await member.send(f'Тебя разбанили на сервере {ctx.guild.name}! {link}')
	@ban_m.error
	async def ban_m_error( self, ctx, error ):
		if isinstance( error, commands.MissingRequiredArgument ):
			await ctx.send( f'{ctx.author.name} пожалуйста укажите кого нужно забанить' )
		if isinstance( error, commands.MissingPermissions ):
			await ctx.send( f'{ctx.author.name} вы не можете использовать данную команду' )

	@ban_h.error
	async def ban_h_error( self, ctx, error ):
		if isinstance( error, commands.MissingRequiredArgument ):
			await ctx.send( f'{ctx.author.name} пожалуйста укажите кого нужно забанить' )
		if isinstance( error, commands.MissingPermissions ):
			await ctx.send( f'{ctx.author.name} вы не можете использовать данную команду' )

	@ban.error
	async def ban_error( self, ctx, error ):
		if isinstance( error, commands.MissingRequiredArgument ):
			await ctx.send( f'{ctx.author.name} пожалуйста укажите кого нужно забанить' )
		if isinstance( error, commands.MissingPermissions ):
			await ctx.send( f'{ctx.author.name} вы не можете использовать данную команду' )


def setup(client):
	client.add_cog(User(client))