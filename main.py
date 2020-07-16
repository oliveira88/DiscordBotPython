import discord
import asyncio
import random
import secret

client = discord.Client()
token = secret.n_token()

msg_id = None
msd_user = None

COR = 0x690FC3


@client.event
async def on_ready():
    print('To pronto disgretça!')
    print(client.user.name)
    print(client.user.id)
    print('---------------------------------')


@client.event
async def on_member_join(member):
    canal = client.get_channel("380476242987581444")
    jogos = client.get_channel("380476242987581446")
    msg = "Eae {}, este é o canal de {}".format(member.mention, jogos.mention)
    await client.send_message(canal, msg)


@client.event
async def on_member_remove(member):
    msg = "Flws ae {}, sucesso em sua jornada!".format(member.mention)
    await client.send_message(member, msg)


# @client.event
# async def on_message(message):

#     if message.content.lower().startswith('!h'):
#         if message.author.id == "211899509725331456":
#             embed = discord.Embed(
#                 title="Eu nao sei pra que server isso entao to escrevendo qualquer coisa",
#                 color=COR,
#                 description="kkkkkkk sei la pora\n"
#                 "O pora é um teste asdasdasd\n"
#                 "boa"
#             )

#         botmsg = await message.channel.send(embed)
#         await client.add_reaction(botmsg, "📘")
#         await client.add_reaction(botmsg, "📙")

#     if message.content.lower().startswith('?beibedobiruleibe') or message.content.lower().startswith('?b'):
#         if message.author.id == "211899509725331456":
#             await client.send_message(message.channel, "Vai te tomar nu cu")
#         else:
#             await client.send_message(message.channel, "Cade tua permissão? Seu hotario")

#     if message.content.lower().startswith('?m'):

#         choice = random.randint(1, 2)
#         if choice == 1:
#             await client.send_message(message.channel, 'Voce é um merda')
#         if choice == 2:
#             await client.send_message(message.channel, 'Voce é realmente um merda')


client.run(token)
