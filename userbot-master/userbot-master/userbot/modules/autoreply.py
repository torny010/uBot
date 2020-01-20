import asyncio

from userbot.events import register

message = "**⛔️ Al momento sono OFFLINE.\n⚠️ Risponderò il prima possibile.\n\n👉🏻 NON spammatemi troppi messaggi, Quando torno ONLINE mi dici quello di cui hai bisogno.**"
exempt = []
mutedList = []
autoNiceText = False

@register(incoming=True, pattern="^.dev$")
async def devInfo(e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    await e.reply("**⚙ Dev: @Magic_Angel ⚙**")

@register(outgoing=True, pattern="^Canali$")
async def Channels(e):
  await e.edit("**Canali:\n@zJugur3sRep\n\nGruppi:\n@GruppoVenditeStonks**")

@register(outgoing=True, pattern="^.pula$")
async def CARABINIERIIIIIIIIIII(e):
  for i in range(10):
    await asyncio.wait([e.edit("🔵🔵🔵🔵   🔴🔴🔴🔴\n🔵🔵🔵🔵   🔴🔴🔴🔴\n🔵🔵🔵🔵   🔴🔴🔴🔴\n🔵🔵🔵🔵   🔴🔴🔴🔴")])
    await asyncio.sleep(0.1)
    await asyncio.wait([e.edit("🔴🔴🔴🔴   🔵🔵🔵🔵\n🔴🔴🔴🔴   🔵🔵🔵🔵\n🔴🔴🔴🔴   🔵🔵🔵🔵\n🔴🔴🔴🔴   🔵🔵🔵🔵")])
    await asyncio.sleep(0.1)
  await asyncio.wait([e.edit("**🚨🚔 CHIAMATE IL CIENTODICIOTTOOOOO!!! 🚔🚨**")])

@register(outgoing=True)
async def niceText(e):
  if e.text[0].isalpha() and not e.text == "Canali":
    global autoNiceText
    if autoNiceText:
      mex = ""
      for i in range(len(e.text)):
        if e.text[i] == " ":
          mex = mex + ' '
        else:
          mex = mex + e.text[i]
        await asyncio.wait([e.edit("`" + mex + " |`")])
        await asyncio.sleep(0.1)
        await asyncio.wait([e.edit("`" + mex + "  ‏‏‎ `")])
        await asyncio.sleep(0.1)
        if i == len(e.text) - 1:
          await asyncio.wait([e.edit("`" + e.text + "`")])

@register(outgoing=True, pattern="^.niceText$")
async def setNiceText(e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    global autoNiceText
    if autoNiceText:
      autoNiceText = False
      await e.edit("`Animazione Testo Disattivata!`")
    else:
      autoNiceText = True
      await e.edit("`Animazione Testo Attivata!`")

@register(outgoing=True, pattern="^.mex")
async def setMessage(e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    global message
    message = str(e.text[5:])
    await e.edit("`Messaggio impostato correttamente!`")

@register(outgoing=True, pattern="^.mute$")
async def setMute(e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    if e.is_private and not (await e.get_sender()).bot:
      global mutedList
      if e.chat_id in mutedList:
        mutedList.remove(e.chat_id)
        await e.edit("`Utente Smutato!`")
      else:
        mutedList.append(e.chat_id)
        await e.edit("`Utente Mutato!`")

@register(incoming=True)
async def autoReply(e):
  if e.is_private and not (await e.get_sender()).bot:
    global mutedList
    if e.chat_id in mutedList:
      await e.delete()
    else:
      if type((await e.client.get_me()).status).__name__ ==  "UserStatusOffline":
        global exempt
        if not e.sender.id in exempt:
          exempt.append(e.sender.id)
          x = 0
          while True:
            if type((await e.client.get_me()).status).__name__ ==  "UserStatusOffline":
              await asyncio.sleep(1)
              x += 1
              if x >= 300:
                global message
                await e.respond(message)
                exempt.remove(e.sender.id)
                break
            else:
              exempt.remove(e.sender.id)
              break
