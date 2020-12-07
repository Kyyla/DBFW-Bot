import discord
import json
import os
from datetime import datetime
from discord.ext import commands
import time
import sched
from discord.utils import get
from discord.ext.commands import Bot
import asyncio
import discord.utils 
import random
import datetime
bot = commands.Bot(command_prefix="-z ")
TOKEN = "NzQ3OTQwNjUyNjE1OTkxNDI3.X0WMAw.InKxa9OYN8CsAroS8YZnoEqk9jM"
os.chdir("C:\\Users\\donki\\OneDrive\\Escritorio\\bot")
alarm_time = '7:41'#24hrs
channel_id = "671487552754024479"
@bot.event
async def on_ready(): 
	await bot.change_presence(activity = discord.Game("-z "))
	print ("Bot gei")
ROLE = "Usuario/a"
bot.remove_command('help')
bronce = ["Hazzel", "Azeirf", "HRX", "Pyrofarer","Axis","Zeit","Stelio","Kurima","Lorraine","Rogaza", "Kazabe", "Hundred", "Deneb", "Nebula", "Yuya", "Yazasem", "Nydaq", "LZR", "Reihan", "Legión", "Gohan (DB:S)", "Gond (WW)", "Yonedge (WW)", "Sake (WW)", "Zaku (WW)", "Vuko", "Goten", "Kyuri", "ShiroKuro", "Kyla", "Aerith", "Moori", "Icy", "Akamai", "Atomu", "Kumori", "N-25", "Seiji", "Macht VI", "Zukki", "Dai", "Ezekiel", "Shinsen the Reaper", "Bionicle", "Cassie", "Travis", "Cycyp", "Mr. Músculo", "Rhodex (WW)", "Suteki","Fireku", "Anz'olah", "A.A. Sting", "Sveglia", "Fern du Moshui", "Psypotato", "Blue", "Laven", "Level", "Bara", "Riesig", "Verlassen", "Sandown", "Ice", "Omega DBTLW", "Lance", "Ƶhivago/Legión (WW)", "Sunai", "Soren", "Paddo", "Kijito", "Malka", "Grope Itari", "Chikara", "Artich", "Kumi", "Maan Ashura", "Snow", "Seb Soyokazii", "Luke"]
broncebrillo = ["Nigma", "Kaibort (DBGD)","Saiko", "Belulz (KnG)"] 
plata = ["Tagoku (CW)", "Arctic (I&S)", "Komina (I&S)", "Kaih (DBGS)", "Gerft", "Kinom (Total)", "Kakaroto (TC)", "Kimmy (WW)", "Lance (DBDS)", "Omega (WF)","Rediktum-Yudai>AN<", "Sadness (WW)", "Rokoshi", "Saail (WW)", "Shouyu (CW)"]
platabrillo = ["╠ Klepsei ╣", "╠ Kynos ╣", "Nasu", "Masuta (RoC)","Sadness (CW)", "Zalitai (DBF)", "Hidaki (CW)", "Renasci", "Lance (DBPZ)", "Stroke (𝓩&𝓢)", "Saairu (𝓩&𝓢)", "Nix", "Makako (WW)", "Caelesti"]
oro = ["Leezer","Gondamek","Shuma (DBF)","《𝓚𝓸𝓼𝓱𝓾》"]
orobrillante = ["Rice-Zeek (DBF/WW)", "►Farnat◄", "Allez (DBF)", "Sugoki (Bamber)", "NZHN (I&S)"]
especial =["Nasu GFA", "Rice-Zeek GFA", "Allez GFA", "Zalitai GFA", "Sugoki Bamber GFA", "Nix GFA"]
todas =["Hazzel", "Azeirf", "HRX", "Pyrofarer","Axis","Zeit","Stelio","Kurima","Lorraine","Rogaza", "Kazabe", "Hundred", "Deneb", "Nebula", "Yuya", "Yazasem", "Nydaq", "LZR", "Reihan", "Legión", "Gohan", "Gond (WW)", "Yonedge (WW)", "Sake (WW)", "Zaku (WW)", "Vuko", "Goten", "Kyuri", "ShiroKuro", "Kyla", "Aerith", "Moori", "Icy", "Akamai", "Atomu", "Kumori", "N-25", "Seiji", "Macht VI", "Zukki", "Dai", "Ezekiel", "Shinsen the Reaper", "Bionicle", "Cassie", "Travis", "Cycyp", "Mr. Músculo", "Rhodex (WW)", "Suteki","Fireku", "Anz'olah", "A.A. Sting", "Sveglia", "Fern du Moshui", "Psypotato", "Blue", "Laven", "Level", "Bara", "Riesig", "Verlassen", "Sandown", "Ice", "Omega DBTLW","Nigma", "Kaibort (DBGD)","Saiko", "Belulz (KnG)","Tagoku (CW)", "Arctic (I&S)", "Komina (I&S)", "Kaih (DBGS)", "Gerft", "Kinom (Total)", "Kakaroto (TC)", "Kimmy (WW)", "Lance (DBDS)", "Lance", "Ƶhivago/Legión (WW)", "Omega (WF)","Rediktum-Yudai>AN<", "Sadness (WW)", "Rokoshi", "Saail (WW)", "Shouyu (CW)","╠ Klepsei ╣", "╠ Kynos ╣", "Nasu", "Masuta (RoC)","Sadness (CW)", "Zalitai (DBF)", "Hidaki (CW)", "Sunai", "Soren", "Paddo", "Kijito", "Malka", "Grope Itari", "Chikara", "Artich", "Kumi", "Maan Ashura", "Snow", "Seb Soyokazii", "Luke", "Renasci", "Lance (DBPZ)", "Stroke (𝓩&𝓢)", "Saairu (𝓩&𝓢)", "Nix", "Makako (WW)", "Caelesti","Leezer", "Gondamek", "Shuma (DBF)", "《𝓚𝓸𝓼𝓱𝓾》","Rice-Zeek (DBF/WW)", "►Farnat◄", "Allez (DBF)", "Sugoki (Bamber)", "NZHN (I&S)","Nasu GFA", "Rice-Zeek GFA", "Allez GFA", "Zalitai GFA", "Sugoki Bamber GFA", "Nix GFA"]
@bot.command()
async def Acepto(ctx):
	member = ctx.author
	role = get(member.guild.roles,name = ROLE)
	await member.add_roles(role)
