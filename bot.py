import discord
from discord.ext import commands
import os, sqlite3
from asyncio import sleep
from discord.utils import get
import json
from Cybernator import Paginator as pag

import collections
from pymongo import MongoClient

cluster = MongoClient('mongodb+srv://Vladik012:Vladik0713@vladik012.z3qq6fz.mongodb.net/?retryWrites=true&w=majority')
collusers = cluster.vladik012data.collusers
collservers = cluster.vladik012data.collservers

intents = discord.Intents().all()


def get_prefix(bot, message):
	prefix = collservers.find_one({"_id": message.guild.id})["prefix"]
	return prefix

bot = commands.Bot(command_prefix = get_prefix, intents = intents)


	

@bot.event
async def on_guild_join(guild):
	collservers.insert_one({"_id": guild.id, "prefix": '.'})
	


@bot.event
async def on_guild_remove(guild):
	collservers.delete_one(
		{
			'_id': guild.id
		}
	)

@bot.command()
@commands.has_permissions(administrator = True)
async def prefix(ctx, prefix):
	if prefix is None:
		await ctx.send('Префикс не найден')
	else:
		collservers.update_one({'_id': ctx.guild.id}, {'$set': {'prefix': prefix}})
		await ctx.send(f'Новый префикс: {prefix}')

