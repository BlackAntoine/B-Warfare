#crée par λητθιηε#8330 et aur3my#3201 copyright par InterliX

import discord
from discord.ext import commands, tasks
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

locale.setlocale(locale.LC_TIME,'FR')

print(time.strftime('%A %d/%m/%Y %H:%M:%S'))

DIR = os.path.dirname(__file__)

os.chdir(r'C:\Users\Administrateur\Desktop\B-Warfare')

status = cycle(['InterliX', 'v 2.01.16.8', 'RPG', '!help', time.strftime('%A %d/%m/%Y')])

client = commands.Bot(command_prefix="!")

db = sqlite3.connect(os.path.join(DIR, "BankAccounts.db"))

SQL = db.cursor()

client.remove_command('help')

XP ="XP"

Coin = "Piece"

Pierre = "Pierre"

Charbon = "Charbon"

Fer = "Fer"

Or = "Or"

Diamant = "Diamant💎"

obsidienne = "obsidienne"

START_BALANCE = 100.00

s0 = 0.0

s1 = 1.0

s5 = 5.0

s10 = 10.0



VICTOIRE = "https://media.discordapp.net/attachments/715674715519451206/716096815224717332/VICTOIRE.jpg?width=254&height=405"

#SQL.execute(f'select Mana from consommable where user_id="{USER_ID}"')
#Mana = SQL.fetchone()
#SQL.execute(f'select MaxMana from consommable where user_id="{USER_ID}"')
#MaxMana = SQL.fetchone()
#if Mana < MaxMana :
    #SQL.execute(f'update consommable set Mana = Mana + 1 where user_id="{USER_ID}"')
    #db.commit()

#def community_report(guild):
    #online = 0
    #idle = 0
    #offline = 0

    #for m in guild.members:
        #if str (m.status) == "online":
            #online += 1
        #if str (m.status) == "offline":
            #offline += 1
        #else:
            #idle += 1
    #return online, idle, offline

@client.command()
async def player(ctx):
    online, idle, offline = community_report()

    await message.channel.send(f"'''Online:{online}. Offline:{offline}. idle:{idle}")

@client.event
async def on_ready():
    change_status.start()
    print('Tu est connecté sur {0.user}'.format(client))

