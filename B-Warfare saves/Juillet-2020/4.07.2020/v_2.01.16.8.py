#--------------------------------------------------------------------------#
#--------------------------------------------------------------------------#
#--------------------------------------------------------------------------#
#--------------------------------------------------------------------------#
#--------------------------------------------------------------------------#
#----------------------Crée par Antoine et Aurelien------------------------#
#-----------------------------v 2.01.16.8----------------------------------#
#--------------------------------------------------------------------------#
#--------------------------------------------------------------------------#
#--------------------------------------------------------------------------#
#--------------------------------------------------------------------------#

from discord.utils import get
import logging
import os
from os import path, mkdir
import asyncio
from itertools import cycle
import shutil
import typing
import random
from random import *
import time
import sqlite3
import json
import hashlib
import locale
from dataIO import fileIO
from getpass import getpass
try:
    from discord.ext import commands, tasks
    import discord
except ImportError:
    print("Discord.py is not installed. Please install it!")
    sys.exit(30)

locale.setlocale(locale.LC_TIME,'FR')

config_location = fileIO("assets/config/config.json", "load")
Shards = config_location["Shards"]
Prefix = config_location["Prefix"]
PASSWORD = config_location["PASSWORD"]

client = commands.AutoShardedBot(shard_count = Shards, command_prefix=Prefix)

#-----------------------PASSWORD-------------------------#
chaine_mot_de_passe = b'PASSWORD'
mot_de_passe_chiffre = hashlib.sha1(chaine_mot_de_passe).hexdigest()

verrouille = True
while verrouille:
    entre = getpass("Tapez le mot de passe : ")
    # encodage de la saisie pour avoir un type bytes
    entre = entre.encode()

    entre_chiffre = hashlib.sha1(entre).hexdigest()
    if entre_chiffre == mot_de_passe_chiffre:
        verrouille = False
    else:
        print("Mot de passe incorrect")

print("Mot de passe accepté..., please wait a few minute")
#-----------------------PASSWORD-------------------------#

starttime = time.time()

VS = 1.0

DIR = os.path.dirname(__file__)

os.chdir(r'C:\Users\33664\Desktop\B-Warfare')

status = cycle(['InterliX', 'v 2.01.16.8', 'RPG', '!help', time.strftime('%A %d/%m/%Y')])

db = sqlite3.connect(os.path.join(DIR, "BankAccounts.db"))

SQL = db.cursor()

client.remove_command('help')

XP = "XP"

LV = "LV"

PV = ":heart:"

Defence = ":shield:"

Force = ":crossed_swords:"

Mana = ":alembic:"

Pierre = "Pierre"

Charbon = "Charbon"

Fer = "Fer"

Cuivre = "cuivre"

Cobalt = "Cobalt"

Gold= "Or"

Platine = "Platine"

Diamant = "Diamant💎"

Paladium = "Paladium"

obsidienne = "obsidienne"

Coin = "Piece"

START_BALANCE = 100.00

s0 = 0.0

s1 = 1.0

s5 = 5.0

s10 = 10.0

s20 = 20.0

VICTOIRE = "https://media.discordapp.net/attachments/715674715519451206/716096815224717332/VICTOIRE.jpg?width=254&height=405"


@client.event
async def on_ready():
    change_status.start()
    print('Tu est connecté sur {0.user}'.format(client))

@client.event
async def on_command(command):
	info = fileIO("assets/config/config.json", "load")
	info["Commands_used"] = info["Commands_used"] + 1
	fileIO("assets/config/config.json", "save", info)

