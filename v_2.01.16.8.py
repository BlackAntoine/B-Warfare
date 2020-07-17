# --------------------------------------------------------------------------#
# --------------------------------------------------------------------------#
# --------------------------------------------------------------------------#
# --------------------------------------------------------------------------#
# --------------------------------------------------------------------------#
# -----------------Crée par Antoine, Aurelien et David----------------------#
# -----------------------------v 2.01.16.9----------------------------------#
# --------------------------------------------------------------------------#
# --------------------------------------------------------------------------#
# --------------------------------------------------------------------------#
# --------------------------------------------------------------------------#

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

locale.setlocale(locale.LC_TIME, 'FR')

config_location = fileIO("assets/config/config.json", "load")
Shards = config_location["Shards"]
Prefix = config_location["Prefix"]
PASSWORD = config_location["PASSWORD"]

#info_location = fileIO("players/{}/info.json".format(member.id), "load")
#Mana = info_location["Mana"]
#MaxMana = info_location["MaxMana"]
#PV = info_location["PV"]
#MaxPV = info_location["MaxPV"]
#Defence = info_location["Defence"]
#Force = info_location["Force"]
#LV = info_location["LV"]
#XP = info_location["XP"]


client = commands.AutoShardedBot(shard_count=Shards, command_prefix=Prefix)

# -----------------------PASSWORD-------------------------#
chaine_mot_de_passe = b'Pdzas8R6T7987xErP'
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
# -----------------------PASSWORD-------------------------#

starttime = time.time()

VS = 1.0

DIR = os.path.dirname(__file__)

os.chdir(r'C:\Users\33664\Desktop\B-Warfare')

status = cycle(['InterliX', 'v 2.01.16.9', '!help', 'New update'])

db = sqlite3.connect(os.path.join(DIR, "BankAccounts.db"))

SQL = db.cursor()

client.remove_command('help')

Pierre = "Pierre"

Charbon = "Charbon"

Fer = "Fer"

Cuivre = "cuivre"

Cobalt = "Cobalt"

Gold = "Or"

Platine = "Platine"

Diamant = "Diamant💎"

Palladium = "Palladium"

Obsidienne = "Obsidienne"

Coin = "Piece"

START_BALANCE = 100.00

s0 = 0.0

s1 = 1.0

s5 = 5.0

s10 = 10.0

s20 = 20.0

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount):
    await ctx.channel.purge(limit = amount)

async def _check_levelup(ctx):
    author = ctx.author
    info_location = fileIO("players/{}/info.json".format(author.id), "load")
    xp = info_location["XP"]
    num = 1000.0
    name = info_location["name"]
    lvl = info_location["LV"]
    lvlexp = num * lvl
    GMaxMana = randint(0,1)
    GForce = randint(0,1)
    GDefence = randint(0,1)
    GPVMax = randint(0,2)


    if xp >= lvlexp:
        await ctx.send("```diff\n+ {} a gagné un level ! + {} MaxMana, + {} MaxPV, + {} Force, + {} Defence. ```".format(name, GMaxMana, GPVMax, GForce, GDefence))
        info_location["LV"] = info_location["LV"] + 1.0
        info_location["MaxMana"] = info_location["MaxMana"] + GMaxMana
        info_location["Force"] = info_location["Force"] + GForce
        info_location["Defence"] = info_location["Defence"] + GDefence
        info_location["MaxPV"] = info_location["MaxPV"] + GPVMax

        fileIO("players/{}/info.json".format(author.id), "save", info_location)
        return await _check_levelup(ctx)
    else:
        pass

@client.command
async def Mana(ctx):
    info_location = fileIO("players/{}/info.json".format(author.id), "load")
    Mana = info_location["Mana"]
    MaxMana = info_location["MaxMana"]

        if Mana == MaxMana
            await ctx.send(f"Tu ne peux plus stocker de Mana.")
    else:
        await ctx.send("Mana en cours de régénération.")
        info_location["Mana"] = info_location["Mana"] + 1.0
        fileIO("players/{}/info.json".format(author.id), "save", info_location)
        await asyncio.sleep(30)
        return await _mana_reg()

