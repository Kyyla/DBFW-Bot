import discord
import json
import os
from datetime import datetime
from discord.ext import commands
import time
import sched
from discord.utils import get
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import discord.utils 
import random
import datetime 
bot = commands.Bot(command_prefix="-z ", case_insensitive=True)
bot.remove_command('HELP')
@bot.event
async def on_ready(): 
	await bot.change_presence(activity = discord.Game("-z "))
	print ("Bot gei")
token = os.getenv("TOKEN")
ROLE2 = "Participante del Torneo"
ROLE = "Espectador del Torneo" 
bronce = ["Hazzel", "Azeirf", "HRX", "Pyrofarer","Axis","Zeit","Stelio","Kurima","Lorraine","Rogaza", "Kazabe", "Hundred", "Deneb", "Nebula", "Yuya", "Yazasem", "Nydaq", "LZR", "Reihan", "Legión", "Gohan (DB:S)", "Gond (WW)", "Yonedge (WW)", "Sake (WW)", "Zaku (WW)", "Vuko", "Goten", "Kyuri", "ShiroKuro", "Kyla", "Aerith", "Moori", "Icy", "Akamai", "Atomu", "Kumori", "N-25", "Seiji", "Macht VI", "Zukki", "Dai", "Ezekiel", "Shinsen the Reaper", "Bionicle", "Cassie", "Travis", "Cycyp", "Mr. Músculo", "Rhodex (WW)", "Suteki","Fireku", "Anz'olah", "A.A. Sting", "Sveglia", "Fern du Moshui", "Psypotato", "Blue", "Laven", "Level", "Bara", "Riesig", "Verlassen", "Sandown", "Ice", "Omega DBTLW", "Lance", "Ƶhivago/Legión (WW)", "Sunai", "Soren", "Paddo", "Kijito", "Malka", "Grope Itari", "Chikara", "Artich", "Kumi", "Maan Ashura", "Snow", "Seb Soyokazii", "Luke"]
broncebrillo = ["Nigma", "Kaibort (DBGD)","Saiko", "Belulz (KnG)"] 
plata = ["Tagoku (CW)", "Arctic (I&S)", "Komina (I&S)", "Kaih (DBGS)", "Gerft", "Kinom (Total)", "Kakaroto (TC)", "Kimmy (WW)", "Lance (DBDS)", "Omega (WF)","Rediktum-Yudai>AN<", "Sadness (WW)", "Rokoshi", "Saail (WW)", "Shouyu (CW)"]
platabrillo = ["╠ Klepsei ╣", "╠ Kynos ╣", "Nasu", "Masuta (RoC)","Sadness (CW)", "Zalitai (DBF)", "Hidaki (CW)", "Renasci", "Lance (DBPZ)", "Stroke (𝓩&𝓢)", "Saairu (𝓩&𝓢)", "Nix", "Makako (WW)", "Caelesti"]
oro = ["Leezer","Gondamek","Shuma (DBF)","《𝓚𝓸𝓼𝓱𝓾》"]
orobrillante = ["Rice-Zeek (DBF/WW)", "►Farnat◄", "Allez (DBF)", "Sugoki (Bamber)", "NZHN (I&S)"]
especial =["Nasu GFA", "Rice-Zeek GFA", "Allez GFA", "Zalitai GFA", "Sugoki Bamber GFA", "Nix GFA"]
todas =["Hazzel", "Azeirf", "HRX", "Pyrofarer","Axis","Zeit","Stelio","Kurima","Lorraine","Rogaza", "Kazabe", "Hundred", "Deneb", "Nebula", "Yuya", "Yazasem", "Nydaq", "LZR", "Reihan", "Legión", "Gohan", "Gond (WW)", "Yonedge (WW)", "Sake (WW)", "Zaku (WW)", "Vuko", "Goten", "Kyuri", "ShiroKuro", "Kyla", "Aerith", "Moori", "Icy", "Akamai", "Atomu", "Kumori", "N-25", "Seiji", "Macht VI", "Zukki", "Dai", "Ezekiel", "Shinsen the Reaper", "Bionicle", "Cassie", "Travis", "Cycyp", "Mr. Músculo", "Rhodex (WW)", "Suteki","Fireku", "Anz'olah", "A.A. Sting", "Sveglia", "Fern du Moshui", "Psypotato", "Blue", "Laven", "Level", "Bara", "Riesig", "Verlassen", "Sandown", "Ice", "Omega DBTLW","Nigma", "Kaibort (DBGD)","Saiko", "Belulz (KnG)","Tagoku (CW)", "Arctic (I&S)", "Komina (I&S)", "Kaih (DBGS)", "Gerft", "Kinom (Total)", "Kakaroto (TC)", "Kimmy (WW)", "Lance (DBDS)", "Lance", "Ƶhivago/Legión (WW)", "Omega (WF)","Rediktum-Yudai>AN<", "Sadness (WW)", "Rokoshi", "Saail (WW)", "Shouyu (CW)","╠ Klepsei ╣", "╠ Kynos ╣", "Nasu", "Masuta (RoC)","Sadness (CW)", "Zalitai (DBF)", "Hidaki (CW)", "Sunai", "Soren", "Paddo", "Kijito", "Malka", "Grope Itari", "Chikara", "Artich", "Kumi", "Maan Ashura", "Snow", "Seb Soyokazii", "Luke", "Renasci", "Lance (DBPZ)", "Stroke (𝓩&𝓢)", "Saairu (𝓩&𝓢)", "Nix", "Makako (WW)", "Caelesti","Leezer", "Gondamek", "Shuma (DBF)", "《𝓚𝓸𝓼𝓱𝓾》","Rice-Zeek (DBF/WW)", "►Farnat◄", "Allez (DBF)", "Sugoki (Bamber)", "NZHN (I&S)","Nasu GFA", "Rice-Zeek GFA", "Allez GFA", "Zalitai GFA", "Sugoki Bamber GFA", "Nix GFA"]
@bot.event
async def on_message(message): 
	if str(message.channel)== "reglas":
		if message.author.id != 347201351543160834:
			await message.channel.purge(limit=1)
	await bot.process_commands(message)