@bot.command()
async def Burocrata(ctx):
    await ctx.send("Cosmic es burócrata 10/10, todo mi apoyo, un grande de grandes")
@bot.command()
async def Cosmic(ctx):
    await ctx.send("Admin ocupado")
    await ctx.send(file=discord.File('Cosmic.gif'))
@bot.command()
async def DBW(ctx):
	await ctx.send(file=discord.File("DBW.jpgx"))
@bot.command()
async def Rayuke(ctx):
	await ctx.send("Gay-uke")
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
@bot.command()
async def Bybychu(ctx):
    await ctx.send("No te pago, ya hice mi propio bot, y es mejor")
@bot.command()
async def Sting(ctx):
	await ctx.send("No, no vamos a jugar Among us.")
@bot.command()
async def Omega(ctx):
    await ctx.send("Chat muerto")
@bot.command()
async def Roberto(ctx):
	await ctx.send("Omega, ponle rol")
@bot.command()
async def Jupero(ctx):
    await ctx.send("Mmmm Caballos")
@bot.command()
async def Zakura(ctx):
    await ctx.send("Pasa pac..digo patas")
    await ctx.send("pack*")
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
@bot.command()
async def Kyomist (ctx):
	await ctx.send(file=discord.File('Kyomist.png'))
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
@bot.command()
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
async def Tyson (ctx):
	await ctx.send(file=discord.File('Tyson.jpg'))
@bot.command()
async def Admin (ctx, arg = None):
	if not arg:    
		await ctx.send("Admin ocupado")
		await ctx.send(file=discord.File('Cosmic.gif'))
	else:
		await ctx.send(file=discord.File("Admin chikito.png"))
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
async def perder(ctx):
	if ctx.author.id == 265725029902319616:
		with open("it.json","r") as f:
			users = json.load(f)
		users["Nada"]["cuenta"] = 1
		with open("it.json", "w") as f:
			json.dump(users,f)
@bot.command()
async def normal(ctx):
	if ctx.author.id == 265725029902319616:
		with open("it.json","r") as f:
			users = json.load(f)
		users["Nada"]["cuenta"] = 0
		with open("it.json", "w") as f:
			json.dump(users,f)
@bot.command()
async def Wiki (ctx):
	await ctx.send("https://dragonballfanon.fandom.com/es/wiki/Dragon_Ball_Fanon_Wiki")
