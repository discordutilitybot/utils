import discord
from discord import Guild
from discord.ext import commands


# Make sure its always asynchronous (since dpy is async duh)
async def get_prefix(bot, message):
    prefix = await (await bot.db.execute(f"SELECT guild_prefix FROM guilds WHERE id = {ctx.guild.id}", message.guild.id)).fetchone()
