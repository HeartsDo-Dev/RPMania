#    Greysario Manager - A Discord Bot for roleplay server
#    Copyright (C) 2O19 HeartsDo
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


import discord
from discord.ext import commands
import json
import random
import logging
import sqlite3
import time
conn = sqlite3.connect('bot.db')
conn.text_factory = str
cursor = conn.cursor()
import schedule
import threading


def reset_counter():
    cursor.execute("""UPDATE entrainement_user SET rate=0 WHERE idu=*""")
    conn.commit()
    logging.info("Il est l'heure de remettre les conpteur à zéro ! (Remise à 0 des entrainements !)")


def schedl_start():
    while True:
        schedule.run_pending()
        time.sleep(1)


class Entrainements(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        with open('config.json', 'r') as fichier:
            self.config = json.load(fichier)
        schedule.every().day.at("23:59").do(reset_counter)
        # launchtime = threading.Thread(target=schedl_start) Temporaire le temps que je trouve la résolution du bug
        # launchtime.start()


    @commands.command()
    @commands.has_role("Admin")
    async def entrainement(self, ctx, row:str="None"):
        """"Entrainez vous au combat !!!\n
            Utilisation: !entrainement <defense, magie, agilite, force, maitrise-magie,
            maitrise-corps, maitrise-arme>"""
        row_supported = ['defense', 'magie', 'agilite', 'force', 'maitrise-magie',
        'maitrise-corps', 'maitrise-arme']
        user = ctx.author
        id = str(user.id)
        cursor.execute("""SELECT rate FROM entrainement_user WHERE idu=?""", [id])
        respond = [r[0] for r in cursor.fetchall()]
        respond = respond[0]
        if rate == 2:
            return await ctx.send("Cooldown: Veillez patientez jusqu'a minuit pour vous entrainemenez de nouveau !", delete_after=20)
        if row in row_supported:
            cursor.execute("""SELECT rate FROM entrainement_user WHERE idu=?""", [id])
            rate = [r[0] for r in cursor.fetchall()]
            rate = respond[0]
            num = random.randrange(1, 100, 1)
            if num < 70:
                rate + 1
                cursor.execute("""UPDATE entrainement_user SET rate=? WHERE idu=?""", (rate, [id]))
                cursor.execute("""SELECT ? FROM entrainement_user WHERE idu=?""", (row, [id]))
                respond = [r[0] for r in cursor.fetchall()]
                respond = respond[0]
                respond + 1
                cursor.execute("""UPDATE entrainement_user SET ?=? WHERE idu=?""", (row, respond, [id]))
                conn.commit()
                return await ctx.send("{}: Votre entrainement de {} a réussi !".format(user.mention, row))
            else:
                rate + 1
                cursor.execute("""UPDATE entrainement_user SET rate=? WHERE idu=?""", (rate, [id]))
                conn.commit()
                return await ctx.send("{}: Dommage, votre entrainement de {} a raté !".format(user.mention, row))
        else:
            return await ctx.send("Vous n'avez pas precisez de bonne entrainement ou il n'en a pas, merci de corriger cela !",  delete_after=20)



        @commands.command()
        @commands.has_role("Admin")
        async def info_entrainement(self, ctx):
            print("YOLO")


def setup(bot):
    bot.add_cog(Entrainements(bot))