@bot.command()
async def Album(ctx, member: discord.Member= None):
	if member is None: 
		user = ctx.author
	else: user = member
	await open_account0(user)
	users = await get_bank_data0()
	acc = users[str(user.id)]["cuenta"]
	embed = discord.Embed(title="Album", desciption = "")
	cont = 0
	for i in range (0,(len(acc)-1)):
		if cont == 0:
			x = "Tienes " + str(acc[i+1])
			embed.add_field(name = acc[i], value= x)
			cont = 1
		else: cont = 0
	await ctx.send(content=None, embed=embed)
@bot.command()
async def Búsqueda(ctx,arg,member: discord.Member= None):
	if member is None: 
		user = ctx.author
	else: user = member
	await open_account0(user)
	users = await get_bank_data0()
	acc = users[str(user.id)]["cuenta"]
	cont = False
	for i in range (0,len(todas)):
		if arg == todas[i]: cont = True
	if cont == False: await ctx.send("Esa carta no existe")
	else:
		cont = False
		for i in range(0,len(acc)):
			if arg == acc[i]: 
				cont = True
				x = arg + " (x" + str(acc[i + 1]) + ")"
				await ctx.send(x)
		if cont == False: await ctx.send("No tienes esa carta")
@bot.command()
async def Repetidas(ctx, member: discord.Member=None):
	if member is None: 
		user = ctx.author
	else: user = member
	await open_account0(user)
	users = await get_bank_data0()
	acc = users[str(user.id)]["cuenta"]
	cont = False
	acc2 = []
	for i in range(1,(len(acc)),2):
		cont2 = True
		if acc[i] != 1:
			acc2.append(acc[i-1])
			acc2.append(acc[i])
	if len(acc2) == 0:
		await ctx.send("No tienes cartas repetidas")
	else:
		embed = discord.Embed(title="Album", desciption = "")
		cont = 0	
		for i in range (0,(len(acc2)-1)):
			if cont == 0:
				x = "Tienes " + str(acc2[i+1])
				embed.add_field(name = acc2[i], value= x)
				cont = 1
			else: cont = 0
	await ctx.send(content=None, embed=embed)
@bot.command()
async def Cambio (ctx, member: discord.Member):
	user = ctx.author
	user2 = member
	await open_account0(user)
	await open_account0(user2)
	users = await get_bank_data0()
	acc = users[str(user2.id)]["cuenta"]
	acc3 = users[str(user.id)]["cuenta"]
	cont = False
	acc2 = []
	for i in range(1,(len(acc)),2):
		cont2 = True
		if acc[i] != 1:
			acc2.append(acc[i-1])
			acc2.append(acc[i])
	if len(acc2) == 0:
		await ctx.send("Ninguna.")
	else:
		acc= []
		for i in range (0,len(acc3),2):
			for j in range (0,len(acc2),2):
				if acc2[j] == acc3[i]: acc.append(acc2[j])
		await ctx.send(acc)
