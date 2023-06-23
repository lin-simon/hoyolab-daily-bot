import os

from token_manager import populate_db, update_db, remove_from_db, sanitize_token
from claim import check_in
from assets import reward_image
from embeds import init_embeds

from interactions.ext.paginators import Page, Paginator
from interactions import (
    Client,
    slash_command,  
    SlashContext, 
    Modal,  
    ModalContext,
    ShortText, 
    ParagraphText,
    Embed,
    Activity,
    ActivityType,
)

embeds = init_embeds()

client = Client(token=os.getenv("hsr_token"))

async def on_ready():
    await client.change_presence(activity=Activity(type=ActivityType.GAME, name="/guide"))

@slash_command(name="authenticate", description="share your senstive info!!!")
async def authenticate(ctx: SlashContext):
    db = populate_db()
    if str(ctx.author.id) in list(db.keys()): 
        return await ctx.send("do /claim idiot")

    authenticator = Modal(
        ShortText(label="Enter your username:", custom_id="user", placeholder="can be anything"),
        ParagraphText(label="Paste your token below:", custom_id="token", placeholder="type /guide to learn how to get token"),
        title="starrail login reward getter thing"
    )
    
    await ctx.send_modal(modal=authenticator)
    query: ModalContext = await ctx.bot.wait_for_modal(authenticator)
    if sanitize_token(query.responses["token"]):
        update_db(ctx.author.id, sanitize_token(query.responses["token"]))
        await query.send("verified!!! now do /claim for rewards!!!")
    else:
        await query.send("invalid token, make sure you are logged in to the website")

@slash_command(name="unlink", description="unlink your token from star whale")
async def unlink(ctx: SlashContext):
    db = populate_db()
    try:
        remove_from_db(str(ctx.author.id))
        db.pop(str(ctx.author.id))
        await ctx.send("unlinked!")
    except KeyError:
        await ctx.send("no account linked")

@slash_command(name="claim", description="claim star rail daily rewards!!")
async def claim(ctx: SlashContext):
    try:
        await ctx.defer()
        db = populate_db()
        result = check_in(db[str(ctx.author.id)])
        if type(result) == list:
            embed = Embed(
                title=f"{result[1]}",
                color=15844367,
                description=f"Reward: **{result[3]}**",
                footer=f"Total Logins: {result[2]}")
            embed.set_image(reward_image(result[3]))
            await ctx.send(embeds=embed)
        else:
            await ctx.send(result)              
    except KeyError:
        await ctx.send("no account linked, do /authenticate")
        
@slash_command(name="guide", description="learn how to use bot")
async def guide(ctx: SlashContext):
    
    paginator = Paginator.create_from_embeds(client, *embeds)    
    paginator.show_first_button = False
    paginator.show_last_button = False
    paginator.show_select_menu = True
    
    await paginator.send(ctx)

client.start()