@client.event
async def on_member_join(member):
    USER_ID = member.id
    USER_NAME = str(member)

    SQL.execute('create table if not exists Accounts("Num" integer primary key autoincrement,"user_name" text, "user_id" integer NOT NULL, "Pierre" REAL, "Charbon" REAL, "Fer" REAL, "Gold" REAL, "Diamant" REAL, "obsidienne" REAL, "Coin" REAL)')
    SQL.execute(f'select user_id from Accounts where user_id="{USER_ID}"')
    result_userID = SQL.fetchone()

    if result_userID is None:
        SQL.execute('insert into Accounts(user_name, user_id, Pierre, Charbon, Fer, Gold, Diamant, obsidienne, Coin) values(?,?,?,?,?,?,?,?,?)', (USER_NAME, USER_ID, START_BALANCE, s0, s0, s0, s0, s0, s0))
        db.commit()

    SQL.execute('create table if not exists consommable("Num" integer primary key autoincrement,"user_name" text, "user_id" integer NOT NULL, "Mana" REAL)')
    SQL.execute(f'select user_id from consommable where user_id="{USER_ID}"')
    result_userID = SQL.fetchone()

    if result_userID is None:
        SQL.execute('insert into consommable(user_name, user_id, MaxMana, Mana, Heal, Force, Defence) values(?,?,?,?,?,?,?)', (USER_NAME, USER_ID, s10, s5, s10, s1, s1))
        db.commit()

    SQL.execute('create table if not exists industrie("Num" integer primary key autoincrement,"user_name" text, "user_id" integer NOT NULL, "Mine_Pierre" REAL, "Mine_Fer" REAL,)')
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

    SQL.execute('create table if not exists Accounts("Num" integer primary key autoincrement, "user_name" text, "user_id" integer NOT NULL, "Pierre" REAL, "Charbon" REAL, "Fer" REAL, "Gold" REAL, "Diamant" REAL, "obsidienne" REAL, "Coin" REAL)')
    SQL.execute(f'select user_id from Accounts where user_id="{USER_ID}"')
    result_userID = SQL.fetchone()

    if result_userID is None:
        SQL.execute('insert into Accounts(user_name, user_id, Pierre, Charbon, Fer, Gold, Diamant, obsidienne, Coin) values(?,?,?,?,?,?,?,?,?)', (USER_NAME, USER_ID, START_BALANCE, s0, s0, s0, s0, s0, s0))
        db.commit()

    SQL.execute('create table if not exists consommable("Num" integer primary key autoincrement, "user_name" text, "user_id" integer NOT NULL, "Mana" REAL)')
    SQL.execute(f'select user_id from consommable where user_id="{USER_ID}"')
    result_userID = SQL.fetchone()

    if result_userID is None:
        SQL.execute('insert into consommable(user_name, user_id, MaxMana, Mana, Heal, Force, Defence) values(?,?,?,?,?,?,?)', (USER_NAME, USER_ID, s10, s5, s10, s1, s1))
        db.commit()

    SQL.execute('create table if not exists industrie("Num" integer primary key autoincrement, "user_name" text, "user_id" integer NOT NULL, "Mine_Pierre" REAL, "Mine_Fer" REAL)')
    SQL.execute(f'select user_id from industrie where user_id="{USER_ID}"')
    result_userID = SQL.fetchone()

    if result_userID is None:
        SQL.execute('insert into industrie(user_name, user_id, Mine_Pierre, Mine_Fer,) values(?,?,?,?)', (USER_NAME, USER_ID, s0, s0,))
        db.commit()

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
    Daily = randint(100,1000)
    USER_ID = ctx.message.author.id
    USER_NAME = str(ctx.message.author)

    SQL.execute(f'select Coin from Accounts where user_id="{USER_ID}"')

    SQL.execute(f'update Accounts set Coin = Coin + {Daily} where user_id="{USER_ID}"')
    db.commit()
    result_userbal = SQL.fetchone()

    await ctx.send(f"{ctx.message.author.mention} tu gagne {Daily} {Coin}")


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

    SQL.execute(f'select Gold from Accounts where user_id="{USER_ID}"')
    result_userbal = SQL.fetchone()

    embed.add_field(name="Or",value=f"{result_userbal[0]} {Or}",inline=True)

    SQL.execute(f'select Diamant from Accounts where user_id="{USER_ID}"')
    result_userbal = SQL.fetchone()

    embed.add_field(name="Diamant",value=f"{result_userbal[0]} {Diamant}",inline=True)

    SQL.execute(f'select obsidienne from Accounts where user_id="{USER_ID}"')
    result_userbal = SQL.fetchone()

    embed.add_field(name="obsidienne",value=f"{result_userbal[0]} {obsidienne}",inline=True)

    SQL.execute(f'select Coin from Accounts where user_id="{USER_ID}"')
    result_userbal = SQL.fetchone()

    embed.add_field(name="Coin",value=f"{result_userbal[0]} {Coin}",inline=True)

    embed.set_thumbnail(url="https://media.discordapp.net/attachments/668182697335848975/714214889178005546/sac.gif")

    embed.set_footer(text=time.strftime('%A %d/%m/%Y %H:%M:%S'))

    await ctx.channel.send(embed=embed)

    embed = discord.Embed(
	title=f"consommable de {USER_NAME}",
	color = 0xFFD801
	)

    SQL.execute(f'select Mana from consommable where user_id="{USER_ID}"')
    result_userbal = SQL.fetchone()

    SQL.execute(f'select MaxMana from consommable where user_id="{USER_ID}"')
    result_userbal1 = SQL.fetchone()

    embed.add_field(name="Mana",value=f"{result_userbal[0]}/{result_userbal1[0]} Mana",inline=True)

    SQL.execute(f'select Heal from consommable where user_id="{USER_ID}"')
    result_userbal = SQL.fetchone()

    embed.add_field(name="PV",value=f"{result_userbal[0]} PV",inline=True)

    SQL.execute(f'select Force from consommable where user_id="{USER_ID}"')
    result_userbal = SQL.fetchone()

    embed.add_field(name="Force",value=f"{result_userbal[0]} Force",inline=True)

    SQL.execute(f'select Defence from consommable where user_id="{USER_ID}"')
    result_userbal = SQL.fetchone()

    embed.add_field(name="Defence",value=f"{result_userbal[0]} Defence",inline=True)

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


client.run('NjY4ODc2NjI3MjI4NDkxNzg5.XtVr3Q.ZBMQ_y3xExcCNQx2JegT5wGhp_M')

#crée par λητθιηε#8330 et aur3my#3201 copyright par InterliX