@client.event
async def on_member_join(member):
    USER_ID = member.id
    USER_NAME = str(member)

    SQL.execute('create table if not exists Accounts("Num" integer primary key autoincrement, "user_name" text, "user_id" integer NOT NULL, "Pierre" REAL, "Charbon" REAL, "Fer" REAL, "Cuivre" REAL, "Cobalt" REAL, "Gold" REAL,"Platine" REAL, "Diamant" REAL, "Paladium" REAL, "obsidienne" REAL, "Coin" REAL)')
    SQL.execute(f'select user_id from Accounts where user_id="{USER_ID}"')
    result_userID = SQL.fetchone()

    if result_userID is None:
        SQL.execute('insert into Accounts(user_name, user_id, Pierre, Charbon, Fer, Cuivre, Cobalt, Gold, Platine, Diamant, Paladium, obsidienne, Coin) values(?,?,?,?,?,?,?,?,?)', (USER_NAME, USER_ID, START_BALANCE, s0, s0, s0, s0, s0, s0, s0, s0, s0, s0))
        db.commit()

    SQL.execute('create table if not exists consommable("Num" integer primary key autoincrement, "user_name" text, "user_id" integer NOT NULL, "XP" REAL, "LV" REAL, "MaxMana" REAL, "Mana" REAL, "Heal" REAL, "MaxHeal" REAL, "Force" REAL, "Defence" REAL)')
    SQL.execute(f'select user_id from consommable where user_id="{USER_ID}"')
    result_userID = SQL.fetchone()

    if result_userID is None:
        SQL.execute('insert into consommable(user_name, user_id, XP, LV, MaxMana, Mana, Heal, MaxHeal, Force, Defence) values(?,?,?,?,?,?,?,?,?,?)',(USER_NAME, USER_ID, s1, s1, s20, s5, s20, s20, s1, s1))
        db.commit()

    SQL.execute('create table if not exists industrie("Num" integer primary key autoincrement,"user_name" text, "user_id" integer NOT NULL, "Mine_Pierre" REAL, "Mine_Fer" REAL)')
    SQL.execute(f'select user_id from industrie where user_id="{USER_ID}"')
    result_userID = SQL.fetchone()

    if result_userID is None:
        SQL.execute('insert into industrie(user_name, user_id, Mine_Pierre, Mine_Fer,) values(?,?,?,?)', (USER_NAME, USER_ID, s0, s0,))
        db.commit()

    await member.create_dm()
    await member.dm_channel.send(f'Salut {member.name},bienvenue sur le serveur Discord! je te dit de faire !start dans le salon commande')

@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx,user : discord.User, *reason):
    reason = " ".join(reason)
    await ctx.guild.kick(user, reason = reason)
    await ctx.send(f"{user} à été kick.")

@tasks.loop(seconds=60)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.command()
async def ping(ctx):
    await ctx.send(f'mon ping est de {round(client.latency * 1000)}ms')