@client.command()
async def test_01(ctx):
    USER_NAME = str(ctx.message.author)
    author = ctx.author
    info_location = fileIO("players/{}/info.json".format(author.id), "load")

    if info_location["Language"] == 1.0:
        await ctx.send(f"Salut, je suis B-Warfare traduit en français.")
    elif info_location["Language"] == 0.0:
        await ctx.send(f"Hi, I'm B-Warfare translated into english.")

@client.command()
async def lang(ctx, arg):
    author = ctx.author

    info_location = fileIO("players/{}/info.json".format(author.id), "load")
    if arg == "fr":
        info_location["Language"] = info_location["Language"] == 1.0
        await author.create_dm()
        await author.dm_channel.send(f'B-Warfare est configuré en français.')
    elif arg == "en":
        info_location["Language"] = info_location["Language"] == 0.0
        await author.create_dm()
        await author.dm_channel.send(f'B-Warfare is translated into english.')


    fileIO("players/{}/info.json".format(author.id), "save", info_location)

@client.command()
async def tuto(ctx, amount=1):
    USER_NAME = str(ctx.message.author)
    author = ctx.author
    message = ctx.message
    await ctx.send(f'Ah ! Bonjour jeune aventurier, tu doit être {USER_NAME} si je ne me trompe ? On m\'a beaucoup parlé de toi et de tes exploits. Si tu es ici c\'est pour une tache très simple :')
    await asyncio.sleep(10)
    await ctx.channel.purge(limit=amount)
    await ctx.send('SAUVER LE MONDE !')
    await asyncio.sleep(4)
    await ctx.channel.purge(limit=amount)
    await ctx.send('Alors prépare toi a une grande aventure !')
    await asyncio.sleep(4)
    await ctx.channel.purge(limit=amount)

    if not os.path.exists("players/{}".format(author.id)):
        os.makedirs("players/{}".format(author.id))
        new_account = {
            "name":f"{USER_NAME}",
            "Ready":"",
            "Mana": 5.0,
            "MaxMana":10.0,
            "LV":1.0,
            "XP":0.0,
            "Force":1.0,
            "Defence":1.0,
            "PV":100.0,
            "MaxPV":100.0,
            "Daily_time":0.0,
            "Language":1.0,
            "in_party": []
        }
        fileIO("players/{}/info.json".format(author.id), "save", new_account)
    info = fileIO("players/{}/info.json".format(author.id), "load")

    await ctx.send('Faite la commande "!ready" quand vous êtes prêt.')

