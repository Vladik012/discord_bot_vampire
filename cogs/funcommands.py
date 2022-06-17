import discord
from discord.ext import commands
from asyncio import sleep
import random

class User(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

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
		


def setup(client):
	client.add_cog(User(client))