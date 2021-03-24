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
bot.remove_command("help")
os.chdir("https://github.com/Kyyla/DBFW-Bot")
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


#@bot.command()
#async def tomar muchas palabras en una varriable (ctx,*,persona):
#	await ctx.send(str(persona)+" 5 last suprise")
@bot.command()
async def rol (ctx,arg,arg2= None, arg3=None, arg4=None, arg5=None):
	if not arg:
		await ctx.send("Ingrese el nombre del rol a obtener")
	rem = False
	if not arg2 and not arg3 and not arg4:
		arg = str(arg) 
	elif not arg3 and not arg4:
		if arg2.upper() == "REMOVE":
			rem = True
		else:
			arg = str(arg) + " "+ str (arg2)
	elif not arg4:
		if arg3.upper() == "REMOVE":
			rem = True
		else:
			arg = str(arg) + " "+ str (arg2) + " " + str(arg3)
	else: 
		if arg4.upper() == "REMOVE":
			rem = True
		else:
			arg = str(arg) + " "+ str (arg2) + " " + str(arg3) + " " + str(arg4)
	arg = arg.upper()
	if arg == "PARTICIPANTE DEL TORNEO" or arg == "PARTICIPANTE" or arg == "EVENTOS":
		user = ctx.author
		role = get(user.guild.roles,name = ROLE2)
		if rem == False:
			await user.add_roles(role)
		elif rem == True:
			await user.remove_roles(role)
	elif rem == False:
		await ctx.send("Este no es un rol valido")
@bot.command()
async def Wiki (ctx, arg= None, *, arg2=None):
	if arg is None:
		await ctx.send("https://dragonballfanon.fandom.com/es/wiki/Dragon_Ball_Fanon_Wiki")
	elif arg.upper() == "ZENIS":
		await ctx.send("https://dragonballfanon.fandom.com/es/wiki/Proyectos/Zenis")
	elif arg.upper() == "BÚSQUEDA" or arg.upper() == "BUSQUEDA":
		if arg2 is None:
			await ctx.send("Debes colocar un árticulo para buscar")
		else:
			buscar = "https://dragonballfanon.fandom.com/es/wiki/" + str(arg2)
			buscar = buscar.replace(" ", "_")
			await ctx.send(buscar)
	elif arg.upper() == "EVENTO" or arg.upper() == "EVENTOS":
		await ctx.send("https://dragonballfanon.fandom.com/es/wiki/Usuario_Blog:Rayuke/3º_Torneo_Fanon_del_Poder_-_Novena_Ronda")
	elif arg.upper() == "CALENDARIO":
		await ctx.send("https://dragonballfanon.fandom.com/es/wiki/Dragon_Ball_Fanon_Wiki:Calendario")