@client.command()
async def ready(ctx):
    USER_NAME = str(ctx.message.author)
    author = ctx.author
    message = ctx.message

    info_location = fileIO("players/{}/info.json".format(member.id), "load")
    info_location["Ready"] = info_location["ready"] + 1
    fileIO("players/{}/info.json".format(ctx.author.id), "save", info_location)




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

    SQL.execute(
        'create table if not exists Accounts("Num" integer primary key autoincrement, "user_name" text, "user_id" integer NOT NULL, "Pierre" REAL, "Charbon" REAL, "Fer" REAL, "Cuivre" REAL, "Cobalt" REAL, "Gold" REAL,"Platine" REAL, "Diamant" REAL, "Palladium" REAL, "Obsidienne" REAL, "Coin" REAL)')
    SQL.execute(f'select user_id from Accounts where user_id="{USER_ID}"')
    result_userID = SQL.fetchone()

    if result_userID is None:
        SQL.execute(
            'insert into Accounts(user_name, user_id, Pierre, Charbon, Fer, Cuivre, Cobalt, Gold, Platine, Diamant, Palladium, Obsidienne, Coin) values(?,?,?,?,?,?,?,?,?)',
            (USER_NAME, USER_ID, START_BALANCE, s0, s0, s0, s0, s0, s0, s0, s0, s0, s0))
        db.commit()

    SQL.execute(
        'create table if not exists industrie("Num" integer primary key autoincrement,"user_name" text, "user_id" integer NOT NULL, "Mine_Pierre" REAL, "Mine_Fer" REAL)')
    SQL.execute(f'select user_id from industrie where user_id="{USER_ID}"')
    result_userID = SQL.fetchone()

    if result_userID is None:
        SQL.execute(
            'insert into industrie(user_name, user_id, Mine_Pierre, Mine_Fer,) values(?,?,?,?)',
            (USER_NAME, USER_ID, s0, s0,))
        db.commit()

    await member.create_dm()
    await member.dm_channel.send(
        f'Salut {member.name},bienvenue sur le serveur Discord! je te dit de faire !start dans le salon commande')

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.User, *reason):
    reason = " ".join(reason)
    await ctx.guild.kick(user, reason=reason)
    await ctx.send(f"{user} a été kick.")


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
    await ctx.channel.send(
        f'Bienvenue {ctx.message.author.mention}, je me prénomme X Æ A-Xii et je serai ton parrain pour ton aventure, nous sommes en 3025, suite à une guerre bactériologique. 98 % De la population mondiale a succombé, les machines on donc commencé à vouloir prendre le pouvoir, à vous de les en empêcher. Pour commencer je te propose de faire la commande !mine pour miner puis tu peut faire la commande !i pour ouvrir ton inventaire.')
    await asyncio.sleep(3)
    await ctx.message.delete()

    SQL.execute(
        'create table if not exists Accounts("Num" integer primary key autoincrement, "user_name" text, "user_id" integer NOT NULL, "Pierre" REAL, "Charbon" REAL, "Fer" REAL, "Cuivre" REAL, "Cobalt" REAL, "Gold" REAL,"Platine" REAL, "Diamant" REAL, "Palladium" REAL, "Obsidienne" REAL, "Coin" REAL)')
    SQL.execute(f'select user_id from Accounts where user_id="{USER_ID}"')
    result_userID = SQL.fetchone()

    if result_userID is None:
        SQL.execute(
            'insert into Accounts(user_name, user_id, Pierre, Charbon, Fer, Cuivre, Cobalt, Gold, Platine, Diamant, Palladium, Obsidienne, Coin) values(?,?,?,?,?,?,?,?,?)',
            (USER_NAME, USER_ID, START_BALANCE, s0, s0, s0, s0, s0, s0, s0, s0, s0, s0))
        db.commit()

    SQL.execute(
        'create table if not exists industrie("Num" integer primary key autoincrement,"user_name" text, "user_id" integer NOT NULL, "Mine_Pierre" REAL, "Mine_Fer" REAL)')
    SQL.execute(f'select user_id from industrie where user_id="{USER_ID}"')
    result_userID = SQL.fetchone()

    if result_userID is None:
        SQL.execute('insert into industrie(user_name, user_id, Mine_Pierre, Mine_Fer,) values(?,?,?,?)',
                    (USER_NAME, USER_ID, s0, s0,))
        db.commit()

@client.command()
async def credits(ctx):
    embed = discord.Embed(
        title=f"Credits",
        color=0xe0ff00
    )

    embed.add_field(name="Developpeurs", value="Λητθιηε & AUR3MY")

    embed.set_footer(text=time.strftime('%A %d/%m/%Y %H:%M:%S'))

    await ctx.channel.send(embed=embed)

@client.command()
async def shop(ctx):
    USER_ID = ctx.message.author.id
    USER_NAME = str(ctx.message.author)
    info_location = fileIO("players/{}/info.json".format(ctx.author.id), "load")
    if info_location["Ready"]  == 0:
        await ctx.send("Tu dois d\'abord faire le tuto avant de commencer ta grande aventure ! `{}tuto`".format(Prefix))
        return
    embed = discord.Embed(
        title=f"SHOP",
        color=0x36FF00
    )
    embed.add_field(name='Bienvenue dans le "SHOP" !',value='Ici tu peux vendre n\'importe quel objet')
    embed.add_field(name='!sell [insérer nom objet] [nombre]',value='Cette commande sert a vendre un objet unique.')
    embed.add_field(name='!sell all',value='Celle-ci sert a vendre tout les minerais de votre inventaire.')
    await ctx.channel.send(embed=embed)