@client.command()
async def start(ctx):
    USER_ID = ctx.message.author.id
    USER_NAME = str(ctx.message.author)
    await ctx.channel.send(f'Bienvenue {ctx.message.author.mention}, je me prénomme X Æ A-Xii et je serai ton parrain pour ton aventure, nous sommes en 3025, suite à une guerre bactériologique. 98 % De la population mondiale a succombé, les machines on donc commencé à vouloir prendre le pouvoir, à vous de les en empêcher. Pour commencer je te propose de faire la commande !mine pour miner puis tu peut faire la commande !i pour ouvrir ton inventaire.')
    await asyncio.sleep(3)
    await ctx.message.delete()

    SQL.execute('create table if not exists Accounts("Num" integer primary key autoincrement, "user_name" text, "user_id" integer NOT NULL, "Pierre" REAL, "Charbon" REAL, "Fer" REAL, "Cuivre" REAL, "Cobalt" REAL, "Gold" REAL,"Platine" REAL, "Diamant" REAL, "Paladium" REAL, "obsidienne" REAL, "Coin" REAL)')
    SQL.execute(f'select user_id from Accounts where user_id="{USER_ID}"')
    result_userID = SQL.fetchone()

    if result_userID is None:
        SQL.execute('insert into Accounts(user_name, user_id, Pierre, Charbon, Fer, Cuivre, Cobalt, Gold, Platine, Diamant, Paladium, obsidienne, Coin) values(?,?,?,?,?,?,?,?,?)',(USER_NAME, USER_ID, START_BALANCE, s0, s0, s0, s0, s0, s0, s0, s0, s0, s0))
        db.commit()

    SQL.execute('create table if not exists consommable("Num" integer primary key autoincrement, "user_name" text, "user_id" integer NOT NULL, "XP" REAL, "LV" REAL, "MaxMana" REAL, "Mana" REAL, "Heal" REAL, "MaxHeal" REAL, "Force" REAL, "Defence" REAL)')
    SQL.execute(f'select user_id from consommable where user_id="{USER_ID}"')
    result_userID = SQL.fetchone()

    if result_userID is None:
        SQL.execute('insert into consommable(user_name, user_id, XP, LV, MaxMana, Mana, Heal, MaxHeal, Force, Defence) values(?,?,?,?,?,?,?,?,?,?)',(USER_NAME, USER_ID, s1, s1, s20, s5, s20, s20, s1, s1))
        db.commit()

    SQL.execute('create table if not exists industrie("Num" integer primary key autoincrement,"user_name" text, "user_id" integer NOT NULL, "Mine_Pierre" REAL, "Mine_Fer" REAL)')
    SQL.execute(f'select user_id from industrie where user_id="{USER_ID}"')
    result_userID = SQL.fetchone()

    if result_userID is None:
        SQL.execute('insert into industrie(user_name, user_id, Mine_Pierre, Mine_Fer,) values(?,?,?,?)', (USER_NAME, USER_ID, s0, s0,))
        db.commit()

    SQL.execute(f'select Mana from consommable where user_id="{USER_ID}"')
    result_userbal = SQL.fetchone()

    SQL.execute(f'select MaxMana from consommable where user_id="{USER_ID}"')
    result_userbal1 = SQL.fetchone()

    while result_userbal < result_userbal1 :
        SQL.execute(f'update consommable set Mana = Mana + 1 where user_id="{USER_ID}"')
        db.commit()
        time.sleep(10)
    pass

@client.command()
async def select(ctx):
    await ctx.channel.send(f'{VICTOIRE}')

@client.command()
async def credits(ctx):
    embed = discord.Embed(
    title = f"Credits",
    color = 0xe0ff00
    )

    embed.add_field(name="Developpeurs",value="Λητθιηε & AUR3MY")

    embed.set_footer(text=time.strftime('%A %d/%m/%Y %H:%M:%S'))

    await ctx.channel.send(embed=embed)

@client.command()
async def mine(ctx):
    USER_ID = ctx.message.author.id
    USER_NAME = str(ctx.message.author)

    SQL.execute(f'select Mana from consommable where user_id="{USER_ID}"')

    SQL.execute(f'update consommable set Mana = Mana - Mana where user_id="{USER_ID}"')

    result_userbal = SQL.fetchone()

@client.command()
async def entreprise(ctx):
    await ctx.channel.send('cette commande arrivera dans les prochain jour')
    await asyncio.sleep(3)
    await ctx.message.delete()

@client.command()
async def daily(ctx):
    DailyC = randint(100,1000)
    DailyX = randint(700,1500)
    USER_ID = ctx.message.author.id
    USER_NAME = str(ctx.message.author)

    SQL.execute(f'select Coin from Accounts where user_id="{USER_ID}"')

    SQL.execute(f'update Accounts set Coin = Coin + {DailyC} where user_id="{USER_ID}"')
    db.commit()
    result_userbal = SQL.fetchone()

    SQL.execute(f'select XP from consommable where user_id="{USER_ID}"')

    SQL.execute(f'update consommable set XP = XP + {DailyX} where user_id="{USER_ID}"')
    db.commit()
    result_userbal1 = SQL.fetchone()

    await ctx.send(f"{ctx.message.author.mention} tu gagne {DailyC} {Coin} et {DailyX} {XP}.")