@prefix.error
async def prefix_error(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.send( f'{ctx.author.name} вы не можете использовать данную команду' )



#@bot.command()
#async def changeprefix(ctx, prefix):
#	with open('prefixes.json', 'r') as f:
#		prefixes = json.load(f)
#
#	prefixes[str(ctx.guild.id)] = prefix
#
#	with open('prefixes.json', 'w') as f:
#		json.dump(prefixes, f, indent=4)
#
#	await ctx.send(f'Перфикс изменен на {prefix}')
	
	
	
bot.remove_command('help')

@bot.event
async def on_ready():
	print('Я готов к работе')

	for guild in bot.guilds:
		for members in guild.members:
			
			values = {
				'_id': guild.id,
				'prefix': '.'
			}
		if collservers.count_documents({'_id':guild.id, 'prefix': '.'}) == 0:
			collservers.insert_one(values)


	

@bot.event
async def on_ready():
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
	await channel.send(f'Создатель гильдии {guild.owner}')
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


#@bot.command()
#async def test(ctx):
#	await ctx.send(f'{bot.guilds}')

'''
@bot.command()
async def help(ctx):
	embed1 = discord.Embed(tittle = 'Помощь по командам', 
		description = '''
'''
		`.guilds` - Информация про то на скольких серверах бот
		`.ping` - Информация о пинге бота
		`.serverinfo` - Информация о сервере
		`.info` - Информация про пользователей (.info **@имя пользователя**)
		`.hug` - Обнять кого-то (.hug **@имя пользователя**)
		`.kiss` - Поцеловать кого-то (.kiss **@имя пользователя**)
		`.шар` - Комманда шар (.шар **Ваш вопрос**)
		`.invite` - Пригласить бота и зайти на сервер поддержки
		`.кости` - Игра в кости
		`.vote` - проголосовать за бота
'''		


''', color = 0x3498db)
	embed1.set_footer(text=f'Vladik012 ©️ Vampire | Все права защищены')
	embed2 = discord.Embed(tittle = 'Команды для админимтрации', 
		description = '''
'''
		`.ban_m` - Забанить пользователя по минутам (.ban_m `ник нарушителя` `время бана` `причина бана`)
		`.ban_h` - Забанить пользователя по часам(.ban_h `ник нарушителя` `время бана` `причина бана`)
		`.ban` - Забанить пользователя по дням(.ban `ник нарушителя` `время бана` `причина бана`)
		`.kick` - Кикнуть пользователя (.kick **ник нарушителя**)
		`.clear` - Очистка сообщений (.clear **количество очищаемых сообщений**)
		`.mute` - Кинуть пользователя в мут по минутахм (.mute `время мута` `причина`)
		`.mute_h` - Кинуть пользователя в мут по в часам (.mute `время мута` `причина`)
		`.bug` - сообщить о баге
		'''
'''
		, color = 0xe74c3c)

	embed2.set_footer(text=f'Vladik012 ©️ Vampire | Все права защищены')
	embeds = [embed1, embed2]

	message_embed = await ctx.send(embed=embed1)
	page = pag(bot, message_embed, only=ctx.author, use_more = False, embeds=embeds, timeout = 120)
	await page.start()
	'''

@bot.group(invoke_without_command = True)
async def help(ctx):
	em = discord.Embed(tittle = 'Помощ', description = 'Используйте .help `название комманды` чтобы получить помощ по определенной команде', color = ctx.author.color)

	em.add_field(name='Moderation', value = 'ban, kick, mute, clear')
	em.add_field(name='Fun', value = 'guilds, ping, serverinfo, info, avatar, hug, kiss, шар, invite, кости, vote')

	await ctx.send(embed = em)

@help.command()
async def kick(ctx):
	em = discord.Embed(title = '.kick', description='Кикнуть пользователя', color = ctx.author.color)

	em.add_field(name = '*Syntax*', value = '.kick `никнейм пользователя которого нужно кикнуть` `причина`')

	await ctx.send(embed = em)

@help.command()
async def ban(ctx):
	em = discord.Embed(title = '.ban', description='Забанить пользователя', color = ctx.author.color)

	em.add_field(name = '*Syntax*', value = '.ban `никнейм пользователя которого нужно забанить` `причина` (забанить пользователя по дням)')
	em.add_field(name = '*Syntax*', value = '.ban_h `никнейм пользователя которого нужно забанить` `причина` (забанить пользователя по часам)')
	em.add_field(name = '*Syntax*', value = '.ban_m `никнейм пользователя которого нужно забанить` `причина` (забанить пользователя по минутам)')

	await ctx.send(embed = em)

@help.command()
async def mute(ctx):
	em = discord.Embed(title = '.mute', description='Замьютить пользователя', color = ctx.author.color)

	em.add_field(name = '*Syntax*', value = '.mute `никнейм пользователя которого нужно замьютить` `причина` (минутный мьют)')
	em.add_field(name = '*Syntax*', value = '.mute_h `никнейм пользователя которого нужно замьютить` `причина` (часовой мьют)')

	await ctx.send(embed = em)

@help.command()
async def clear(ctx):
	em = discord.Embed(title = '.clear', description='Очистить сообщения', color = ctx.author.color)

	em.add_field(name = '*Syntax*', value = '.clear `количество очищаемых сообщений` ')

	await ctx.send(embed = em)

@help.command()
async def guilds(ctx):
	em = discord.Embed(title = '.guilds', description='На скольких сервераах бот', color = ctx.author.color)

	em.add_field(name = '*Syntax*', value = '.guilds')

	await ctx.send(embed = em)


@help.command()
async def ping(ctx):
	em = discord.Embed(title = '.ping', description='Узнать пинг бота', color = ctx.author.color)

	em.add_field(name = '*Syntax*', value = '.ping')

	await ctx.send(embed = em)

@help.command()
async def serverinfo(ctx):
	em = discord.Embed(title = '.serverinfo', description='Узнать информацию о сервере', color = ctx.author.color)

	em.add_field(name = '*Syntax*', value = '.serverinfo')

	await ctx.send(embed = em)

@help.command()
async def avatar(ctx):
	em = discord.Embed(title = '.avatar', description='Отобразить аватар пользователя', color = ctx.author.color)

	em.add_field(name = '*Syntax*', value = '.avatar `Ник пользователя`')

	await ctx.send(embed = em)

@help.command()
async def info(ctx):
	em = discord.Embed(title = '.info', description='Узнать информацию о пользователе', color = ctx.author.color)

	em.add_field(name = '*Syntax*', value = '.info `никнейм пользователя`')

	await ctx.send(embed = em)

@help.command()
async def hug(ctx):
	em = discord.Embed(title = '.hug', description='Обнять пользователя', color = ctx.author.color)

	em.add_field(name = '*Syntax*', value = '.hug `никнейм пользователя`')

	await ctx.send(embed = em)

@help.command()
async def kiss(ctx):
	em = discord.Embed(title = '.kiss', description='Поцеловать пользователя', color = ctx.author.color)

	em.add_field(name = '*Syntax*', value = '.kiss `никнейм пользователя`')

	await ctx.send(embed = em)

@help.command()
async def шар(ctx):
	em = discord.Embed(title = '.шар', description='Узнать ответ на свой вопрос', color = ctx.author.color)

	em.add_field(name = '*Syntax*', value = '.шар `Ваш вопрос`')

	await ctx.send(embed = em)

@help.command()
async def invite(ctx):
	em = discord.Embed(title = '.invite', description='Пригласить бота на свой сервер', color = ctx.author.color)

	em.add_field(name = '*Syntax*', value = '.invite')

	await ctx.send(embed = em)

@help.command()
async def кости(ctx):
	em = discord.Embed(title = '.кости', description='Мини игра с ботом', color = ctx.author.color)

	em.add_field(name = '*Syntax*', value = '.кости')

	await ctx.send(embed = em)

@help.command()
async def vote(ctx):
	em = discord.Embed(title = '.vote', description='Проголосовать за бота', color = ctx.author.color)

	em.add_field(name = '*Syntax*', value = '.vote')

	await ctx.send(embed = em)




@bot.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member:discord.Member, time:int):
	mute_role = discord.utils.get(ctx.message.guild.roles, name = 'muted')
	await member.add_roles(mute_role)
	await ctx.send(f'Был кинут в мут пользователь {member.mention}, на время {time} м')
	await sleep(time * 60)
	await member.remove_roles(mute_role)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def mute_h(ctx, member:discord.Member, time:int):
	mute_role = discord.utils.get(ctx.message.guild.roles, name = 'muted')
	await member.add_roles(mute_role)
	await ctx.send(f'Был кинут в мут пользователь {member.mention}, на время {time} ч')
	await sleep(time * 360)
	await member.remove_roles(mute_role)



@mute.error
async def mute( ctx, error ):
	if isinstance( error, commands.MissingRequiredArgument ):
		await ctx.send( f'{ctx.author.name} чего-то не хватает (.mute `пользователь` `время`)' )
	if isinstance( error, commands.MissingPermissions ):
		await ctx.send( f'{ctx.author.name} вы не можете использовать данную команду' )
@mute_h.error
async def mute_h( ctx, error ):
	if isinstance( error, commands.MissingRequiredArgument ):
		await ctx.send( f'{ctx.author.name} чего-то не хватает (.mute `пользователь` `время`)' )
	if isinstance( error, commands.MissingPermissions ):
		await ctx.send( f'{ctx.author.name} вы не можете использовать данную команду' )











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