@client.command()
async def mine(ctx):
    MPierre = randint(10000, 50000)
    MCharbon = randint(7500, 35000)
    MFer = randint(4500, 20000)
    MCuivre = randint(2500, 10000)
    MCobalt = randint(1000, 5000)
    MOr = randint(500, 2500)
    MPlatine = randint(1000, 5000)
    MDiamant = randint(0, 20)
    MPalladium = randint(1000, 5000)
    MObsidienne = randint(2500, 10000)
    MXP = randint(10, 150)
    USER_ID = ctx.message.author.id
    USER_NAME = str(ctx.message.author)
    info_location = fileIO("players/{}/info.json".format(ctx.author.id), "load")

    if info_location["Mana"] < 1.0 :
        await ctx.send("```diff\n-► Vous n'avez pas assez de Mana pour réaliser cette action.```")
    else :

        info_location["Mana"] = info_location["Mana"] - 1.0

        info_location["XP"] = info_location["XP"] + MXP

        embed = discord.Embed(
        title=f"Vous avez minez :",
        color=0x00FFFB
        )

        SQL.execute(f'select Pierre from Accounts where user_id="{USER_ID}"')

        SQL.execute(f'update Accounts set Pierre = Pierre + {MPierre} where user_id="{USER_ID}"')
        db.commit()
        result_Pierre = SQL.fetchone()

        embed.add_field(name="Pierre", value=f"{MPierre}", inline=True)

        SQL.execute(f'select Charbon from Accounts where user_id="{USER_ID}"')

        SQL.execute(f'update Accounts set Charbon = Charbon + {MCharbon} where user_id="{USER_ID}"')
        db.commit()
        result_Charbon = SQL.fetchone()

        embed.add_field(name="Charbon", value=f"{MCharbon}", inline=True)

        SQL.execute(f'select Fer from Accounts where user_id="{USER_ID}"')

        SQL.execute(f'update Accounts set Fer = Fer + {MFer} where user_id="{USER_ID}"')
        db.commit()
        result_Fer = SQL.fetchone()

        embed.add_field(name="Fer", value=f"{MFer}", inline=True)

        SQL.execute(f'select Cuivre from Accounts where user_id="{USER_ID}"')

        SQL.execute(f'update Accounts set Cuivre = Cuivre + {MCuivre} where user_id="{USER_ID}"')
        db.commit()
        result_Cuivre = SQL.fetchone()

        embed.add_field(name="Cuivre", value=f"{MCuivre}", inline=True)

        SQL.execute(f'select Obsidienne from Accounts where user_id="{USER_ID}"')
        SQL.execute(f'update Accounts set Obsidienne = Obsidienne + {MObsidienne} where user_id="{USER_ID}"')
        db.commit()
        result_Obsidienne = SQL.fetchone()

        embed.add_field(name="Obsidienne", value=f"{MObsidienne}", inline=True)

        SQL.execute(f'select Cobalt from Accounts where user_id="{USER_ID}"')
        SQL.execute(f'update Accounts set Cobalt = Cobalt + {MCobalt} where user_id="{USER_ID}"')
        db.commit()
        result_Cobalt = SQL.fetchone()

        embed.add_field(name="Cobalt", value=f"{MCobalt}", inline=True)

        SQL.execute(f'select Platine from Accounts where user_id="{USER_ID}"')
        SQL.execute(f'update Accounts set Platine = Platine + {MPlatine} where user_id="{USER_ID}"')
        db.commit()
        result_Platine = SQL.fetchone()

        embed.add_field(name="Platine", value=f"{MPlatine}", inline=True)

        SQL.execute(f'select Palladium from Accounts where user_id="{USER_ID}"')
        SQL.execute(f'update Accounts set Palladium = Palladium + {MPalladium} where user_id="{USER_ID}"')
        db.commit()
        result_Palladium = SQL.fetchone()

        embed.add_field(name="Palladium", value=f"{MPalladium}", inline=True)

        SQL.execute(f'select Gold from Accounts where user_id="{USER_ID}"')
        SQL.execute(f'update Accounts set Gold = Gold + {MOr} where user_id="{USER_ID}"')
        db.commit()
        result_Or = SQL.fetchone()

        embed.add_field(name="Or", value=f"{MOr}", inline=True)

        SQL.execute(f'select Diamant from Accounts where user_id="{USER_ID}"')
        SQL.execute(f'update Accounts set Diamant = Diamant + {MDiamant} where user_id="{USER_ID}"')
        db.commit()
        result_Diamant = SQL.fetchone()

        embed.add_field(name="Diamant", value=f"{MDiamant}", inline=True)


        embed.add_field(name="XP", value=f"{MXP}", inline=True)

        embed.set_thumbnail(
            url="https://media.discordapp.net/attachments/721338399562137610/732734690565292113/8096.png")

        fileIO("players/{}/info.json".format(ctx.author.id), "save", info_location)

        await ctx.channel.send(embed=embed)

        await _check_levelup(ctx)


