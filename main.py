import discord
from discord.ext import commands
from wee import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def im(ctx):
    if ctx.message.attachments:
        for archi in ctx.message.attachments:
            name= archi.filename
            url = archi.url
            await archi.save(f"./{name}")
            clase = (get_class (model="keras_model.h5", labels="labels.txt", image=f"./{name}"))
            if clase[0] == "Revolver": 
                await ctx.send("El revólver es un tipo de pistola que se caracteriza por tener la munición alojada en varias recámaras dispuestas en un tambor o cilindro, a diferencia de las armas de fuego cortas semiautomáticas, que tienen la recámara unida al cañón y suelen llevar la munición alojada en un cargador. El revólver Colt Peacemaker, también conocido como Colt 1873 o Colt SAA . 45, se ha convertido en el revolver más famoso de la historia. 500 S&W Magnum hoy en día es el revólver de serie más potente del mundo.")
 
            elif clase[0] == "Pistola":
                await ctx.send("Una pistola es un arma de fuego corta diseñada para ser apuntada y disparada con una sola mano, o con dos, se puede utilizar para la caza dependiendo del arma y dispara balas a corto alcance. A todos ellos, para bien y para mal, les rememora a la pistola más popular del planeta: la Glock.")

            elif clase[0] == "Escopeta":
                await ctx.send("Una escopeta es un arma de fuego, de ánima lisa o rayada, de mano, y que se sostiene contra el hombro, diseñada para descargar varios proyectiles en cada disparo. Escopeta Remington modelo 870 Wingmaster, Con un receptor mecanizado a partir de una sólida pieza de acero, es el modelo de resistencia duradera. Fiel a su diseño original, la bomba se desliza con sedosa seguridad sobre dos barras de doble acción para lograr la máxima cámara y expulsión positivas. Estas características, junto con su impecable equilibrio y sus cualidades naturales de puntería, han convertido al modelo 870 en la escopeta más vendida y más confiable de todos los tiempos, con cualquier tipo de acción y de cualquier fabricante.")

            elif clase[0] == "Rifle":
                await ctx.send("Un fusil es un arma de fuego portátil de cañón largo, que dispara balas de largo alcance.​ Creada con propósitos ofensivos, es el arma personal más utilizada en los ejércitos desde el final del siglo XVII. Se acostumbraba fijarle una bayoneta para la lucha cuerpo a cuerpo. Gracias a que los materiales y la construcción de la AK-47 son de bajo costo, se ha convertido en el arma más numerosa del planeta. Se calcula que existen entre 35 y 50 millones de fusiles de este tipo en estos momentos en más de cincuenta países.")
    else:
        await ctx.send("Olvidaste subir la imagen :(")



bot.run("Token")