@client.command()
async def info(ctx):
    server = ctx.guild
    numberOfTextChannels = len(server.text_channels)
    numberOfVoiceChannels = len(server.voice_channels)
    serverDescription = server.description
    numberOfPerson = server.member_count
    serverName = server.name

    embed = discord.Embed(
    title=f"information sur B-Warfare",
    color = 0x00FFB2
    )

    embed.add_field(name="Créateur",value=f"Λητθιηε#8330 / AUR3MY#3201",inline=True)

    embed.add_field(name="Version",value=f"v 2.01.16.8",inline=True)

    embed.add_field(name="Langage de programmation",value=f"Python/python",inline=True)

    embed.add_field(name="API",value=f"Non disponible",inline=True)

    embed.add_field(name="joueur",value=f"{numberOfPerson}",inline=True)

    embed.add_field(name="channels vocaux",value=f"{numberOfVoiceChannels}",inline=True)

    embed.add_field(name="channels textuels",value=f"{numberOfTextChannels}",inline=True)

    embed.add_field(name="Shards", value=f"{Shards}", inline=True)

    embed.set_footer(text=time.strftime('%A %d/%m/%Y %H:%M:%S'))

    await ctx.channel.send(embed=embed)

@client.command()
async def help(ctx):
    embed = discord.Embed(
	title=f"Commande principale de B-Warfare",
	color = 0x2eff00
	)

    embed.add_field(name="!start",value=f"commence ton aventure",inline=False)

    embed.add_field(name="!i",value=f"ouvre ton inventaire",inline=False)

    embed.add_field(name="!mine",value=f"Mine des minéraux",inline=False)

    embed.add_field(name="!daily",value=f"Reçois ton argent quotidiennement",inline=False)

    embed.add_field(name="!info",value=f"Donne des information sur le serveur",inline=False)

    embed.add_field(name="!ping",value=f"Ping du bot",inline=False)

    embed.add_field(name="!kick",value=f"Kick les joueur toxic",inline=False)

    embed.add_field(name="!credits",value=f"Credits",inline=False)

    embed.set_footer(text=time.strftime('%A %d/%m/%Y %H:%M:%S'))

    await ctx.channel.send(embed=embed)