@bot.command()
async def Cartas(ctx, arg, arg2 = None):
	if not arg2: cont2 = False
	else:
		p = arg2.upper()
		if p == "PREMIUM": cont2= True 
	valor = arg.upper() 
	user = ctx.author
	await open_account1(user)
	users1 = await get_bank_data1()
	zi = users1[str(user.id)]["cuenta"]
	with open("rei.json", "w") as f:
		json.dump(users1,f)
	if zi != 2:
		cont = False
		cartas = ["0","0","0"]
		if cont2 == True: cartas = ["0","0","0","0","0","0"]
		if valor == "BRONCE":
			cont = True
			earnings = 70
			if cont2 == True: earnings = 120
			for i in range(0,len(cartas)):
				x = random.randint (1,101)
				if 1 <= x and x <= 50: cartas[i] = "Bronce"
				elif x <= 90: cartas[i] = "Bronce brillante"
				elif x <= 99: cartas[i] = "Plata"
				else: cartas[i] = "Plata brillante"
		elif valor == "PLATA": 
			cont = True
			earnings = 120
			if cont2 == True: earnings = 300
			for i in range(0,len(cartas)):
				x = random.randint (1,101)
				if 1 <= x and x <= 8: cartas[i] = "Bronce"
				elif x <= 24: cartas[i] = "Bronce brillante"
				elif x <= 64: cartas[i] = "Plata"
				elif x <= 94: cartas[i] = "Plata brillante"
				elif x <= 99: cartas[i] = "Oro"
				else: cartas[i] = "Oro brillante"
		elif valor == "NADA": 
			cont = True
			earnings = 0
			cartas = []
		elif valor == "ORO":
			cont = True
			earnings = 360
			if cont2 == True: earnings = 600
			for i in range(0,len(cartas)):
				x = random.randint (1,101)
				if 1 <= x and x <= 1: cartas[i] = "Bronce"
				elif x <= 6: cartas[i] = "Bronce brillante"
				elif x <= 14: cartas[i] = "Plata"
				elif x <= 30: cartas[i] = "Plata brillante"
				elif x <= 70: cartas[i] = "Oro"
				else: cartas[i] = "Oro brillante"
		elif valor == "ESPECIAL":
			cont = True
			earnings = 600
			if cont2 == True: earnings = 1000
			for i in range(0,len(cartas)):
				x = random.randint (1,101)
				if 1 <= x and x <= 1: cartas[i] = "Plata"
				elif x <= 10: cartas[i] = "Plata brillante"
				elif x <= 40: cartas[i] = "Oro"
				elif x <= 60: cartas[i] = "Oro brillante"
				else: cartas[i] = "Especial"
		else: await ctx.send("Invalido, debe ser Bronce, Plata u Oro.")
		if cont == True:
			await open_account(ctx.author)
			users = await get_bank_data()
			user = ctx.author
			if earnings > users[str(user.id)]["cuenta"]:
				await ctx.send("No tienes dinero suficiente")
			else:	
				users[str(user.id)]["cuenta"] -= earnings
				with open("zen.json", "w") as f:
					json.dump(users,f)
				for i in range (0,len(cartas)):
					if cartas[i] == "Especial": cartas[i] = random.choice(especial)
					if cartas[i] == "Oro brillante": cartas[i] = random.choice(orobrillante) 
					if cartas[i] == "Oro": cartas[i] = random.choice(oro)
					if cartas[i] == "Plata": cartas[i] = random.choice(plata)
					if cartas[i] == "Plata brillante": cartas[i] = random.choice(platabrillo)
					if cartas[i] == "Bronce": cartas[i] = random.choice(bronce)
					if cartas[i] == "Bronce brillante": cartas[i] = random.choice(broncebrillo)
				await open_account0(ctx.author)
				users0 = await get_bank_data0()
				user = ctx.author
				acc = users0[str(user.id)]["cuenta"]
				with open("cartas.json", "w") as f:
					json.dump(users0,f)
				acc = users0[str(user.id)]["cuenta"] 
				if acc[0] == "Nada": acc.remove("Nada")
				for i in range (0,len(cartas)):
					k = cartas[i]
					cont5= True
					for i in range (0,(len(acc)-1)):
						if cont5 == True:
								if k == acc[i]: 
									cont5 = False
									acc[i + 1] +=1
					if cont5 == True: 
						acc.append(k)
						acc.append(1)
					await ctx.send(k)
				users0[str(user.id)]["cuenta"] = acc
				with open("cartas.json", "w") as f:
					json.dump(users0,f)
				await open_account1(user)
				zi = users1[str(user.id)]["cuenta"]
				if zi == 0: zi = 1
				elif zi == 1: zi = 2 
				users1[str(user.id)]["cuenta"] = zi
				with open("rei.json", "w") as f:
					json.dump(users1,f)
				await ctx.send("Contactate con Rayuke, Misunderstood Human o DenCosmic por los codigos")
	else: await ctx.send("Ya compraste dos sobres hoy, espera a mañana")
@bot.command()
async def Help(ctx):
	embed = discord.Embed(title="Ayuda", desciption = "Los comandos del bot.")
	embed.add_field(name="-z cuenta", value= "Mirar tu cuenta de zenis.")
	embed.add_field(name="-z give <valor> @someone", value= "Dar zenis a otro usuario.") 
	embed.add_field(name="-z Cartas <valor> ", value ="Comprar cartas")
	embed.add_field(name="-z Album", value="Ver tu album de cartas")
	embed.add_field(name="-z give <carta> @someone Cartas", value="Dar una carta a otro usuario, si se quiere dar una carta con más de una palabra, esta debe ser escrita entre comillas")
	await ctx.send(content=None, embed=embed)