@bot.command()
async def acepto(ctx):
	user = ctx.author
	role = get(user.guild.roles,name = ROLE)
	await user.add_roles(role)
@bot.command()
async def Burocrata(ctx):
    await ctx.send("Cosmic es burócrata 10/10, todo mi apoyo, un grande de grandes")
@bot.command()
async def Cosmic(ctx):
    await ctx.send("Admin ocupado")
    await ctx.send(file=discord.File('Cosmic.gif'))
@bot.command()
async def HxH(ctx):
	await ctx.send("https://hunter-x-hunter-fanon.fandom.com/es/wiki/Wiki_Hunter_x_Hunter_Fanon")
@bot.command()
async def DBW(ctx):
	await ctx.send(file=discord.File("DBW.jpg"))
@bot.command()
async def Farnat(ctx):
	await ctx.send(file=discord.File("Farnat.jpg"))
@bot.command()
async def Rayuke(ctx):
	await ctx.send("Gay-uke")
@bot.command()
async def NotSo (ctx):
	await ctx.send("Fuck you, NotSoBot, yo si funciono")
@bot.command()
async def Gond(ctx):
	await ctx.send("¿Y el capítulo de World Wikia?") 
@bot.command()
async def Deri(ctx):
	await ctx.send("Esperabas una respuesta, pero era yo Di....iggy de ovas")
	await ctx.send(file=discord.File('Iggy.png'))
@bot.command()
async def Kanda(ctx):
	await ctx.send(file=discord.File("Kanda.jpg"))
@bot.command(aliases = ["Crimson","Son destroyer ss2"])
async def Crim(ctx):
	await ctx.send("¿Quién?")
@bot.command()
async def primo(ctx,arg,arg2):
	arg = arg + " " + arg2
	if arg.upper() == "DE CRIMSON" or arg.upper() == "DE CRIM":
		await ctx.send("Momento Venezuela")
@bot.command()
async def Dark(ctx,arg):
	if arg.upper() == "FURRO":
		await ctx.send(file=discord.File("Dark.jpg"))
@bot.command()
async def Bybychu(ctx):
    await ctx.send("No te pago, ya hice mi propio bot, y es mejor")
@bot.command()
async def Sting(ctx):
	await ctx.send("Maricón")
@bot.command()
async def Omega(ctx):
    await ctx.send("Chat muerto")
@bot.command()
async def Roberto(ctx):
	await ctx.send("Omega, ponle rol")
@bot.command()
async def Jupero(ctx):
	y = random.randint(1,8)
	x = "Jupero"+str(y)
	x = x + ".jpg"
	print(x)
	await ctx.send(file=discord.File(x))
@bot.command()
async def Cif (ctx):
	await ctx.send(file=discord.File("Cif.jpg"))
@bot.command()
async def Zakura(ctx):
    await ctx.send("Pasa pac..digo patas")
    await ctx.send("pack*")
@bot.command()
async def UCP(ctx):
	await ctx.send(file=discord.File("UCP.jpg"))
@bot.command()
async def Turles(ctx):
	await ctx.send(file=discord.File("Turles.jpg"))