@client.command()
async def i(ctx,):
    USER_ID = ctx.message.author.id
    USER_NAME = str(ctx.message.author)

    SQL.execute('create table if not exists Accounts("Num" integer primary key autoincrement, "user_name" text, "user_id" integer NOT NULL, "Pierre" REAL, "Charbon" REAL, "Fer" REAL, "Cuivre" REAL, "Cobalt" REAL, "Gold" REAL,"Platine" REAL, "Diamant" REAL, "Paladium" REAL, "obsidienne" REAL, "Coin" REAL)')
    SQL.execute(f'select user_id from Accounts where user_id="{USER_ID}"')
    result_userID = SQL.fetchone()

    if result_userID is None:
        SQL.execute('insert into Accounts(user_name, user_id, Pierre, Charbon, Fer, Cuivre, Cobalt, Gold, Platine, Diamant, Paladium, obsidienne, Coin) values(?,?,?,?,?,?,?,?,?)', (USER_NAME, USER_ID, START_BALANCE, s0, s0, s0, s0, s0, s0, s0, s0, s0, s0))
        db.commit()

    SQL.execute('create table if not exists consommable("Num" integer primary key autoincrement, "user_name" text, "user_id" integer NOT NULL, "XP" REAL, "LV" REAL, "MaxMana" REAL, "Mana" REAL, "Heal" REAL, "MaxHeal" REAL, "Force" REAL, "Defence" REAL)')
    SQL.execute(f'select user_id from consommable where user_id="{USER_ID}"')
    result_userID = SQL.fetchone()

    if result_userID is None:
        SQL.execute('insert into consommable(user_name, user_id, XP, LV, MaxMana, Mana, Heal, MaxHeal, Force, Defence) values(?,?,?,?,?,?,?,?,?,?)', (USER_NAME, USER_ID, s1, s1, s20, s5, s20, s20, s1, s1))
        db.commit()

    embed = discord.Embed(
	title=f"inventaire de {USER_NAME}",
	color = 0xFFD801
	)

    SQL.execute(f'select Pierre from Accounts where user_id="{USER_ID}"')
    result_userbal = SQL.fetchone()

    embed.add_field(name="Pierre",value=f"{result_userbal[0]} {Pierre}",inline=True)

    SQL.execute(f'select Charbon from Accounts where user_id="{USER_ID}"')
    result_userbal = SQL.fetchone()

    embed.add_field(name="Charbon",value=f"{result_userbal[0]} {Charbon}",inline=True)

    SQL.execute(f'select Fer from Accounts where user_id="{USER_ID}"')
    result_userbal = SQL.fetchone()

    embed.add_field(name="Fer",value=f"{result_userbal[0]} {Fer}",inline=True)

    SQL.execute(f'select Cuivre from Accounts where user_id="{USER_ID}"')
    result_userbal = SQL.fetchone()

    embed.add_field(name="Cuivre",value=f"{result_userbal[0]} {Cuivre}",inline=True)

    SQL.execute(f'select Cobalt from Accounts where user_id="{USER_ID}"')
    result_userbal = SQL.fetchone()

    embed.add_field(name="Cobalt", value=f"{result_userbal[0]} {Cobalt}", inline=True)

    SQL.execute(f'select Gold from Accounts where user_id="{USER_ID}"')
    result_userbal = SQL.fetchone()

    embed.add_field(name="or", value=f"{result_userbal[0]} {Gold}", inline=True)

    SQL.execute(f'select Platine from Accounts where user_id="{USER_ID}"')
    result_userbal = SQL.fetchone()

    embed.add_field(name="Platine",value=f"{result_userbal[0]} {Platine}",inline=True)

    SQL.execute(f'select Diamant from Accounts where user_id="{USER_ID}"')
    result_userbal = SQL.fetchone()

    embed.add_field(name="Diamant",value=f"{result_userbal[0]} {Diamant}",inline=True)

    SQL.execute(f'select Paladium from Accounts where user_id="{USER_ID}"')
    result_userbal = SQL.fetchone()

    embed.add_field(name="Paladium", value=f"{result_userbal[0]} {Paladium}", inline=True)

    SQL.execute(f'select Obsidienne from Accounts where user_id="{USER_ID}"')
    result_userbal = SQL.fetchone()

    embed.add_field(name="Obsidienne", value=f"{result_userbal[0]} {obsidienne}", inline=True)

    SQL.execute(f'select Coin from Accounts where user_id="{USER_ID}"')
    result_userbal = SQL.fetchone()

    embed.add_field(name="Coin",value=f"{result_userbal[0]} {Coin}",inline=True)

    embed.set_thumbnail(url="https://media.discordapp.net/attachments/668182697335848975/714214889178005546/sac.gif")

    embed.set_footer(text=time.strftime('%A %d/%m/%Y %H:%M:%S'))

    await ctx.channel.send(embed=embed)

    embed = discord.Embed(
	title=f"Consommable de {USER_NAME}",
	color = 0xFFD801
	)

    SQL.execute(f'select XP from consommable where user_id="{USER_ID}"')
    result_userbal = SQL.fetchone()

    SQL.execute(f'select LV from consommable where user_id="{USER_ID}"')
    result_userbal1 = SQL.fetchone()

    embed.add_field(name="LV/XP",value=f"{result_userbal1[0]} {LV}/({result_userbal[0]} {XP})",inline=True)

    SQL.execute(f'select Mana from consommable where user_id="{USER_ID}"')
    result_userbal = SQL.fetchone()

    SQL.execute(f'select MaxMana from consommable where user_id="{USER_ID}"')
    result_userbal1 = SQL.fetchone()

    embed.add_field(name="Mana",value=f"{result_userbal[0]}/{result_userbal1[0]} {Mana}",inline=True)

    SQL.execute(f'select Heal from consommable where user_id="{USER_ID}"')
    result_userbal = SQL.fetchone()

    SQL.execute(f'select MaxHeal from consommable where user_id="{USER_ID}"')
    result_userbal1 = SQL.fetchone()

    embed.add_field(name="PV",value=f"{result_userbal[0]}/{result_userbal1[0]} {PV}",inline=True)

    SQL.execute(f'select Force from consommable where user_id="{USER_ID}"')
    result_userbal = SQL.fetchone()

    embed.add_field(name="Force",value=f"{result_userbal[0]} {Force}",inline=True)

    SQL.execute(f'select Defence from consommable where user_id="{USER_ID}"')
    result_userbal = SQL.fetchone()

    embed.add_field(name="Defence",value=f"{result_userbal[0]} {Defence}",inline=True)

    embed.set_thumbnail(url="")

    embed.set_footer(text=time.strftime('%A %d/%m/%Y %H:%M:%S'))

    await ctx.channel.send(embed=embed)

