import discord
from discord.ext import commands
from asyncio import sleep

class User(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print('info is connected')
	@commands.command()
	async def info(self, ctx,member: discord.Member = None):
		t = member.status
		if t == discord.Status.online:
			d = " В сети 🟢"
		elif t == discord.Status.offline:
			d = " Не в сети <:offline1:988409218153447434>"
		elif t == discord.Status.idle:
			d = " Не активен 🌙"
		elif t == discord.Status.dnd:
			d = " Не беспокоить ⛔"
		emb = discord.Embed(title = 'Информация об пользователе', color = 0xFF8000)
		emb.add_field(name="Активность:", value=d, inline=False)
		emb.add_field(name = 'Когда присоеденился:', value = member.joined_at ,inline = False)
		emb.add_field(name = 'Имя:', value = member.display_name, inline = False)
		emb.add_field(name = 'Айди:', value = member.id, inline = False)
		emb.add_field(name = 'Дата создания аккаунта', value = member.created_at.strftime("%b %d %Y at %H:%M"), inline = False )
		emb.set_thumbnail(url=member.avatar_url)
		emb.set_footer(text=f'Запрошено: {ctx.message.author}', icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed = emb)
	@info.error
	async def info_error( self, ctx, error ):
		if isinstance( error, commands.MissingRequiredArgument ):
			await ctx.send( f'{ctx.author.name} пожалуйста укажите кого информацию хотите посмотреть' )


def setup(client):
	client.add_cog(User(client))
