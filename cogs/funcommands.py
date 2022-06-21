import discord
from discord.ext import commands
from asyncio import sleep
import random
import aiohttp

class User(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.invite = 'https://inlnk.ru/846XV7'
		self.server = 'https://discord.gg/kyFQDnU4u9'

	@commands.Cog.listener()
	async def on_ready(self):
		print('funcommands is connected')

	@commands.command()
	async def hug(self, ctx, member: discord.Member = None):
		HUG = ["https://c.tenor.com/OXCV_qL-V60AAAAC/mochi-peachcat-mochi.gif",
		"https://c.tenor.com/jU9c9w82GKAAAAAC/love.gif",
		"https://c.tenor.com/ZzorehuOxt8AAAAC/hug-cats.gif",
		"https://c.tenor.com/GwFP_tY-jmQAAAAC/hug-hugs-and-love.gif"]
		author = ctx.author
		embed = discord.Embed(title="Объятия!", description=f"{author.display_name} обнял(a) {member.display_name}", color = discord.Color.green())
		embed.set_image(url = random.choice(HUG))
		await ctx.send(embed=embed)


	@commands.command()
	async def kiss(self, ctx, member: discord.Member = None):
		HUG = ["https://c.tenor.com/217aKgnf16sAAAAC/kiss.gif",
		"https://c.tenor.com/wPzIJLI3IeQAAAAC/kiss-hot.gif",
		"https://c.tenor.com/FgYExssph6MAAAAC/kiss-love.gif",
		"https://c.tenor.com/4wtQ-7iub7AAAAAC/ishupanda-happy.gif"]	
		author = ctx.author
		embed = discord.Embed(title="Поцелуй!", description=f"{author.display_name} поцеловал(a) {member.display_name}", color = discord.Color.purple())
		embed.set_image(url = random.choice(HUG))
		await ctx.send(embed=embed)


	


	@commands.command(name='Шар', aliases=['shar', 'шар'])
	async def Шар(self, ctx, *, question):
		responses = [
		'Это точно.',
		'Очень даже вряд-ли.',
		'Нет.',
		'Да, безусловно.',
		'Вы можете рассчитывать на это.',
		'Вероятно.',
		'Перспектива хорошая.',
		'Да.',
		'Знаки указывают - да.',	
		'50/50',
		'мой ответ - нет.',
		'Мои источники говорят нет.',
		'Перспективы не очень.',
		'Очень сомнительно.'
		]
		embed = discord.Embed(title='Шар', color=0xFF0000)
		embed.add_field(name='Шар говорит:', value=random.choice(responses))
		await ctx.send(content=f'[:8ball:] Шар говорит\n', embed=embed)
	@commands.command()
	async def invite(self, ctx):
		embed=discord.Embed(
            title="Пригласить бота",
            timestamp = ctx.message.created_at,
            color = 0xf1c40f
        )

		embed.add_field(
			name = "Добавить бота на свой сервер",
			value = "[Добавить]({0.invite})".format(self),
			inline = False
		)
		embed.add_field(
			name = "Оффициальный сервер бота",
			value = "[Зайти]({0.server})".format(self),
			inline = False
		)
		
		await ctx.send(embed = embed)


def setup(client):
	client.add_cog(User(client))