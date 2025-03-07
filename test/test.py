import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel, getLogger

logger = getLogger(__name__)


class Test(commands.Cog):
    """Plugin to delete multiple messages at once."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot  
    
    @commands.command()
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def tester(self, ctx: commands.Context, amount: int):
        """This is just my test command... Freel free to ignore :wink:"""
        
        message ="Hello, world!"
        await ctx.send(message)
     
    @commands.command()
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def tester2(self, ctx: commands.Context):
        """This is just my test command... Freel free to ignore :wink:"""
        
        message ="Hello, world!"
        await ctx.send(message)
    
    @commands.command()
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def tester3(self, ctx: commands.Context, message: string):
        """This is just my test command... Freel free to ignore :wink:"""
        
        await ctx.send(message)
    
    @checks.has_permissions(PermissionLevel.SUPPORTER)
    @checks.thread_only()
    @commands.command()
    async def claim(self, ctx):
        """Hello there!"""
        await ctx.send('Thread is already claimed. Or is it?')
        
  

    @commands.command()
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def purge(self, ctx: commands.Context, amount: int):
        """Delete multiple messages at once."""

        if amount < 1:
            raise commands.BadArgument(
                "The amount of messages to delete should be a scrictly "
                f"positive integer, not `{amount}`."
            )

        try:
            deleted = await ctx.channel.purge(limit=amount + 1)
        except discord.Forbidden:
            embed = discord.Embed(color=self.bot.error_color)

            embed.description = (
                "This command requires the `Manage Messages` permission, "
                "which the bot does not have at the moment."
            )

            return await ctx.send(embed=embed)

        logger.debug(
            f"{ctx.author} purged {len(deleted)} messages in the "
            f"#{ctx.channel} channel."
        )  # len(deleted) >= 2 so no plural checks necessary

        message = f"{len(deleted)} messages have been deleted!"
        to_delete = await ctx.send(message)

        await to_delete.delete(delay=3)


async def setup(bot: commands.Bot):
    await bot.add_cog(Test(bot))
