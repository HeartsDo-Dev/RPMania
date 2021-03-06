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
import sqlite3
import logging
conn = sqlite3.connect('bot.db')
conn.text_factory = str
cursor = conn.cursor()


class Rules(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        with open('config.json', 'r') as fichier:
            self.config = json.load(fichier)

    def update_rules(self, ctx, message, reason):
        logging.info("Règles de Greysario en cours de mise à jour pour la raison suivante: " + reason)

    @commands.command()
    async def rules(self, ctx):