@bot.command()
async def help(ctx):
	embed = discord.Embed(title="Ayuda", desciption = "Los comandos del bot.")
	embed.add_field(name = "-z cuenta", value= "Mirar tu cuenta de zenis.")
	embed.add_field(name= "-z give <valor> @someone", value= "Dar zenis a otro usuario.") 
	embed.add_field(name="-z Cartas <valor> ", value ="Comprar cartas")
	embed.add_field(name="-z Album", value="Ver tu album de cartas")
	embed.add_field(name="-z give <carta> @someone Cartas", value="Dar una carta a otro usuario, si se quiere dar una carta con más de una palabra, esta debe ser escrita entre comillas")
	await ctx.send(content=None, embed=embed)
@bot.command()
async def cuenta(ctx, member: discord.Member= None):
	if member is None: 
		user = ctx.author
	else: user = member
	await open_account(user)
	users = await get_bank_data()
	cuenta_amt = users[str(user.id)]["cuenta"] 
	em = discord.Embed(title = f"{user.name}", color = discord.Color.red())
	em.add_field(name = "cuenta", value = cuenta_amt)
	await ctx.send(embed = em)
@bot.command()
async def Sello (ctx, arg, member : discord.Member):
	sello = "Nada"
	if ctx.author.id == 265725029902319616: sello = "Allez Studios"
	elif ctx.author.id == 263108593178509313: sello = "Dragon News"
	elif ctx.author.id == 721480105448177797 or ctx.author == 347201351543160834: sello = "Paint Express Z" 
	elif ctx.author.id == 439829989274157057: sello = "Arcade Studios"
	elif ctx.author.id == 498610422119923723: sello = "The Sparkling Key Studios"
	else: await ctx.send ("No eres dueño de un sello")
	if sello != "Nada":
		usuario2 = member
		await open_account(usuario2)
		users = await get_bank_data()
		earnings = int(arg)
		if earnings > users[str(sello)]["cuenta"]:
			await ctx.send("Invalido")
		else:
			if earnings > 0:
				await ctx.send("Transación completada")
				users[str(sello)]["cuenta"] -= earnings
				with open("zen.json", "w") as f:
					json.dump(users,f)
				users[str(usuario2.id)]["cuenta"] += earnings
				with open("zen.json", "w") as f:
					json.dump(users,f)
			else: 
				await ctx.send("Invalido")
@bot.command()
async def Par (ctx, arg):
	await open_account(ctx.author)
	users = await get_bank_data()
	user = ctx.author
	cont = False
	earnings = int(arg)
	earnings -= earnings % 10
	if earnings > users[str(user.id)]["cuenta"]:
		await ctx.send("Invalido")
	else:
		if earnings > 1001: cont = True
		x = random.randint(1,6)
		y = random.randint(1,6)
		await ctx.send(x)
		await ctx.send(y)
		z = x + y
		if z % 2 == 0:
			await ctx.send("Ganas")
			if cont == True:
				if earnings > 1009 and earnings < 4001: earnings *= 75
				elif earnings > 4009 and earnings < 10001: earnings *= 50 
				elif earnings > 10010 and earnings < 20001: earnings *= 25  
				else: earnings *= 10
				earnings /= 100
			earnings = int(earnings)
			users[str(user.id)]["cuenta"] += earnings
			with open("zen.json", "w") as f:
				json.dump(users,f)
		else: 	
			await ctx.send("Pierdes")
			users[str(user.id)]["cuenta"] -= earnings
			with open("zen.json", "w") as f:
				json.dump(users,f)
@bot.command()
async def Impar (ctx, arg):
	await open_account(ctx.author)
	users = await get_bank_data()
	user = ctx.author
	cont = False
	earnings = int(arg)
	earnings -= earnings % 10
	if earnings > users[str(user.id)]["cuenta"]:
		await ctx.send("Invalido")
	else:
		if earnings > 1001: cont = True
		x = random.randint(1,6)
		y = random.randint(1,6)
		await ctx.send(x)
		await ctx.send(y)
		z = x + y
		if z % 2 == 1:
			await ctx.send("Ganas")
			if cont == True:
				if earnings > 1009 and earnings < 4001: earnings *= 75
				elif earnings > 4009 and earnings < 10001: earnings *= 50 
				elif earnings > 10010 and earnings < 20001: earnings *= 25  
				else: earnings *= 10
				earnings /= 100
			earnings = int(earnings)
			users[str(user.id)]["cuenta"] += earnings
			with open("zen.json", "w") as f:
				json.dump(users,f)
		else: 	
			await ctx.send("Pierdes")
			users[str(user.id)]["cuenta"] -= earnings
			with open("zen.json", "w") as f:
				json.dump(users,f)
