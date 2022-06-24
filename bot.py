import discord
from discord.ext import commands
import os, sqlite3
from asyncio import sleep
from discord.utils import get
import json
from Cybernator import Paginator as pag

def get_prefix(bot, message):
	with open('prefixes.json', 'r') as f:
		prefixes = json.load(f)

	return prefixes[str(message.guild.id)]

bot = commands.Bot(command_prefix = get_prefix)


@bot.event
async def on_ready():
	print('Я готов к работе')

@bot.event
async def on_guild_join(guild):
	with open('prefixes.json', 'r') as f:
		prefixes = json.load(f)

	prefixes[str(guild.id)] = '.'

	with open('prefixes.json', 'w') as f:
		json.dump(prefixes, f, indent=4)

@bot.event
async def on_guild_remove(guild):
	with open('prefixes.json', 'r') as f:
		prefixes = json.load(f)

	prefixes.pop[str(guild.id)]

	with open('prefixes.json', 'w') as f:
		json.dump(prefixes, f, indent=4)

@bot.command()
async def changeprefix(ctx, prefix):
	with open('prefixes.json', 'r') as f:
		prefixes = json.load(f)

	prefixes[str(ctx.guild.id)] = prefix

	with open('prefixes.json', 'w') as f:
		json.dump(prefixes, f, indent=4)

	await ctx.send(f'Перфикс изменен на {prefix}')


bot.remove_command('help')

@bot.event
async def on_ready():
	print('Я готов к работе')


	while True:
		await bot.change_presence(status = discord.Status.online, activity = discord.Activity(name = f'.help', type = discord.ActivityType.playing)) #Идёт инфа о команде помощи (префикс изменить)
		await sleep(15)
		await bot.change_presence(status = discord.Status.online, activity = discord.Activity(name = f'за {len(bot.guilds)} серверами', type = discord.ActivityType.watching)) #Инфа о количестве серверов, на котором находится бот.
		await sleep(15)	
		await bot.change_presence(status = discord.Status.online, activity = discord.Activity(name = f'за {len(bot.users)} пользователями', type = discord.ActivityType.watching))
		await sleep(15)


@bot.command()
async def load(ctx, extension):
	if ctx.author.id == 721024285346496574:
		bot.load_extension(f'cogs.{extension}')
		await ctx.message.delete(delay = 10)
		await ctx.send('Cogs is loaded...')
	else:
		await ctx.message.delete(delay = 10)
		await ctx.send('Error')

@bot.command()
async def unload(ctx, extension):
	if ctx.author.id == 721024285346496574:
		bot.unload_extension(f'cogs.{extension}')
		await ctx.message.delete(delay = 10)
		await ctx.send('Cogs is unloaded...')
	else:
		await ctx.message.delete(delay = 10)
		await ctx.send('Error')

@bot.command()
async def reload(ctx, extension):
	if ctx.author.id == 721024285346496574:
		bot.unload_extension(f'cogs.{extension}')
		bot.load_extension(f'cogs.{extension}')
		await ctx.message.delete(delay = 10)
		await ctx.send('Cogs is reloaded...')
	else:
		await ctx.message.delete(delay = 10)
		await ctx.send('Error')

@bot.event
async def on_guild_join(guild):
	channel = bot.get_channel(978021222493339668)
	await channel.send(f'Я вступил в гильдию **{guild.name}**. Теперь я на **' + str(len(bot.guilds)) + '** серверах')	
	await channel.send(f'Пользователей на сервере: ** ' + str(len(guild.members)) + '**')
	for role in guild.roles:
		if role.name == "muted":
			pass # role already exists
		else:
			perms = discord.Permissions(read_messages=True)
			return await guild.create_role(name='muted', permissions=perms)
@bot.event
async def on_guild_remove(guild):
	channel = bot.get_channel(988734401997316116)
	await channel.send(f'Меня выгнали из гильдии **{guild.name}**. Теперь я на **' + str(len(bot.guilds)) + '** серверах')




@bot.command()
async def help(ctx):
	embed1 = discord.Embed(tittle = 'Помощь по командам', 
		description = '''

		`.guilds` - Информация про то на скольких серверах бот
		`.ping` - Информация о пинге бота
		`.serverinfo` - Информация о сервере
		`.info` - Информация про пользователей (.info **@имя пользователя**)
		`.hug` - Обнять кого-то (.hug **@имя пользователя**)
		`.kiss` - Поцеловать кого-то (.kiss **@имя пользователя**)
		`.шар` - Комманда шар (.шар **Ваш вопрос**)
		`.invite` - Пригласить бота и зайти на сервер поддержки
		`.bug` - сообщить о баге


		''', color = 0x3498db)
	embed1.set_footer(text=f'Vladik012 ©️ Vampire | Все права защищены')
	embed2 = discord.Embed(tittle = 'Команды для админимтрации', 
		description = '''

		`.ban_m` - Забанить пользователя по минутам (.ban_m `ник нарушителя` `время бана` `причина бана`)
		`.ban_h` - Забанить пользователя по часам(.ban_h `ник нарушителя` `время бана` `причина бана`)
		`.ban` - Забанить пользователя по дням(.ban `ник нарушителя` `время бана` `причина бана`)
		`.kick` - Кикнуть пользователя (.kick **ник нарушителя**)
		`.clear` - Очистка сообщений (.clear **количество очищаемых сообщений**)
		`.mute` - Кинуть пользователя в мут по минутахм (.mute `время мута` `причина`)
		`.mute_h` - Кинуть пользователя в мут по в часам (.mute `время мута` `причина`)
		`.changeprefix` - Изменть префикс на сервере (.changeprefix **новый префикс**)

		''', color = 0xe74c3c)
	embed2.set_footer(text=f'Vladik012 ©️ Vampire | Все права защищены')
	embeds = [embed1, embed2]

	message_embed = await ctx.send(embed=embed1)
	page = pag(bot, message_embed, only=ctx.author, use_more = False, embeds=embeds, timeout = 120)
	await page.start()









@bot.event
async def on_member_join(member):
	await member.send(f'Приветствую {member} на сервере' )

async def on_member_remove(member):
	await member.send(f'Прощай {member}' )


@bot.command()
async def guilds(ctx):
	await ctx.send ('**Бот на:** ' + str(len(bot.guilds)) + ' серверах')
	await ctx.send ('**Пользуеться ботом:** ' + str(len(bot.users)) + ' пользоватетелей') 
	

		
for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		bot.load_extension(f"cogs.{filename[:-3]}")


bot.run('NzY4MTc4NjI0NDMxNjUyOTM0.GZoIbi.PlSZVLO1XPjYFHwjp86hTPCVTHxlN_NUknLP0g')