@client.command()
async def daily(ctx):
    DailyC = randint(100, 1000)
    DailyX = randint(700, 1500)
    author = ctx.author
    info_location = fileIO("players/{}/info.json".format(author.id), "load")
    USER_ID = ctx.message.author.id
    USER_NAME = str(ctx.message.author)
    curr_time = time.time()
    delta = float(curr_time) - float(info_location["Daily_time"])

    if delta >= 86400.0 and delta>0:
        info_location["Daily_time"] = curr_time
        fileIO("players/{}/info.json".format(ctx.author.id), "save", info_location)
        await ctx.send(f"{ctx.message.author.mention} tu gagne {DailyC} coin et {DailyX} XP.")

        SQL.execute(f'select Coin from Accounts where user_id="{USER_ID}"')

        SQL.execute(f'update Accounts set Coin = Coin + {DailyC} where user_id="{USER_ID}"')
        db.commit()
        result_userbal = SQL.fetchone()

        info_location["XP"] = info_location["XP"] + DailyX
        fileIO("players/{}/info.json".format(author.id), "save", info_location)
    else:
        seconds = 86400 - delta
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        await ctx.send("```diff\n-► Tu peux recuperer ton daily dans :{} Heures, {} Minutes, et {} Secondes```".format(int(h), int(m), int(s)))

    await _check_levelup(ctx)

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
        color=0x00FFB2
    )

    embed.add_field(name="Créateur", value=f"Λητθιηε#8330 / AUR3MY#3201", inline=True)

    embed.add_field(name="Version", value=f"v 2.01.16.8", inline=True)

    embed.add_field(name="Langage de programmation", value=f"Python/python", inline=True)

    embed.add_field(name="API", value=f"Non disponible", inline=True)

    embed.add_field(name="joueur", value=f"{numberOfPerson}", inline=True)

    embed.add_field(name="channels vocaux", value=f"{numberOfVoiceChannels}", inline=True)

    embed.add_field(name="channels textuels", value=f"{numberOfTextChannels}", inline=True)

    embed.add_field(name="Shards", value=f"{Shards}", inline=True)

    embed.add_field(name="BG:", value=f"ZowKleGentil#6365", inline=True)

    embed.set_footer(text=time.strftime('%A %d/%m/%Y %H:%M:%S'))

    await ctx.channel.send(embed=embed)