@bot.command()
async def TDP (ctx, *, objeto):
	objeto = objeto.upper()
	if objeto == "NUBE VOLADORA" or objeto == "BLADE" or objeto == "BLADELLAMARADAAZUL":
		await ctx.send("Permite al poseedor saltar su respectivo combate, ni habrá ganador ni perdedor.")
	elif objeto == "CAPSULA ESPACIAL" or objeto == "CÁPSULA ESPACIAL" or objeto == "CABE" or objeto == "CABE SSJ":
		await ctx.send ("Te brinda la posibilidad de que otro universo te reemplace en tu combate, dicho universo a reemplazar sera elegido de manera aleatoria.")
	elif objeto == "ARMADURA SAIYAJIN" or objeto == "DENCOSMIC" or objeto == "COSMIC":
		await ctx.send("Imposibilita que tu universo sea seleccionado para combatir durante 3 rondas.")
	elif objeto == "SEMILLAS SAIBAIMAN" or objeto == "SEMILLAS" or objeto == "KYYLLA" or objeto == "SPEEDY":
		await ctx.send("Te permite añadir un cuarto (o quinto) combate a la jornada, en el cual puedes retar directamente a un universo, ambos universos son libres de elegir a cualquiera de sus personajes.")	
	elif objeto == "ESFERAS DEL DRAGÓN" or objeto == "ESFERAS DEL DRAGON" or objeto == "TYSON" or objeto == "TYSON-KUN": 
		await ctx.send("Te permite reemplazar el personaje del universo rival.")
	elif objeto == "ESFERAS DEL DRAGÓN NAMEKIANAS" or objeto== "ESFERAS DEL DRAGON NAMEKIANAS" or objeto== "CIF":
		await ctx.send("El usuario acreedor de las Esferas del Dragón pertenecientes al Planeta Namek, tendrá la posibilidad de reemplazar la modalidad de un combate en el cual participe, esto sin importar si participa en un combate especial o no, en caso de que que sea seleccionado un combate en el cual participen mas de 2 guerreros, el resto serán elegidos nuevamente mediante sorteo.")
	elif objeto== "SUPER ESFERAS DEL DRAGON" or objeto== "SUPER ESFERAS DEL DRAGÓN" or objeto== "STING":
		await ctx.send("Quien sea el poseedor de las Super Esferas, tendrá la posibilidad de restablecer a alguno de sus personajes caído en una batalla previa.")	
	elif objeto== "CELDA DE LUZ" or objeto == "OMEGA" or objeto == "OMEGA76":
		await ctx.send("La celda de luz (técnica de Freezer) te brinda la posibilidad de reemplazar algún combate, por uno en el que el puede elegir los universos que combatirán.")
	elif objeto== "CAMBIO" or objeto== "SAAIL" or objeto== "SAAIL GOX":
		await ctx.send("La técnica característica de Ginyu, permite a su poseedor intercambiar lugar en un combate ya establecido (uno en el cual no participe), remplazando a uno de los personajes de dicho combate por uno propio.")		
	elif objeto == "JOVEN BROLY" or objeto == "KYO" or objeto == "KYOMIST":
		await ctx.send("Si fuiste seleccionado para combatir Joven Broly, te permite evitar dicho combate y elegir tu reemplazo, esto a cambio de la eliminación de otro de tus personajes.")
	elif objeto== "TELETRANSPORTACIÓN" or objeto == "TELETRANSPORTACION" or objeto == "TRIVAGO" or objeto == "TRI" or objeto == "TRIVAGO SHIPPUDEN":
		await ctx.send("En caso de ser seleccionado para combatir, te permite intercambiar lugar con otro universo también seleccionado para combatir.")
	elif objeto == "MAFUBA" or objeto == "KANDA" or objeto == "KANDA21":
		await ctx.send("Quien pueda hacer uso del Mafuba, puede impedir el uso de un personaje de un universo a su elección, durante tres rondas (en las que haya sido seleccionado el universo afectado), en consecuencia, el universo que utilice dicha técnica, tendrá que inhabilitar uno de sus personajes durante dos rondas (en las que haya sido seleccionado el universo portador del objeto).")
	elif objeto== "OCARINA DE TAPION" or objeto== "NIKO" or objeto =="RAYUKE":
		await ctx.send("Imposibilita la edición del articulo de tu rival, desde el punto en que fue usada, hasta el final de la ronda en cuestión.")			
	elif objeto== "OJO DE NZHN (VSS-8)" or objeto== "OJO DE NZHN" or objeto== "VSS-8" or objeto == "GOKUTA" or objeto == "GOKUTAAS97":
		await ctx.send("Su uso causa que en un combate tu rival tenga que elegir personaje antes que vos, en caso de que el rival no elija personaje, el usuario del objeto puede elegir qué personaje rival debe participar del combate.")
	elif objeto== "MÁQUINA DEL TIEMPO" or objeto== "MAQUINA DEL TIEMPO" or objeto== "MAKA" or objeto== "SACERDOTE DE LANCE":
		await ctx.send("Te permite trasladar un combate del que participes a una ronda siguiente.")
	else:
		await ctx.send("Este no es un objeto")