@bot.command()
async def DBFW(ctx):
    await ctx.send("DBFW: 1")
    await ctx.send("Todas las otras wikis geis sin un bot: 0")
@bot.command()
async def Lon(ctx):
    await ctx.send("Lon hermosa")
@bot.command()
async def Saail(ctx):
    await ctx.send("¿El creador del furro rojo?")
@bot.command()
async def Sinidius(ctx):
    await ctx.send("Sinidius, prende el server")
@bot.command()
async def Diego(ctx):
	await ctx.send("Ochako cagando")
	x = random.randint(1,2)
	if x == 1:
		await ctx.send(file=discord.File("Ochako.png"))
	else:	
		await ctx.send(file=discord.File("Ochako2.png"))
@bot.command()
async def Nusita(ctx):
	await ctx.send("THE GAME")
@bot.command(aliases=["Kyo"])
async def Kyomist (ctx):
	await ctx.send(file=discord.File('Kyomist.png'))
@bot.command()
async def Buitre(ctx):
	await ctx.send(file=discord.File("buitre.gif"))	
@bot.command()
async def Dibujo (ctx):
	await ctx.send("Nadie:")
	await ctx.send("Saail:")
	await ctx.send(file=discord.File("Dibujo.png"))
@bot.command()
async def Uziel (ctx):
	await ctx.send("¿Este comando es para siempre o solo durá nueve horas?")
@bot.command()
async def Allez (ctx):
	await ctx.send(file=discord.File('Allez.png'))
@bot.command(aliases = ["Fantendo"])
async def Blade (ctx):
	await ctx.send("Hail Fantendo")
	await ctx.send(file=discord.File('Blade.png'))
@bot.command()
async def Makaio(ctx):
	await ctx.send(file=discord.File("Maka.jpg"))
@bot.command()
async def Heyta (ctx):
	await ctx.send(file=discord.File('Heyta.png'))
@bot.command()
async def Tyson (ctx,arg=None):
	if arg is None:
		await ctx.send(file=discord.File('Tyson.png'))
	elif arg.upper() == "TRIVIA":
		await ctx.send(file=discord.File('Tyson.jpg'))
@bot.command()
async def Admin (ctx,*,arg = None):
	if not arg:    
		await ctx.send("Admin ocupado")
		await ctx.send(file=discord.File('Cosmic.gif'))
	elif arg.upper() == "CHIKI FURRO":
		await ctx.send(file=discord.File("admin chikifurro.jpg"))
	else:
		await ctx.send(file=discord.File("Admin chikito.png"))
@bot.command()
async def Mario (ctx):
	await ctx.send(file=discord.File("Mario.jpg"))
@bot.command()
async def Bluezin (ctx):
	await ctx.send(file=discord.File('Bluezin.jpg'))
@bot.command()
async def Shinji (ctx):
	await ctx.send(file=discord.File("Omedetou.gif"))
@bot.command()
async def Trivia (ctx):
	await ctx.send(file=discord.File("Anti-Tyson.jpg"))
@bot.command()
async def F (ctx):
	await ctx.send("F")
	await ctx.send(file=discord.File("Chat.png"))
@bot.command()
async def SiniYandere (ctx):
	await ctx.send(file=discord.File("Sini.gif"))
@bot.command()
async def Zakurapack(ctx):
	await ctx.send(file=discord.File("pack.jpg"))
@bot.command()
async def Simp(ctx):
	await ctx.send(file=discord.File("Simp.png"))
@bot.command()
async def Lance(ctx):
	await ctx.send(file=discord.File("Lance.jpg"))
@bot.command()
async def Gokuta(ctx):
	await ctx.send ("Vetrom le ganan't")
@bot.command()
async def Trivago(ctx):
	await ctx.send (file=discord.File("Trivago.jpg"))
@bot.command()
async def Zenis(ctx):
	await ctx.send(file=discord.File("Blade_z.jpg"))	
@bot.command(aliases = ["Membresia"])
async def Membresía (ctx):
	await ctx.send(file=discord.File("Membresía.jpg"))
@bot.command()
async def Sugoki(ctx):
	await ctx.send("¿Cuántos teamkaichis tenés?")
@bot.command()
async def prueba (ctx):
	await ctx.send ("@!" + str(ctx.author.id))
@bot.command()
async def usuario (ctx,arg,member: discord.Member):
	if ctx.author.id == 315221475051307028:
		if arg.upper() == "PREMIUM":
			user = member
			role = get(user.guild.roles,name = "Usuario Premium")
			await user.add_roles(role)
			await ctx.send("{0} es ahora un usuario premium".format(user))
	else: 
		await ctx.send("No tienes permiso para usar este comando.")
bot.run(token)