@bot.command()
async def pagar(ctx, arg, member : discord.Member):
	if ctx.author.id == 265725029902319616:
		await open_account(ctx.author)
		users = await get_bank_data()
		user = member
		earnings = int(arg)
		if earnings > 0: 
			await ctx.send("Pago completado")
		else: await ctx.send("Cobro completado")
		users[str(user.id)]["cuenta"] += earnings
		with open("zen.json", "w") as f:
			json.dump(users,f)
	else: await ctx.send("Solo la ama Kyylla puede usar este comando")
@bot.command()
async def give(ctx, arg, member : discord.Member, arg2 = None):
	cont2= True
	if not arg2: cont2 = False
	else:
		p = arg2.upper()
		if p == "CARTAS": cont2= True 
	usuario2 = member
	user = ctx.author
	if cont2 == False:
		await open_account(ctx.author)
		await open_account(usuario2)
		users = await get_bank_data()
		earnings = int(arg)
		if earnings > users[str(user.id)]["cuenta"]:
			await ctx.send("Invalido")
		else:
			if earnings > 0:
				await ctx.send("Transación completada")
				users[str(user.id)]["cuenta"] -= earnings
				with open("zen.json", "w") as f:
					json.dump(users,f)
				users[str(usuario2.id)]["cuenta"] += earnings
				with open("zen.json", "w") as f:
					json.dump(users,f)
			else: 
				await ctx.send("Invalido")
	elif cont2 == True:
		cont4 = False
		Cart = arg
		for i in range(0,99):
			if cont4 == False: 
				if Cart == i: cont4= True
		if cont4 == True: await ctx.send("No puedes dar eso, es un indicador")
		else: 
			await open_account0(ctx.author)
			await open_account0(usuario2)
			users = await get_bank_data0()
			users = await get_bank_data0()
			acc = users[str(user.id)]["cuenta"]
			acc2= users[str(usuario2.id)]["cuenta"]
			if acc[0] == "Nada": acc.remove("Nada")
			if acc2[0] == "Nada": acc2.remove("Nada")
			cont3= 0
			for j in range (0,(len(acc)-1)):
				if cont3 == 0:
					if acc[j] == Cart: 
						cont3 = 1
						cont5= True
						for i in range (0,(len(acc2)-1)):
							if cont5 == True:
								if Cart == acc2[i]: 
									cont5 = False
									acc2[i + 1] +=1
						if cont5 == True: 
							acc2.append(Cart)
							acc2.append(1)
						if acc[j+1] > 1:
							acc[j+1] -= 1
						else: 
							acc.pop(j +1)
							acc.remove(Cart)
			users[str(user.id)]["cuenta"] = acc
			users[str(usuario2.id)]["cuenta"] = acc2
			with open("cartas.json", "w") as f:
				json.dump(users,f)
			if cont3 == 1: await ctx.send("Transación completada")
			else:
				for k in range (0,len(todas)):
					if todas[k] == Cart: cont3 = 2
			if cont3 == 2: await ctx.send("No tienes esa carta")
			elif cont3 == 0: await ctx.send("Esa carta no existe")
			
async def open_account(user):
	users = await get_bank_data()
	if str(user.id) in users: 
		return False
	else:
		users[str(user.id)] = {}
		acc = [0]
		users[str(user.id)]["cuenta"] = acc
		with open("zen.json","w") as f:
			json.dump(users,f)
	return True
async def get_bank_data():
	with open("zen.json","r") as f:
		users = json.load(f)
	return (users)
async def open_account0(user):
	users = await get_bank_data0()
	if str(user.id) in users: 
		return False
	else:
		users[str(user.id)] = {}
		acc = ["Nada"]
		users[str(user.id)]["cuenta"] = acc
		with open("cartas.json","w") as f:
			json.dump(users,f)
	return True
async def get_bank_data0():
	with open("cartas.json","r") as f:
		users = json.load(f)
	return (users)
async def open_account1(user):
	users = await get_bank_data1()
	if str(user.id) in users: 
		return False
	else:
		users[str(user.id)] = {}
		users[str(user.id)]["cuenta"] = 0
		with open("rei.json","w") as f:
			json.dump(users,f)
	return True
async def get_bank_data1():
	with open("rei.json","r") as f:
		users = json.load(f)
	return (users)    
bot.run(TOKEN)