@bot.command()
async def artista (ctx, arg = None, *, arg2 = None):
	if arg is None:
		await ctx.send("Escribir \"-z artista help\" para ver los comandos")
	elif arg.upper() == "HELP":
		embed = discord.Embed(title="Ayuda", desciption = "Los comandos de Artista.")
		embed.add_field(name="-z artista unirse <rol>", value= "Permite unirse al plan artista con un rol especifico (creador de logos, personajes, musica, etc).") 
		embed.add_field(name = "-z artista disponible/ocupado", value= "Solo para artistas afiliados, permite cambiar el estado a disponibl u ocupado")
		embed.add_field(name="-z afiliados", value ="Muestra una lista de los artistas en el proyecto, y su disponibilidad.")
		embed.add_field(name= "-z disponibilidad", value = "Igual que afiliados, con la diferencia de mostrar solo quienes esten disponibles")
		embed.add_field(name= "-z pedido <cantidad de dinero> <@artista><descripción>", value= "Envia un pedido al artista en cuestión")
		embed.add_field(name= "-z artista pendientes",value = "Solo para artistas afiliados, muestra los pedidos sin aceptar")
		embed.add_field(name = "-z arista rechazar/aceptar <número del pedido>", value= "Permite rechazar o aceptar algún pedido")
		embed.add_field(name= "-z artista aceptados", value = "Solo para artistas afiliados, permite ver los pedidos aceptados sin terminar")
		embed.add_field(name="-z artista completado <número del pedido>", value="Solo para artistas afiliados, elimina un pedido de la lista de aceptados, y cobra el dinero automaticamente")
		embed.add_field(name="-z give <carta> @someone Cartas", value="Dar una carta a otro usuario, si se quiere dar una carta con más de una palabra, esta debe ser escrita entre comillas")
		await ctx.send(content=None, embed=embed)
	elif arg.upper() == "UNIRSE" and arg2 is None:
		await ctx.send("Debes colocar en que te especializas ")
	#elif arg.upper() == "UNIRSE"and arg2 is not None:

@bot.command()
async def sorteo(ctx):
	user = ctx.author
	with open("membresias.json","r") as f:
		users = json.load(f)
	with open("zen.json", "r") as f:
		users2= json.load(f)
	if str(user.id) in users: 
		x = users[str(user.id)]["disponibles"]
		if users[str(user.id)]["comprados"] != x:
			users[str(user.id)]["comprados"] +=1
			with open("membresias.json", "w") as f:
				json.dump(users,f)
			await ctx.send("Bienvenido al sorteo")
			users2[str(user.id)]["cuenta"]-=50
			with open("zen.json", "w") as f:
				json.dump(users2,f)
		elif users[str(user.id)]["comprados"] == x:
			await ctx.send("No puedes comprar más cupos")
	else:
		await ctx.send("Deberías considerar comprar una Membresía")

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
async def HELP(ctx):
	embed = discord.Embed(title="Ayuda", desciption = "Los comandos del bot.")
	embed.add_field(name="-z cuenta", value= "Mirar tu cuenta de zenis.")
	embed.add_field(name="-z give <valor> @someone", value= "Dar zenis a otro usuario.") 
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
	rol_amt = users[str(user.id)]["rol"]
	if rol_amt is None:
		rol_amt = "Normal"
	if rol_amt == "Premium":
		em = discord.Embed(title = f"{user.name}, Usuario Premium", color = discord.Color.red())
	else: 
		em = discord.Embed(title = f"{user.name}", color = discord.Color.red())
	em.add_field(name = "Cuenta", value = cuenta_amt)
	await ctx.send(embed = em)
#def mayor (x,acc):
#	for j in range (if x > acc):
#		if x > acc[j]:

@bot.command()
async def top (ctx):
	maximo = [0,1,2,3,4,5,6,7,8,9]
	with open("zen.json","r") as f:
		users = json.load(f)
	for i in users:
		print (users[i]["cuenta"])

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
		#impar = [1,3,5]
		#par = [2,4,6]
		#x = random.choice(impar)
		#y = random.choice(par)
		#xyz = random.randint(1,2)
		#if xyz == 1:
		#	await ctx.send(y)
		#	await ctx.send(x)
		#else:
		y = random.randint(1,6)
		x = random.randint(1,6)
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
	if ctx.author.id == 315221475051307028:
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
	else: await ctx.send("Solo la tesorería puede usar este comando")
@bot.command()
async def robar(ctx):
	user = ctx.author
	await open_account(ctx.author)
	users = await get_bank_data()
	users[str(user.id)]["cuenta"] -= int(50)
	with open("zen.json", "w") as f:
		json.dump(users,f)
	await ctx.send("Fallaste en el robo, perdiste 50z")			
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
		users[str(user.id)]["cuenta"] = 0
		users[str(user.id)]["rol"] = "Normal"
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
bot.run(token)
