<<<<<<< HEAD
from interactions import Embed

def init_embeds():
    embed1 = Embed(
        title="STEP 1: GO TO STARRAIL CHECK-IN PAGE",
        color=1752220,  
        footer="Page 1/4",
        description="GO TO THE DAILY REWARD PAGE: https://act.hoyolab.com/bbs/event/signin/hkrpg/index.html?act_id=e202303301540311")

    embed2 = Embed(
        title="STEP 2: OPEN UP THE CONSOLE",
        color=1752220,
        footer="Page 2/4",
        description="DO **CTRL + SHIFT + J** , will look something like this idfk")
    embed2.set_image(url='https://media.discordapp.net/attachments/943645146837307445/1120940886663123024/image.png?width=856&height=672')  

    embed3 = Embed(
        title="STEP 3: GET YOUR TOKEN",
        color=1752220,
        footer="Page 3/4",
        description="type **`document.cookie`** into the console and press enter, copy the whole token to your clipboard")
    embed3.set_image(url='https://cdn.discordapp.com/attachments/943645146837307445/1120643032694390856/image.png')  

    embed4 = Embed(
        title="STEP 4: VERIFY YOUR TOKEN",
        color=1752220,
        footer="Page 4/4",
        description="do /authenticate and paste your token in")
    embed4.set_image('https://cdn.discordapp.com/attachments/943645146837307445/1120635685783736370/image.png')

    return [embed1,
            embed2,
            embed3,
            embed4]


=======
from interactions import Embed

def init_embeds():
    embed1 = Embed(
        title="STEP 1: GO TO STARRAIL CHECK-IN PAGE",
        color=1752220,  
        footer="Page 1/4",
        description="GO TO THE DAILY REWARD PAGE: https://act.hoyolab.com/bbs/event/signin/hkrpg/index.html?act_id=e202303301540311")

    embed2 = Embed(
        title="STEP 2: OPEN UP THE CONSOLE",
        color=1752220,
        footer="Page 2/4",
        description="DO **CTRL + SHIFT + J** , will look something like this idfk")
    embed2.set_image(url='https://media.discordapp.net/attachments/943645146837307445/1120940886663123024/image.png?width=856&height=672')  

    embed3 = Embed(
        title="STEP 3: GET YOUR TOKEN",
        color=1752220,
        footer="Page 3/4",
        description="type **`document.cookie`** into the console and press enter, copy the whole token to your clipboard")
    embed3.set_image(url='https://cdn.discordapp.com/attachments/943645146837307445/1120643032694390856/image.png')  

    embed4 = Embed(
        title="STEP 4: VERIFY YOUR TOKEN",
        color=1752220,
        footer="Page 4/4",
        description="do /authenticate and paste your token in")
    embed4.set_image('https://cdn.discordapp.com/attachments/943645146837307445/1120635685783736370/image.png')

    return [embed1,
            embed2,
            embed3,
            embed4]


>>>>>>> 4a35cc32181ccc76f86f4d76912730991e94eaa1
