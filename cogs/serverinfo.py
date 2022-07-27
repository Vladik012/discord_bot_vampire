import discord
from discord.ext import commands
from asyncio import sleep

class User(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print('server info is connected')

	@commands.command()
	async def serverinfo(self, ctx):
		name = str(ctx.guild.name)
		description = str(ctx.guild.description)

		owner = str(ctx.guild.owner)
		id = str(ctx.guild.id)
		region = str(ctx.guild.region)
		memberCount = str(ctx.guild.member_count)

		icon = str(ctx.guild.icon_url)

		text_channels = len(ctx.guild.text_channels)
		voice_channels = len(ctx.guild.voice_channels)
		categories = len(ctx.guild.categories)
		channels = text_channels + voice_channels
		format = "%a, %d %b %Y | %H:%M:%S %ZGMT"
   
		embed = discord.Embed(
			title=" Информация о сервере - " + name,
			color=discord.Color.blue()
			)
		embed.set_thumbnail(url=icon)
		embed.add_field(name="Владелец", value=owner, inline=False)
		embed.add_field(name="Server ID", value=id, inline=False)
		embed.add_field(name="Регион", value=region, inline=False)
		embed.add_field(name="Пользователей", value=memberCount, inline=False)
		embed.add_field(name="Всего каналов", value=f'{channels}', inline=False) 
		embed.add_field(name="Текстовых каналов", value=f'{text_channels}', inline=False) 
		embed.add_field(name=" Голосовых каналов", value=f'{voice_channels}', inline=False) 

		embed.add_field(name="Дата создания", value=f'{ctx.guild.created_at.strftime(format)}', inline=False)
		
		
		await ctx.send(embed=embed)





def setup(client):
	client.add_cog(User(client))
