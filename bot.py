import discord
from discord.ext import commands


class Bot(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def botMorph(self, ctx, member:discord.Member=None):
		if not member: await self.bot.user.edit(username='Bot User', avatar=None)
		else:
			av = member.avatar_url.read()
			await self.bot.user.edit(username=member.name, avatar=av)


def setup(bot):
	bot.add_cog(Bot(bot))