@client.command()
async def help(ctx):
    embed = discord.Embed(
        title=f"Commande principale de B-Warfare",
        color=0x2eff00
    )

    embed.add_field(name="!start", value=f"Commence ton aventure", inline=False)

    embed.add_field(name="!i", value=f"Ouvre ton inventaire", inline=False)

    embed.add_field(name="!mine", value=f"Mine des minéraux", inline=False)

    embed.add_field(name="!daily", value=f"Reçois ton argent quotidiennement", inline=False)

    embed.add_field(name="!industrie", value=f"Industrie", inline=False)

    await ctx.channel.send(embed=embed)

    embed = discord.Embed(
        title=f"Commande secondaire ou admin servant pour B-Warfare",
        color=0xfbff00
    )

    embed.add_field(name="!info", value=f"Donne des information sur le serveur", inline=False)

    embed.add_field(name="!ping", value=f"Ping du bot", inline=False)

    embed.add_field(name="!kick", value=f"Kick les joueur toxic", inline=False)

    embed.add_field(name="!credits", value=f"Credits", inline=False)

    embed.set_footer(text=time.strftime('%A %d/%m/%Y %H:%M:%S'))

    await ctx.channel.send(embed=embed)


@client.command()
async def i(ctx, ):
    author = ctx.author
    USER_ID = ctx.message.author.id
    USER_NAME = str(ctx.message.author)
    info_location = fileIO("players/{}/info.json".format(ctx.author.id), "load")
    Mana = info_location["Mana"]
    MaxMana = info_location["MaxMana"]
    PV = info_location["PV"]
    MaxPV = info_location["MaxPV"]
    XP = info_location["XP"]
    LV = info_location["LV"]
    Defence = info_location["Defence"]
    Force = info_location["Force"]

    SQL.execute(
        'create table if not exists Accounts("Num" integer primary key autoincrement, "user_name" text, "user_id" integer NOT NULL, "Pierre" REAL, "Charbon" REAL, "Fer" REAL, "Cuivre" REAL, "Cobalt" REAL, "Gold" REAL,"Platine" REAL, "Diamant" REAL, "Palladium" REAL, "Obsidienne" REAL, "Coin" REAL)')
    SQL.execute(f'select user_id from Accounts where user_id="{USER_ID}"')
    result_userID = SQL.fetchone()

    if result_userID is None:
        SQL.execute(
            'insert into Accounts(user_name, user_id, Pierre, Charbon, Fer, Cuivre, Cobalt, Gold, Platine, Diamant, Palladium, Obsidienne, Coin) values(?,?,?,?,?,?,?,?,?)',
            (USER_NAME, USER_ID, START_BALANCE, s0, s0, s0, s0, s0, s0, s0, s0, s0, s0))
        db.commit()

    embed = discord.Embed(
        title=f"inventaire de {USER_NAME}",
        color=0xFFD801
    )

    SQL.execute(f'select Pierre from Accounts where user_id="{USER_ID}"')
    result_userbal = SQL.fetchone()

    embed.add_field(name="Pierre", value=f"{result_userbal[0]} {Pierre}", inline=True)

    SQL.execute(f'select Charbon from Accounts where user_id="{USER_ID}"')
    result_userbal = SQL.fetchone()

    embed.add_field(name="Charbon", value=f"{result_userbal[0]} {Charbon}", inline=True)

    SQL.execute(f'select Fer from Accounts where user_id="{USER_ID}"')
    result_userbal = SQL.fetchone()

    embed.add_field(name="Fer", value=f"{result_userbal[0]} {Fer}", inline=True)

    SQL.execute(f'select Cuivre from Accounts where user_id="{USER_ID}"')
    result_userbal = SQL.fetchone()

    embed.add_field(name="Cuivre", value=f"{result_userbal[0]} {Cuivre}", inline=True)

    SQL.execute(f'select Cobalt from Accounts where user_id="{USER_ID}"')
    result_userbal = SQL.fetchone()

    embed.add_field(name="Cobalt", value=f"{result_userbal[0]} {Cobalt}", inline=True)

    SQL.execute(f'select Gold from Accounts where user_id="{USER_ID}"')
    result_userbal = SQL.fetchone()

    embed.add_field(name="Or", value=f"{result_userbal[0]} {Gold}", inline=True)

    SQL.execute(f'select Platine from Accounts where user_id="{USER_ID}"')
    result_userbal = SQL.fetchone()

    embed.add_field(name="Platine", value=f"{result_userbal[0]} {Platine}", inline=True)

    SQL.execute(f'select Diamant from Accounts where user_id="{USER_ID}"')
    result_userbal = SQL.fetchone()

    embed.add_field(name="Diamant", value=f"{result_userbal[0]} {Diamant}", inline=True)

    SQL.execute(f'select Palladium from Accounts where user_id="{USER_ID}"')
    result_userbal = SQL.fetchone()

    embed.add_field(name="Palladium", value=f"{result_userbal[0]} {Palladium}", inline=True)

    SQL.execute(f'select Obsidienne from Accounts where user_id="{USER_ID}"')
    result_userbal = SQL.fetchone()

    embed.add_field(name="Obsidienne", value=f"{result_userbal[0]} {Obsidienne}", inline=True)

    SQL.execute(f'select Coin from Accounts where user_id="{USER_ID}"')
    result_userbal = SQL.fetchone()

    embed.add_field(name="Coin", value=f"{result_userbal[0]} {Coin}", inline=True)

    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/721338399562137610/732740123392999454/Sac.png")

    embed.set_footer(text=time.strftime('%A %d/%m/%Y %H:%M:%S'))

    await ctx.channel.send(embed=embed)

    embed = discord.Embed(
        title=f"Consommable de {USER_NAME}",
        color=0xFFD801
    )

    embed.add_field(name="Mana", value=f"{Mana} / {MaxMana} :alembic:", inline=True)
    embed.add_field(name="PV", value=f"{PV} / {MaxPV} :heart:", inline=True)
    embed.add_field(name="LV/XP", value=f"{LV} ( {XP} )", inline=True)
    embed.add_field(name="Force", value=f"{Force} :crossed_swords:", inline=True)
    embed.add_field(name="Defence", value=f"{Defence} :shield:", inline=True)

    await ctx.channel.send(embed=embed)