@client.command()
async def industrie(ctx):
    USER_ID = ctx.message.author.id
    USER_NAME = str(ctx.message.author)
    embed = discord.Embed(
	title=f"industrie de {USER_NAME}",
	color = 0xFFD801
	)

    SQL.execute(f'select Mine_Pierre from industrie where user_id="{USER_ID}"')
    result_userbal = SQL.fetchone()

    embed.add_field(name="Mine de Pierre",value=f"{result_userbal[0]} Mine de Pierre",inline=True)

    SQL.execute(f'select Mine_Fer from industrie where user_id="{USER_ID}"')
    result_userbal = SQL.fetchone()

    embed.add_field(name="Mine de Fer",value=f"{result_userbal[0]} Mine de Fer",inline=True)

    embed.set_thumbnail(url="https://media.discordapp.net/attachments/668182697335848975/714214889178005546/sac.gif")

    embed.set_footer(text=time.strftime('%A %d/%m/%Y %H:%M:%S'))

    await ctx.channel.send(embed=embed)

@client.command(aliases=['8ball', 'test'])
async def  bdc(ctx, *, question):
    responses = [
            "j'en suis sûre.",
            "Il en est décidément ainsi.",
            "Sans aucun doute.",
            "Oui définitivement.",
            "Vous pouvez vous y fier.",
            "Comme je le vois oui.",
            "Bonne perspective.",
            "oui.",
            "non.",
            "Mieux vaut ne pas te le dire maintenant.",
            "Ne compte pas là-dessus.",
            "Ma réponse est non.",
            "Mes sources disent non..",
            "va te faire foutre",
            "bah vien on se bagarre",
            "peut tu mieu écrire crasseux",
            "je ne rigole pas avec toi sa risque de déraper",
            "Les perspectives ne sont pas si bonnes.",
            "au lieu de parler paye moi un paninis Nutella.",
            "Très douteux."]
    embed = discord.Embed(
        title = 'Boule de crystal',
        description = 'pose une question avec .bdc et il va te repondre.',
        color = 0xFFD800
    )

    embed.set_footer(text='ba la ya pas encore')

    embed.set_thumbnail(url='')

    embed.add_field(name=f'Question: {question}', value=f'reponse: {random.choice(responses)}', inline=True)

    embed.set_footer(text=time.strftime('%A %d/%m/%Y %H:%M:%S'))

    await ctx.channel.send(embed=embed)

client.run('NjY4ODc2NjI3MjI4NDkxNzg5.Xv40wA.pOmJtnjteCVBsTC252rPHOT0uPU')

#crée par λητθιηε#8330 et aur3my#3201 copyright par InterliX
