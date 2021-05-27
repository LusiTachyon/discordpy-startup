from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='tc')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()
async def スペシャルウイーク(ctx):
    await ctx.send('https://umamusumematome.net/wp-content/uploads/2021/04/%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%A6%E3%82%A3%E3%83%BC%E3%82%AF.png')
    
@bot.command()
async def サイレンススズカ(ctx):
    await ctx.send('https://umamusume.jp/app/wp-content/uploads/2021/01/575dbb1ed83018483becd9f613c3fb35.png')
    
@bot.command()
async def トウカイテイオー(ctx):
    await ctx.send('https://umamusume.jp/app/wp-content/uploads/2021/01/18ba01c0c00b4f5e2c246e1b80aa13ff.png')
    
@bot.command()
async def マルゼンスキー(ctx):
    await ctx.send('http://mageru.org/wp-content/uploads/2021/02/mageru_umamusume_blog_maruzensky-666x1024.png')
    
@bot.command()
async def オグリキャップ(ctx):
    await ctx.send('https://livedoor.blogimg.jp/akb83-c9npozlg/imgs/8/0/8015551f.png')
    
@bot.command()
async def タイキシャトル(ctx):
    await ctx.send('https://umamusume.jp/app/wp-content/uploads/2021/01/8cb1efa8488b4dd008f47d31137d546d.png')
    
@bot.command()
async def メジロマックイーン(ctx):
    await ctx.send('https://i.pinimg.com/originals/5d/96/02/5d96024b7a7aedddfc126ad5557d782f.png')
    
@bot.command()
async def シンボリルドルフ(ctx):
    await ctx.send('https://umamusume.jp/app/wp-content/uploads/2021/01/900065cbe5ecb091cd2911d68d866a31.png')
    
@bot.command()
async def ライスシャワー(ctx):
    await ctx.send('https://umamusume.jp/app/wp-content/uploads/2021/01/3f870987542d38df7399e4b721700e0c.png')
    
@bot.command()
async def アグネスタキオン(ctx):
    embed=discord.Embed(title="アグネスタキオン", color=0xff00ff)
embed.set_thumbnail(url="https://img.game8.jp/5652871/328858adf869cfe77a521ac3da91545f.png/show")
embed.add_field(name="適性距離", value="中距離", inline=True)
embed.add_field(name="適性脚質", value="先行", inline=True)
embed.add_field(name="ステータス成長率", value="スピード+20%  根性＋10%", inline=True)
await ctx.send(embed=embed)

bot.run(token)