@client.command()
async def industrie(ctx):
    USER_ID = ctx.message.author.id
    USER_NAME = str(ctx.message.author)
    embed = discord.Embed(
        title=f"industrie de {USER_NAME}",
        color=0xFFD801
    )

    SQL.execute(f'select Mine_Pierre from industrie where user_id="{USER_ID}"')
    result_userbal = SQL.fetchone()

    embed.add_field(name="Mine de Pierre", value=f"{result_userbal[0]} Mine de Pierre", inline=True)

    SQL.execute(f'select Mine_Fer from industrie where user_id="{USER_ID}"')
    result_userbal = SQL.fetchone()

    embed.add_field(name="Mine de Fer", value=f"{result_userbal[0]} Mine de Fer", inline=True)

    embed.set_thumbnail(url="https://media.discordapp.net/attachments/721338399562137610/732740123392999454/Sac.png")

    embed.set_footer(text=time.strftime('%A %d/%m/%Y %H:%M:%S'))

    await ctx.channel.send(embed=embed)


@client.command(aliases=['8ball', 'test'])
async def bdc(ctx, *, question):
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
        title='Boule de crystal',
        description='pose une question avec .bdc et il va te repondre.',
        color=0xFFD800
    )

    embed.set_footer(text='ba la ya pas encore')

    embed.set_thumbnail(url='')

    embed.add_field(name=f'Question: {question}', value=f'reponse: {random.choice(responses)}', inline=True)

    embed.set_footer(text=time.strftime('%A %d/%m/%Y %H:%M:%S'))

    await ctx.channel.send(embed=embed)

@client.command()
async def google(ctx):
    await ctx.send("https://www.google.com/#q=" + "+".join(params[1:]))


client.run('NjY4ODc2NjI3MjI4NDkxNzg5.Xv40wA.pOmJtnjteCVBsTC252rPHOT0uPU')

# --------------------------------------------------------------------------#
# --------------------------------------------------------------------------#
# --------------------------------------------------------------------------#
# --------------------------------------------------------------------------#
# --------------------------------------------------------------------------#
# -----------------Crée par Antoine, Aurelien et David----------------------#
# -----------------------------v 2.01.16.9----------------------------------#
# --------------------------------------------------------------------------#
# --------------------------------------------------------------------------#
# --------------------------------------------------------------------------#
# --------------------------------------------------------------------------#
