import random
import os
import importlib.util
from highrise import*
from highrise import BaseBot,Position
from highrise.models import SessionMetadata

casa = ["I Marry You 💍","Of course I do 💍❤️","I don't want to 💍💔","Of course I don't 💍💔","I Love You Of course I marry you 💍"]

curativo = ["🔴You Used the Bandage Your Life Is at: 100%🔴","🔴You Used the Bandage Your Life is at: 50%🔴","🔴You Used the Bandage Your Life is at: 60%🔴","🔴You Used Your Life Bandage is at: 75% Your Life is at: 90%🔴","🔴You Used the Bandage It is at: 91%🔴"]
         
bomba = ["💣🧟‍♂️ You Threw a Bomb on 1x Boss Zombie 🧟‍♀️💣","💣🧟 You Threw a Bomb on 3x Boss Zombie 🧟💣","💣🧟‍♂️ You Threw a Bomb on 2x Boss Zombie 💣🧟‍♀️","💣 🧟‍♂️ You Threw a Bomb on 7x Boss Zombie 💣🧟‍♂️","💣🧟 You Threw a Bomb on 4x Boss Zombie 🧟💣"]

facada = ["🧟🔪 You Stabbed 1x Zombie 🔪🧟","🧟🔪 You Stabbed 6x Zombie 🔪🧟","🧟🔪 You Stabbed 7x Zombie 🔪🧟","🧟‍♂️🔪🧟‍♂️ You Stabbed 8x Zombie 🔪🧟‍♂️","🧟 🔪 You Stabbed 10x Zombie 🔪🧟","🧟🔪 You Stabbed 9x Zombie 🔪🧟","🧟‍♀️🔪🧟‍♂️ You Stabbed 3x Zombie 🧟‍♂️🔪🧟‍♀️"]

atirar = ["🧟You Shot 5x Zombie🧟","🧟You Shot 1x Zombie🧟","🧟You Shot 8x Zombie🧟","🧟You Shot 3x Zombie🧟","🧟‍♂️You Shot 5x Zombie🧟‍♂️ ","🧟‍♀️You Shot 10x Zombie🧟‍♀️","🧟🧟‍♀️You Shot 9x Zombie 🧟🧟‍♀️"]

play = ["🔴Your Life is at 50% use : /bandage","🔴Your Life is at 20% use : /bandage","🔴Your Life is at 40% use : /bandage","🧟The Zombies Are Coming Use : /stab or /shoot","🧟🧟‍♂️ There Are Many Zombies 🧟‍♀️🧟 🛡 Use: /shield 🛡","🧟The Zombie Boss Is Coming Use: /bomb","🧟The Zombies Are Coming Use: /stab or/ shoot","🧟🧟‍♂️ There are Lots of Zombies 🧟‍♀️🧟 🛡 Use: /shield 🛡","🔴Your Life is at 60% use: /bandage","🔴Your Life is at 10% use: /bandage" ,"🧟The Zombies Are Coming Use : /stab or /shoot" ,"🧟The Zombies Are Coming Use : /stab or /shoot","🧟The Zombies Are Coming Use : /stab or /shoot","🧟The Zombies They're Coming Use : /stab or /shoot","🧟The Zombies Are Coming Use : /stab or /shoot","🧟The Zombies Are Coming Use : /stab or /shoot "]

pescar = ["🥈YOU WON THE MEDAL: SILVER FISHERMAN🥈","🥉YOU WON THE MEDAL: BRONZE FISHERMAN🥉","🥉YOU WON THE MEDAL: BRONZE FISHERMAN🥉","🥉YOU WON THE MEDAL: BRONZE FISHERMAN🥉","🥉YOU WON OR THE MEDAL: BRONZE FISHERMAN🥉","🟡Event: /carp 🟡","⚫️You Fished 3x Night Moon⚫️(+150 POINTS)","⚫️You Fished 2x Night Moon⚫️(+100 POINTS)"," ⚫️You Fished 1x Night Moon⚫️(+50 POINTS)","🟡You Fished 1x Golden Shrimp 🟡 (MULTIPLE POINT)","🟡You Fished 1x Golden Flounder🟡 (MULTIPLE POINT)","🪼🌈You Fished 1x Octopus Rainbow🪼🌈 (EXTRA POINTS)","🐢You Caught 3x Turtle 🐢 (LOSS OF POINTS)","🦑You Caught 1x Giant Squid 🦑 (LEGENDARY)","🦀You Caught 6x Crab 🦀 (COMMON)", "🦀You Caught 2x Crab 🦀 (COMMON)","🦀You Caught 8x Crab 🦀 (COMMON)","🪼You Caught 1x Sea Octopus🪼(EPIC)","🦈You Caught 2x Shark🦈 (EPIC)", "🦈You Fished 5x Sharks🦈 (EPIC)","🦈You Fished 8x Sharks🦈 (EPIC)","🦈You Fished 1x Sharks🦈 (EPIC)","🐠You Fished 1x Sea Tuna🐠 (LEGENDARY)", "🐠You Caught 3x Clown Fish🐠 (LEGENDARIOUS)","🐠You Caught 3x Sea Tuna🐠 (LEGENDARIOUS)","🐠You Caught 1x Clown Fish🐠 (LEGENDARIOUS)","🐠You Caught 8x Clown Fish🐠 (LEGENDARY) )","🐠You Caught 10x Clown Fish🐠 (LEGENDARY)","🐟You Caught 1x Salmon🐟 (RARE)","🧜🏼‍♀️You Caught 5x Mermaid🧜🏼‍♀️(EPIC)","🧜🏼‍ ♀️You Caught 2x Mermaid🧜🏼‍♀️(EPIC)","🧜🏼‍♀️You Caught 1x Mermaid🧜🏼‍♀️(EPIC)","🐟You Caught 3x Salmon🐟 (RARE)","🟡You Caught 1 x Tilapia Dourada🟡 (MULTIPLE POINT)","☠️🐋You Caught 3x Dead Whale☠️🐋 (LOSS OF POINTS)","🐋You Caught 11x Sea Whale🐋(COMMON)","🐋🌈You Caught 1x Rainbow Whale🌈 🐋 (EXTRA POINTS)","🥈YOU WON THE MEDAL: SILVER FISHERMAN🥈","🥇YOU WON THE MEDAL: GOLD FISHERMAN🥇","🏅YOU WON THE MEDAL: STAR FISHERMAN🏅","💎Event: /shrimp 💎"]

class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("working")
        await self.highrise.walk_to(Position(3.0 , 0.25 , 1.5, "FrontRight"))
    async def on_user_join(self, user: User, position: Position | AnchorPosition) -> None:
        print(f"{user.username} entrou na sala")   
        await self.highrise.send_whisper(user.id,f"❤️Welcome [{user.username}] Use: [!emote list] or [1-97] For Dances & Emotes")

        await self.highrise.send_whisper(user.id,f"❤️Use: [/help] For More Informations.")

        await self.highrise.send_whisper(user.id,f"❤️.🤍.")
           
        await self.highrise.send_emote("dance-hipshake")
      
        await self.highrise.send_emote("emote-lust",user.id) 
      
    async def on_chat(self, user: User, message: str) -> None:
        print(f"{user.username}: {message}")  

        if message.lower().startswith("-tipall ") and user.username == "RayMG":
              parts = message.split(" ")
              if len(parts) != 2:
                  await self.highrise.send_message(user.id, "Invalid command")
                  return
              # Checks if the amount is valid
              try:
                  amount = int(parts[1])
              except:
                  await self.highrise.chat("Invalid amount")
                  return
              # Checks if the bot has the amount
              bot_wallet = await self.highrise.get_wallet()
              bot_amount = bot_wallet.content[0].amount
              if bot_amount < amount:
                  await self.highrise.chat("Not enough funds")
                  return
              # Get all users in the room
              room_users = await self.highrise.get_room_users()
              # Check if the bot has enough funds to tip all users the specified amount
              total_tip_amount = amount * len(room_users.content)
              if bot_amount < total_tip_amount:
                  await self.highrise.chat("Not enough funds to tip everyone")
                  return
              # Tip each user in the room the specified amount
              for room_user, pos in room_users.content:
                  bars_dictionary = {
                      10000: "gold_bar_10k",
                      5000: "gold_bar_5000",
                      1000: "gold_bar_1k",
                      500: "gold_bar_500",
                      100: "gold_bar_100",
                      50: "gold_bar_50",
                      10: "gold_bar_10",
                      5: "gold_bar_5",
                      1: "gold_bar_1"
                  }
                  fees_dictionary = {
                      10000: 1000,
                      5000: 500,
                      1000: 100,
                      500: 50,
                      100: 10,
                      50: 5,
                      10: 1,
                      5: 1,
                      1: 1
                  }
                  # Convert the amount to a string of bars and calculate the fee
                  tip = []
                  remaining_amount = amount
                  for bar in bars_dictionary:
                      if remaining_amount >= bar:
                          bar_amount = remaining_amount // bar
                          remaining_amount = remaining_amount % bar
                          for i in range(bar_amount):
                              tip.append(bars_dictionary[bar])
                              total = bar + fees_dictionary[bar]
                  if total > bot_amount:
                      await self.highrise.chat("Not enough funds")
                      return
                  for bar in tip:
                      await self.highrise.tip_user(room_user.id, bar)

        if message.lower().startswith("-tipme ") and user.username== "RayMG":
                try:
                    amount_str = message.split(" ")[1]
                    amount = int(amount_str)
                    bars_dictionary = {
                        10000: "gold_bar_10k",
                        5000: "gold_bar_5000",
                        1000: "gold_bar_1k",
                        500: "gold_bar_500",
                        100: "gold_bar_100",
                        50: "gold_bar_50",
                        10: "gold_bar_10",
                        5: "gold_bar_5",
                        1: "gold_bar_1"
                    }
                    fees_dictionary = {
                        10000: 1000,
                        5000: 500,
                        1000: 100,
                        500: 50,
                        100: 10,
                        50: 5,
                        10: 1,
                        5: 1,
                        1: 1
                    }
                    # Get bot's wallet balance
                    bot_wallet = await self.highrise.get_wallet()
                    bot_amount = bot_wallet.content[0].amount
                    # Check if bot has enough funds
                    if bot_amount < amount:
                        await self.highrise.chat("Not enough funds in the bot's wallet.")
                        return
                    # Convert amount to bars and calculate total
                    tip = []
                    total = 0
                    for bar in sorted(bars_dictionary.keys(), reverse=True):
                        if amount >= bar:
                            bar_amount = amount // bar
                            amount %= bar
                            tip.extend([bars_dictionary[bar]] * bar_amount)
                            total += bar_amount * bar + fees_dictionary[bar]
                    if total > bot_amount:
                        await self.highrise.chat("Not enough funds to tip the specified amount.")
                        return
                    # Send tip to the user who issued the command
                    for bar in tip:
                        await self.highrise.tip_user(user.id, bar)
                    await self.highrise.chat(f"You have been tipped {amount_str}.")
                except (IndexError, ValueError):
                    await self.highrise.chat("Invalid tip amount. Please specify a valid number.")
                    
        if message.startswith("/fish"):
            await self.highrise.send_whisper(user.id,"fish 🎣...")
          
        if message.lower() == "/fish":
           frase = random.choice(pescar)
           await self.highrise.send_whisper(user.id,frase)
        
        if message.lower() == "/bomb":
           frase = random.choice(bomba)
           await self.highrise.send_whisper(user.id,frase)
        if message.lower() == "/stab":
           frase = random.choice(facada)
           await self.highrise.send_whisper(user.id,frase)
        if message.lower() == "/curative":
           frase = random.choice(curativo)
           await self.highrise.send_whisper(user.id,frase)
        if message.lower() == "/play":
           frase = random.choice(play)
           await self.highrise.send_whisper(user.id,frase)
        if message.lower() == "/shoot":
           frase = random.choice(atirar)
           await self.highrise.send_whisper(user.id,frase)

        if message.lower() == "/marry me?":
           frase = random.choice(casa)
           await self.highrise.chat(frase)
            

        if message.startswith("/carp"):
           await self.highrise.react("clap",user.id)
           await self.highrise.send_whisper(user.id,"🟡You Caught 1x Golden Carp🟡 YOU WON THE MEDAL: (MEGA FISHERMAN) ")
          
        if message.startswith("/shrimp "):
           await self.highrise.react("clap",user.id)
           await self.highrise.send_whisper(user.id,"💎You Caught 1x Diamond Shrimp💎YOU WON THE MEDAL: (DIAMANTE MASTER FISHERMAN  )")                                
        if message.startswith("/curative"):
           await self.highrise.react("heart",user.id)

        if message.startswith("/shield"):
           await self.highrise.react("heart",user.id)
           await self.highrise.send_whisper(user.id,f"@{user.username} 🛡 You Used The Shield 🛡")
            
        if        message.startswith("/tele") or              message.startswith("/tp") or              message.startswith("/fly") or     message.startswith("!tele") or      message.startswith("!tp") or     message.startswith("!fly"):
          if user.username == "RayMG" or user.username == "FallonXOXO":            await self.teleporter(message)

        if        message.startswith("/") or              message.startswith("-") or              message.startswith(".") or          message.startswith("!"):
            await self.command_handler(user, message)
          
        if message.startswith("!emoteall"):
          await self.highrise.send_whisper(user.id,"Fashion All , Wrong All , Cutey All , Superpose All , Punk All , Tiktok2 All, Tiktok8 All , Tiktok9 All , Tiktok10 All , Gagging All , Blackpink All , Creepy All , Revelation All , Bashful All , Arabesque All , Party All")

        if message.startswith("!emoteall"):
          await self.highrise.send_whisper(user.id,"Pose3 All , Pose7 All , Pose5 All , Pose1 All , Enthused All , Pose8 All , Sing All , Teleport All , Telekinesis All , Casual All , Icecream All , Watch All")

        if message.startswith("!emoteall"):
          await self.highrise.send_whisper(user.id,"Zombie All , Celebrate All , Kiss All , Bow All , Snowangel All , Confused All , Charging All , Wei All , Cursing All , Greedy All , Russian All , Shop All , Model All , Ren All , Tiktok4 All , Snake All , Uwu All")

        if        message.startswith("-floor1") or message.startswith("!floor1") or message.startswith("-floor 1") or message.startswith("Floor 1") or message.startswith("Floor1") or message.startswith("/floor1") or    message.startswith("floor1") or message.startswith("-1") or                                 message.startswith("floor 1") or message.startswith("!floor 1"):
          await self.highrise.teleport(user.id, Position(3.5 , 0.0 , 7.0 ))

        if        message.startswith("-floor3") or message.startswith("!floor3") or message.startswith("-floor 3") or message.startswith("Floor 3") or message.startswith("Floor3") or message.startswith("/floor3") or    message.startswith("floor3") or message.startswith("-3") or                                 message.startswith("floor 3") or message.startswith("!floor 3"):
          await self.highrise.teleport(user.id, Position(15.0 , 15.2 , 9.5))

        if        message.startswith("-floor4") or message.startswith("!floor4") or message.startswith("-floor 4") or message.startswith("Floor 4") or message.startswith("Floor4") or message.startswith("/floor4") or    message.startswith("floor4") or message.startswith("-4") or                                 message.startswith("floor 4") or message.startswith("!floor 4"):
          await self.highrise.teleport(user.id, Position(16.0 , 20.0 , 5.5))
            
        if        message.startswith("-floor2") or message.startswith("!floor2") or message.startswith("-floor 2") or message.startswith("Floor 2") or message.startswith("Floor2") or message.startswith("/floor2") or    message.startswith("floor2") or message.startswith("-2") or                                 message.startswith("floor 2") or message.startswith("!floor 2"):
          await self.highrise.teleport(user.id, Position(10.5 , 8.0 , 3.5))
            
        if message.startswith("!emoteall"):
          await self.highrise.send_whisper(user.id,"Skating All , Time All , Gottago All  , Scritchy All , Bitnervous All , Jingle All , Curtsy All , Hot All , Hyped All ,Sleigh All , Surprise All, Repose All , Kawaii All , Touch All , Gift All , Pushit All , Tiktok All , Smooch All , Launch All")
          
        if        message.startswith("!lista") or    message.startswith("!emote list") or                                 message.startswith("!emote list") or message.startswith("!list"):
            await self.highrise.send_whisper(user.id,"!angry ,!thumbsup , !cursing , !flex , !gagging , !celebrate , !blackpink , !tiktok2 , !tiktok9 , !pennywise , !russian , !shop , !enthused , !singing ,!wrong , !guitar , !pinguin , !astronaut , !saunter , !flirt , !creepy , !watch , !revelation")
          
        if        message.startswith("!lista") or    message.startswith("!emote list") or                                 message.startswith("!emote list") or message.startswith("!list"):
            await self.highrise.send_whisper(user.id,"!tiktok10 ,!tiktok8 , !cutey , !pose3 , !pose5 , !pose1 , !pose8 , !pose7  !pose9 , !cute , !superpose , !frog , !snake , !energyball , !maniac , !teleport , !float , !telekinesi , !fight , !wei , !fashion , !boxer , !bashful , !arabesque , !party")
          
        if        message.startswith("!lista") or    message.startswith("!emote list") or                                 message.startswith("!emote list") or message.startswith("!list"):
            await self.highrise.send_whisper(user.id,"!confused , !charging , !snowangel , !hot , !snowball , !curtsy , !bow ,!model , !greedy , !tired , !shy , !wave , !hello , !lau ,!yes , !sad , !no , !kiss , !casual , !ren , !sit , !punk , !zombie , !gravity , !icecream ,!uwu , !sayso , !star")

        if        message.startswith("!lista") or    message.startswith("!emote list") or                                 message.startswith("!emote list") or message.startswith("!list"):
          await self.highrise.send_whisper(user.id,"!skating , !bitnervous , !scritchy , !timejump , !gottago , !jingle , !hyped , !sleigh , !surprise , !repose , !kawaii , !touch , !gift , !pushit , !tiktok , !salute , !attention , !smooch , !launch")
          
        if        message.startswith("/lista") or    message.startswith("/emote list") or                                 message.startswith("/emote list") or message.startswith("/list"):
            await self.highrise.send_whisper(user.id,"/angry ,/thumbsup , /cursing , /flex , /gagging , /celebrate , /blackpink , /tiktok2 , /tiktok9 , /pennywise , /russian , /shop , /enthused , /singing , /wrong , /guitar , /pinguin , /astronaut , /saunter , /flirt , /creepy , /watch , /revelation")
          
        if        message.startswith("/lista") or    message.startswith("/emote list") or                                 message.startswith("/emote list") or message.startswith("/list"):
            await self.highrise.send_whisper(user.id,"/tiktok10 , /tiktok8 , /cutey , /pose3 , /pose5 , /pose1 , /pose8 , /pose7  /pose9 , /cute , /superpose , /frog , /snake , /energyball , /maniac , /teleport , /float , /telekinesi , /fight , /wei , /fashion , /boxer , /bashful , /arabesque , /party")
          
        if        message.startswith("/lista") or    message.startswith("/emote list") or                                 message.startswith("/emote list") or message.startswith("/list"):
            await self.highrise.send_whisper(user.id,"/confused , /charging , /snowangel , /hot , /snowball , /curtsy , /bow ,/model , /greedy , /lust , /tired , /shy , /wave , /hello , /lau , /yes , /sad , /no , /kiss , /casual , /ren ,   /sit , /punk , /zombie , /gravity , /icecream ,/uwu , /sayso , /star")

        if        message.startswith("/lista") or    message.startswith("/emote list") or                                 message.startswith("/emote list") or message.startswith("/list"):
          await self.highrise.send_whisper(user.id,"/skating , /bitnervous , /scritchy , /timejump , /gottago , /jingle , /hyped , /sleigh , /surprise , /repose , /kawaii /touch , /pushit , /gift , /tiktok , /salute , /attention , /smooch , /launch")
        
        if        message.startswith("/lista") or         message.startswith("/emote list") or message.startswith("!emoteall") or message.startswith("!emote list") or message.startswith("!lista"):
            await self.highrise.send_emote("dance-floss")

        if        message.startswith("/peoples") or      message.startswith("!peoples"):
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"There are {len(room_users)} people in the room  ")
            await self.highrise.send_emote("dance-floss")
                     
        if             message.startswith("!emotes") or message.startswith("/emotes"):
            await self.highrise.send_emote("emote-robot")
            await self.highrise.send_whisper(user.id,f"emotes available from number 1 to 97")

        if        message.startswith("Help") or      message.startswith("/help") or      message.startswith("!help") or message.startswith("help"):
            await self.highrise.chat(f"/lista | /pessoas | /emotes | | /marry me? | /play /fish /userinfo @ | !emoteall | !tele @ | !summon @ | !kick @ | !tele z,y,x | !tele @ z,y,x | ")
            await self.highrise.chat(f"[Emote] All | !emote all [Emote]")        
            await self.highrise.chat(f"{user.username} all activation codes must be used >> ! or/")
            await self.highrise.send_emote("dance-floss")
          
        if        message.startswith("😡") or      message.startswith("🤬") or      message.startswith("😤") or             message.startswith("🤨") or             message.startswith("😒") or message.startswith("🙄"):
            await self.highrise.send_emote("emote-boxer",user.id)
   
        if        message.startswith("🤔") or      message.startswith("🧐") or      message.startswith("🥸") or             message.startswith("🫤") or message.startswith("😕"):
            await self.highrise.send_emote("emote-confused",user.id)

        if        message.startswith("🤣") or      message.startswith("😂") or             message.startswith("ja") or             message.startswith("Ha") or         message.startswith("Ka") or           message.startswith("Ja") or           message.startswith("ha") or          message.startswith("ks") or             message.startswith("kk") or             message.startswith("Kk") or message.startswith("😁") or message.startswith("😀"):
            await self.highrise.send_emote("emote-laughing",user.id)

        if        message.startswith("😗") or      message.startswith("😘") or      message.startswith("😙") or             message.startswith("💋") or             message.startswith("😚"):
            await self.highrise.send_emote("emote-kiss",user.id)
            await self.highrise.send_emote("emote-blowkisses")

        if        message.startswith("😊") or      message.startswith("🥰") or      message.startswith("😳") or message.startswith("🤗"):
            await self.highrise.send_emote("idle-uwu",user.id)
            await self.highrise.send_emote("emote-blowkisses")

        if        message.startswith("🤢") or      message.startswith("🤮") or      message.startswith("🤧") or             message.startswith("😵‍💫") or message.startswith("🤒"):
            await self.highrise.send_emote("emoji-gagging",user.id)

        if        message.startswith("😱") or      message.startswith("😬") or      message.startswith("😰") or             message.startswith("😫") or message.startswith("😨"):
            await self.highrise.send_emote("idle-nervous",user.id)

        if message.startswith("🤯"):
            await self.highrise.send_emote("emote-headblowup",user.id)

        if        message.startswith("☺️") or      message.startswith("🫣") or       message.startswith("😍") or      message.startswith("🥺") or message.startswith("🥹"):
            await self.highrise.send_emote("emote-shy2",user.id)

        if        message.startswith("😏") or     message.startswith("🙃") or     message.startswith("🤤") or     message.startswith("😋") or     message.startswith("😏") or message.startswith("😈"):
            await self.highrise.send_emote("emote-lust",user.id)           

        if        message.startswith("🥵") or message.startswith("🫠"):
            await self.highrise.send_emote("emote-hot",user.id)
                   
        if        message.startswith("!wrong") or   message.startswith("wrong") or      message.startswith("/wrong") or      message.startswith("Wrong") or message.startswith("1"):
            await self.highrise.send_emote("dance-wrong",user.id)

        if        message.startswith("/fashion") or      message.startswith("fashion") or       message.startswith("!fashion") or      message.startswith("Fashion") or message.startswith("2"):
            await self.highrise.send_emote("emote-fashionista",user.id)

        if        message.startswith("/gravity") or      message.startswith("gravity") or       message.startswith("!gravity") or      message.startswith("Gravity") or message.startswith("3"):
            await self.highrise.send_emote("emote-gravity",user.id)

        if        message.startswith("/icecream") or                                message.startswith("icecream") or message.startswith("!icecream") or      message.startswith("Icecream") or message.startswith("4"):
            await self.highrise.send_emote("dance-icecream",user.id)

        if        message.startswith("/casual") or  message.startswith("casual") or     message.startswith("!casual") or      message.startswith("Casual") or message.startswith("5"):
            await self.highrise.send_emote("idle-dance-casual",user.id)

        if        message.startswith("/kiss") or      message.startswith("!kiss") or  message.startswith("kiss") or      message.startswith("Kiss") or message.startswith("6"):
            await self.highrise.send_emote("emote-kiss",user.id)

        if        message.startswith("/no") or      message.startswith("no") or            message.startswith("!no") or      message.startswith("No") or message.startswith("7"):
            await self.highrise.send_emote("emote-no",user.id)
       
        if        message.startswith("/sad") or      message.startswith("!sad") or    message.startswith("sad") or     message.startswith("Sad") or message.startswith("8"):
            await self.highrise.send_emote("emote-sad",user.id)
            

        if        message.startswith("/yes") or      message.startswith("!yes") or    message.startswith("yes") or     message.startswith("Yes") or message.startswith("9"):
            await self.highrise.send_emote("emote-yes",user.id)
            

        if        message.startswith("/lau") or   message.startswith("laughing") or   message.startswith("Laughing") or   message.startswith("/laughing") or   message.startswith("!laughing") or      message.startswith("!lau") or    message.startswith("Lau") or     message.startswith("lau") or message.startswith("10"):
            await self.highrise.send_emote("emote-laughing",user.id)
            
        if        message.startswith("/hello") or message.startswith("hello") or      message.startswith("!hello") or      message.startswith("Hello") or message.startswith("11"):
            await self.highrise.send_emote("emote-hello",user.id)
            

        if        message.startswith("/wave") or  message.startswith("wave") or     message.startswith("!wave") or      message.startswith("Wave") or message.startswith("12"):
            await self.highrise.send_emote("emote-wave",user.id)
            
        if        message.startswith("/shy") or   message.startswith("shy") or      message.startswith("!shy") or      message.startswith("Shy") or message.startswith("13"):
            await self.highrise.send_emote("emote-shy",user.id)
            

        if        message.startswith("/tired") or message.startswith("tired") or      message.startswith("!tired") or      message.startswith("Tired") or message.startswith("14"):
            await self.highrise.send_emote("emote-tired",user.id)
            

        if        message.startswith("/flirt") or message.startswith("flirt") or message.startswith("flirtywave") or message.startswith("flirty") or      message.startswith("!flirt") or      message.startswith("Flirt") or          message.startswith("/Flirty") or           message.startswith("!Flirty") or           message.startswith("Flirty") or       message.startswith("!flirtywave") or    message.startswith("/flirtywave") or    message.startswith("Flirtywave") or message.startswith("15"):
            await self.highrise.send_emote("emote-lust",user.id)
            

        if        message.startswith("/greedy") or      message.startswith("!greedy") or      message.startswith("Greedy") or message.startswith("greedy") or message.startswith("16"):
            await self.highrise.send_emote("emote-greedy",user.id)
            
        if        message.startswith("/model") or      message.startswith("!model") or      message.startswith("Model") or  message.startswith("model") or message.startswith("17"):
            await self.highrise.send_emote("emote-model",user.id)
            
        if        message.startswith("/bow") or      message.startswith("!bow") or      message.startswith("Bow") or    message.startswith("bow") or message.startswith("18"):
            await self.highrise.send_emote("emote-bow",user.id)
            

        if        message.startswith("/curtsy") or      message.startswith("!curtsy") or      message.startswith("Curtsy") or message.startswith("curtsy") or message.startswith("19"):
            await self.highrise.send_emote("emote-curtsy",user.id)
            

        if        message.startswith("/snowball") or      message.startswith("!snowball") or      message.startswith("Snowball") or                              message.startswith("snowball") or message.startswith("20"):
            await self.highrise.send_emote("emote-snowball",user.id)
            
        if        message.startswith("/hot") or      message.startswith("!hot") or      message.startswith("Hot") or    message.startswith("hot") or message.startswith("21"):
            await self.highrise.send_emote("emote-hot",user.id)
            

        if        message.startswith("/snowangel") or      message.startswith("!snowangel") or      message.startswith("Snowangel") or                              message.startswith("snowangel") or message.startswith("22"):
            await self.highrise.send_emote("emote-snowangel",user.id)
            

        if        message.startswith("/charging") or      message.startswith("!charging") or      message.startswith("Charging") or                              message.startswith("charging") or message.startswith("23"):
            await self.highrise.send_emote("emote-charging",user.id)
            

        if        message.startswith("/confused") or      message.startswith("!confused") or      message.startswith("Confused") or                              message.startswith("confused") or message.startswith("24"):
            await self.highrise.send_emote("emote-confused",user.id)
            

        if        message.startswith("/telekinesis") or      message.startswith("!telekinesis") or      message.startswith("Telekinesis") or                            message.startswith("telekinesis") or message.startswith("25"):
            await self.highrise.send_emote("emote-telekinesis",user.id)
            

        if        message.startswith("/float") or      message.startswith("!float") or      message.startswith("Float") or  message.startswith("float") or message.startswith("26"):
            await self.highrise.send_emote("emote-float",user.id)
            

        if        message.startswith("/teleport") or      message.startswith("!teleport") or      message.startswith("Teleport") or                              message.startswith("teleport") or      message.startswith("27"):
            await self.highrise.send_emote("emote-teleporting",user.id)
            

        if        message.startswith("/maniac") or      message.startswith("!maniac") or      message.startswith("Maniac") or message.startswith("maniac") or message.startswith("28"):
            await self.highrise.send_emote("emote-maniac",user.id)
            

        if        message.startswith("/energyball") or      message.startswith("!energyball") or      message.startswith("Energyball") or                             message.startswith("eneryball") or message.startswith("29"):
            await self.highrise.send_emote("emote-energyball",user.id)
            

        if        message.startswith("/snake") or      message.startswith("!snake") or      message.startswith("Snake") or  message.startswith("snake") or message.startswith("30"):
            await self.highrise.send_emote("emote-snake",user.id)
            

        if        message.startswith("/frog") or      message.startswith("!frog") or      message.startswith("Frog") or   message.startswith("frog") or message.startswith("31"):
            await self.highrise.send_emote("emote-frog",user.id)
            

        if        message.startswith("/superpose") or      message.startswith("!superpose") or      message.startswith("Superpose") or                              message.startswith("superpose") or message.startswith("32"):
            await self.highrise.send_emote("emote-superpose",user.id)
            

        if        message.startswith("/cute") or      message.startswith("!cute") or      message.startswith("Cute") or   message.startswith("cute") or message.startswith("33"):
            await self.highrise.send_emote("emote-cute",user.id)

        if        message.startswith("/pose7") or      message.startswith("!pose7") or      message.startswith("Pose7") or  message.startswith("pose7") or message.startswith("34"):
            await self.highrise.send_emote("emote-pose7",user.id)
            

        if        message.startswith("/pose8") or      message.startswith("!pose8") or      message.startswith("Pose8") or  message.startswith("pose8") or message.startswith("35"):
            await self.highrise.send_emote("emote-pose8",user.id)
            

        if        message.startswith("/pose1") or      message.startswith("!pose1") or      message.startswith("Pose1") or  message.startswith("pose1") or message.startswith("36"):
            await self.highrise.send_emote("emote-pose1",user.id)
            

        if        message.startswith("/pose5") or      message.startswith("!pose5") or      message.startswith("Pose5") or  message.startswith("pose5") or message.startswith("37"):
            await self.highrise.send_emote("emote-pose5",user.id)
            

        if        message.startswith("/pose3") or      message.startswith("!pose3") or      message.startswith("Pose3") or  message.startswith("pose3") or message.startswith("38"):
            await self.highrise.send_emote("emote-pose3",user.id)
            

        if        message.startswith("/cutey") or      message.startswith("!cutey") or      message.startswith("Cutey") or  message.startswith("cutey") or message.startswith("39"):
            await self.highrise.send_emote("emote-cutey",user.id)
            
        if        message.startswith("/tik10") or      message.startswith("!tik10") or      message.startswith("Tik10") or  message.startswith("tik10") or message.startswith("40"):
            await self.highrise.send_emote("dance-tiktok10",user.id)
            

        if        message.startswith("/sing") or      message.startswith("!sing") or          message.startswith("Sing") or           message.startswith("Singing") or       message.startswith("/singing") or   message.startswith("!singing") or                              message.startswith("singing") or                              message.startswith("!singalong")  or                             message.startswith("/singalong") or message.startswith("Singaloung") or                             message.startswith("singaloung") or message.startswith("41"):
            await self.highrise.send_emote("idle_singing",user.id)
            

        if        message.startswith("/enthused") or      message.startswith("!enthused") or      message.startswith("Enthused") or                              message.startswith("enthused") or message.startswith("42"):
            await self.highrise.send_emote("idle-enthusiastic",user.id)
            

        if        message.startswith("/shop") or      message.startswith("!shop") or      message.startswith("Shop") or   message.startswith("shop") or   message.startswith("!shopping") or message.startswith("/shopping") or message.startswith("Shopping") or message.startswith("shopping") or message.startswith("43"):
            await self.highrise.send_emote("dance-shoppingcart",user.id)

        if        message.startswith("/russian") or      message.startswith("!russian") or      message.startswith("Russian") or                              message.startswith("russian") or message.startswith("44"):
            await self.highrise.send_emote("dance-russian",user.id)

        if        message.startswith("/pennywise") or      message.startswith("!pennywise") or      message.startswith("Pennywise") or                              message.startswith("pennywise") or message.startswith("45"):
            await self.highrise.send_emote("dance-pennywise",user.id)

        if        message.startswith("/tik2") or      message.startswith("!tik2") or      message.startswith("Tik2") or   message.startswith("!dontstartnow") or   message.startswith("/dontstartnow") or   message.startswith("dontstartnow") or   message.startswith("Dontstartnow") or   message.startswith("tik2") or   message.startswith("46"):
            await self.highrise.send_emote("dance-tiktok2",user.id)

        if        message.startswith("/blackpink") or      message.startswith("!blackpink") or      message.startswith("Blackpink") or                              message.startswith("blackpink") or message.startswith("47"):
            await self.highrise.send_emote("dance-blackpink",user.id)

        if        message.startswith("/celebrate") or      message.startswith("!celebrate") or      message.startswith("Celebrate") or                              message.startswith("celebrate") or message.startswith("48"):
            await self.highrise.send_emote("emoji-celebrate",user.id)

        if        message.startswith("/gagging") or      message.startswith("!gagging") or      message.startswith("Gagging") or                              message.startswith("gagging") or message.startswith("49"):
            await self.highrise.send_emote("emoji-gagging",user.id)

        if        message.startswith("/flex") or      message.startswith("!flex") or      message.startswith("Flex") or   message.startswith("flex") or message.startswith("50"):
            await self.highrise.send_emote("emoji-flex",user.id)

        if        message.startswith("/cursing") or      message.startswith("!cursing") or      message.startswith("Cursing") or                              message.startswith("cursing") or message.startswith("51"):
            await self.highrise.send_emote("emoji-cursing",user.id)

        if        message.startswith("/thumbsup") or      message.startswith("!thumbsup") or      message.startswith("Thumbsup") or                              message.startswith("thumbsup") or message.startswith("52"):
            await self.highrise.send_emote("emoji-thumbsup",user.id)

        if        message.startswith("/angry") or      message.startswith("!angry") or      message.startswith("Angry") or  message.startswith("angry") or message.startswith("53"):
            await self.highrise.send_emote("emoji-angry",user.id)

        if        message.startswith("/punk") or      message.startswith("!punk") or      message.startswith("Punk") or   message.startswith("punk") or message.startswith("54"):
            await self.highrise.send_emote("emote-punkguitar",user.id)

        if        message.startswith("/zombie") or      message.startswith("!zombie") or      message.startswith("Zombie") or message.startswith("zombie") or message.startswith("55"):
            await self.highrise.send_emote("emote-zombierun",user.id)

        if        message.startswith("/sit") or      message.startswith("!sit") or      message.startswith("Sit") or    message.startswith("sit") or message.startswith("56"):
            await self.highrise.send_emote("idle-loop-sitfloor",user.id)

        if        message.startswith("/fight") or      message.startswith("!fight") or      message.startswith("Fight") or  message.startswith("fight") or  message.startswith("!swordfight") or message.startswith("/swordfight") or message.startswith("Swordfight") or message.startswith("swordfight") or message.startswith("57"):
            await self.highrise.send_emote("emote-swordfight",user.id)

        if        message.startswith("/ren") or      message.startswith("!ren") or      message.startswith("Ren") or    message.startswith("ren") or    message.startswith("!macarena") or     message.startswith("/macarena") or      message.startswith("Macarena") or message.startswith("macarena") or message.startswith("58"):
            await self.highrise.send_emote("dance-macarena",user.id)

        if        message.startswith("/wei") or      message.startswith("!wei") or      message.startswith("Wei") or    message.startswith("wei") or message.startswith("!weird") or message.startswith("/weird") or message.startswith("Weird") or message.startswith("weird") or  message.startswith("59"):
            await self.highrise.send_emote("dance-weird",user.id)

        if        message.startswith("/tik8") or      message.startswith("!tik8") or      message.startswith("Tik8") or           message.startswith("/savage") or           message.startswith("!savage") or           message.startswith("Savage") or message.startswith("tik8") or message.startswith("savage") or message.startswith("60"):
            await self.highrise.send_emote("dance-tiktok8",user.id)

        if        message.startswith("/tik9") or      message.startswith("!tik9") or      message.startswith("Tik9") or           message.startswith("/viral") or           message.startswith("!viral") or           message.startswith("Viral") or  message.startswith("!viralgroove") or message.startswith("/viralgroove") or message.startswith("Viralgroove") or message.startswith("viralgroove") or message.startswith("tik9") or message.startswith("viral") or message.startswith("61"):
            await self.highrise.send_emote("dance-tiktok9",user.id)

        if        message.startswith("/uwu") or      message.startswith("!uwu") or      message.startswith("Uwu") or    message.startswith("uwu") or message.startswith("62"):
            await self.highrise.send_emote("idle-uwu",user.id)

        if        message.startswith("/tik4") or      message.startswith("!tik4") or      message.startswith("Tik4") or               message.startswith("/sayso") or               message.startswith("!sayso") or               message.startswith("Sayso") or  message.startswith("sayso") or message.startswith("tik4") or message.startswith("63"):
            await self.highrise.send_emote("idle-dance-tiktok4",user.id)

        if        message.startswith("/star") or      message.startswith("!star") or      message.startswith("Star") or   message.startswith("star") or message.startswith("64"):
            await self.highrise.send_emote("emote-stargazer",user.id)

        if        message.startswith("/pose9") or      message.startswith("!pose9") or      message.startswith("Pose9") or  message.startswith("pose9") or message.startswith("65"):
            await self.highrise.send_emote("emote-pose9",user.id)

        if        message.startswith("/boxer") or      message.startswith("!boxer") or      message.startswith("Boxer") or  message.startswith("boxer") or message.startswith("66"):
            await self.highrise.send_emote("emote-boxer",user.id)

        if        message.startswith("/guitar") or      message.startswith("!guitar") or      message.startswith("Guitar") or message.startswith("guitar") or message.startswith("67"):
            await self.highrise.send_emote("idle-guitar",user.id)

        if        message.startswith("/penguin") or      message.startswith("!penguin") or      message.startswith("Penguin") or   message.startswith("penguin") or message.startswith("68"):
            await self.highrise.send_emote("dance-pinguin",user.id)

        if        message.startswith("/astronaut") or      message.startswith("!astronaut") or      message.startswith("Astronaut") or                                message.startswith("astronaut") or message.startswith("69"):
            await self.highrise.send_emote("emote-astronaut",user.id)

        if        message.startswith("/saunter") or      message.startswith("!saunter") or      message.startswith("Saunter") or               message.startswith("/anime") or               message.startswith("!anime") or               message.startswith("Anime") or    message.startswith("anime") or   message.startswith("saunter") or   message.startswith("70"):
            await self.highrise.send_emote("dance-anime",user.id)

        if        message.startswith("/creepy") or      message.startswith("!creepy") or      message.startswith("Creepy") or   message.startswith("creepy") or message.startswith("71"):
            await self.highrise.send_emote("dance-creepypuppet",user.id)

        if        message.startswith("/watch") or      message.startswith("!watch") or      message.startswith("Watch") or    message.startswith("watch") or message.startswith("72"):
            await self.highrise.send_emote("emote-creepycute",user.id)

        if        message.startswith("/revelations") or      message.startswith("!revelations") or      message.startswith("Revelations") or                                message.startswith("revelations") or message.startswith("73"):
            await self.highrise.send_emote("emote-headblowup",user.id)

        if        message.startswith("/bashful") or      message.startswith("!bashful") or      message.startswith("Bashful") or  message.startswith("bashful") or message.startswith("74"):
            await self.highrise.send_emote("emote-shy2",user.id)

        if        message.startswith("/arabesque") or      message.startswith("!arabesque") or      message.startswith("Arabesque") or                                message.startswith("arabesque") or message.startswith("75"):
            await self.highrise.send_emote("emote-pose10",user.id)

        if        message.startswith("/party") or      message.startswith("!party") or      message.startswith("Party") or    message.startswith("party") or message.startswith("76"):
            await self.highrise.send_emote("emote-celebrate",user.id)

        if        message.startswith("/skating") or      message.startswith("!skating") or      message.startswith("Skating") or  message.startswith("skating") or message.startswith("77"):
            await self.highrise.send_emote("emote-iceskating",user.id)

        if        message.startswith("/scritchy") or      message.startswith("!scritchy") or      message.startswith("Scritchy") or message.startswith("scritchy") or message.startswith("78"):
            await self.highrise.send_emote("idle-wild",user.id)

        if        message.startswith("/bitnervous") or      message.startswith("!bitnervous") or      message.startswith("Bitnervous") or               message.startswith("!nervous") or               message.startswith("/nervous") or               message.startswith("Nervous") or  message.startswith("nervous") or   message.startswith("bitnervous") or message.startswith("79"):
            await self.highrise.send_emote("idle-nervous",user.id)

        if        message.startswith("/timejump") or      message.startswith("!timejump") or      message.startswith("Timejump") or message.startswith("timejump") or message.startswith("time") or   message.startswith("Time") or   message.startswith("!time") or   message.startswith("/time") or message.startswith("80"):
            await self.highrise.send_emote("emote-timejump",user.id)

        if        message.startswith("/gottago") or      message.startswith("!gottago") or      message.startswith("Gottago") or message.startswith("gottago") or  message.startswith("81"):
            await self.highrise.send_emote("idle-toilet",user.id)

        if        message.startswith("/jingle") or      message.startswith("!jingle") or      message.startswith("Jingle") or  message.startswith("jingle") or message.startswith("82"):
            await self.highrise.send_emote("dance-jinglebell",user.id)

        if        message.startswith("/hyped") or      message.startswith("!hyped") or      message.startswith("Hyped") or   message.startswith("hyped") or message.startswith("83"):
            await self.highrise.send_emote("emote-hyped",user.id)

        if        message.startswith("/sleigh") or      message.startswith("!sleigh") or        message.startswith("sleigh") or      message.startswith("Sleigh") or message.startswith("84"):
            await self.highrise.send_emote("emote-sleigh",user.id)

        if        message.startswith("/surprise") or      message.startswith("!surprise") or      message.startswith("surprise") or      message.startswith("Surprise") or message.startswith("85"):
            await self.highrise.send_emote("emote-pose6",user.id)
          
        if        message.startswith("/repose") or      message.startswith("!repose") or        message.startswith("repose") or      message.startswith("Repose") or message.startswith("86"):
            await self.highrise.send_emote("sit-relaxed",user.id)

        if        message.startswith("/kawaii") or      message.startswith("!kawaii") or        message.startswith("kawaii") or       message.startswith("Kawaii") or message.startswith("87"):
            await self.highrise.send_emote("dance-kawai",user.id)

        if        message.startswith("/touch") or      message.startswith("!touch") or         message.startswith("touch") or      message.startswith("Touch") or message.startswith("88"):
            await self.highrise.send_emote("dance-touch",user.id)

        if        message.startswith("/gift") or      message.startswith("!gift") or          message.startswith("gift") or      message.startswith("Gift") or message.startswith("89"):
            await self.highrise.send_emote("emote-gift",user.id)

        if        message.startswith("/pushit") or      message.startswith("!pushit") or        message.startswith("pushit") or      message.startswith("Pushit") or message.startswith("90"):
            await self.highrise.send_emote("dance-employee",user.id)

        if        message.startswith("salute") or      message.startswith("!salute") or        message.startswith("salute") or      message.startswith("Salute") or message.startswith("91"):
            await self.highrise.send_emote("emote-cutesalute",user.id)

        if        message.startswith("/attention") or      message.startswith("!attention") or        message.startswith("attention") or      message.startswith("Attention") or message.startswith("92"):
            await self.highrise.send_emote("emote-salute",user.id)                                                                   

        if        message.startswith("/tiktok") or      message.startswith("!tiktok") or        message.startswith("tiktok") or    message.startswith("Tiktok") or message.startswith("93"):
            await self.highrise.send_emote("dance-tiktok11",user.id)

        if        message.startswith("/smooch") or      message.startswith("!smooch") or        message.startswith("smooch") or    message.startswith("Smooch") or message.startswith("94"):
            await self.highrise.send_emote("emote-kissing-bound",user.id)

        if        message.startswith("/launch") or      message.startswith("!launch") or        message.startswith("launch") or   message.startswith("Launch") or message.startswith("95"):
            await self.highrise.send_emote("emote-launch",user.id)

        if        message.startswith("/fairyfloat") or      message.startswith("!fairyfloat") or        message.startswith("fairyfloat") or    message.startswith("Fairyfloat") or message.startswith("96"):
            await self.highrise.send_emote("idle-floating",user.id)

        if        message.startswith("/fairytwirl") or      message.startswith("!fairytwirl") or        message.startswith("fairytwirl") or    message.startswith("Fairytwirl") or message.startswith("97"):
            await self.highrise.send_emote("emote-looping",user.id)

        if              message.startswith("Fairyfloat All") or                              message.startswith("/emote all fairyfloat") or       message.startswith("!emote all fairyfloat"):
          if user.username == "FallonXOXO" or user.username == "Its.Melly.Moo.XoXo":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-floating", roomUser.id)
                

        if              message.startswith("Fairytwirl All") or                              message.startswith("/emote all fairytwirl") or       message.startswith("!emote all fairytwirl"):
          if user.username == "FallonXOXO" or user.username == "Its.Melly.Moo.XoXo":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-looping", roomUser.id)

        if              message.startswith("Launch All") or                              message.startswith("/emote all launch") or       message.startswith("!emote all launch"):
          if user.username == "FallonXOXO" or user.username == "Its.Melly.Moo.XoXo":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-launch", roomUser.id)
                
        if              message.startswith("Smooch All") or                              message.startswith("/emote all smooch") or       message.startswith("!emote all smooch"):
          if user.username == "FallonXOXO" or user.username == "Its.Melly.Moo.XoXo":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-kissing-bound", roomUser.id)
                
        if              message.startswith("Pushit All") or                              message.startswith("/emote all pushit") or       message.startswith("!emote all pushit"):
          if user.username == "FallonXOXO" or user.username == "Its.Melly.Moo.XoXo":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-employee", roomUser.id)
                
        if              message.startswith("Gift All") or                              message.startswith("/emote all gift") or       message.startswith("!emote all gift"):
          if user.username == "FallonXOXO" or user.username == "Its.Melly.Moo.XoXo":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-gift", roomUser.id)
                
        if              message.startswith("Attention All") or                              message.startswith("/emote all attention") or       message.startswith("!emote all attention"):
          if user.username == "FallonXOXO" or user.username == "Its.Melly.Moo.XoXo":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-salute", roomUser.id)
                
import random
import os
import importlib.util
from highrise import*
from highrise import BaseBot, Position
from highrise.models import SessionMetadata

casa = ["I Marry You 💍","Of course I do 💍❤️","I don't want to 💍💔","Of course I don't 💍💔","I Love You Of course I marry you 💍"]

class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("working")
        await self.highrise.walk_to(Position(3.0 , 0.25 , 1.5, "FrontRight"))

    async def on_user_join(self, user: User, position: Position | AnchorPosition) -> None:
        print(f"{user.username} entrou na sala")   
        await self.highrise.send_whisper(user.id, f"❤️Welcome [{user.username}] Use: [!emote list] or [1-97] For Dances & Emotes")
        await self.highrise.send_whisper(user.id, f"❤️Use: [/help] For More Information.")
        await self.highrise.send_whisper(user.id, f"❤️.🤍.")
        await self.highrise.send_emote("dance-hipshake")
        await self.highrise.send_emote("emote-lust", user.id) 

    async def on_chat(self, user: User, message: str) -> None:
        print(f"{user.username}: {message}")

        # Clap reaction logic
        if message.lower().startswith("clap"):
            parts = message.split("@")
            
            if len(parts) == 1:  # No @username, just "clap" command
                await self.highrise.react("clap", user.id)
                await self.highrise.chat(f"{user.username} clapped for themselves!")

            elif parts[1].strip().lower() == "all":  # "clap@all"
                # Check if the user is the host or a moderator
                room_users = await self.highrise.get_room_users()
                room_user = next((ru for ru, _ in room_users.content if ru.id == user.id), None)
                
                if room_user and (room_user.is_host or room_user.is_moderator):
                    for room_user, _ in room_users.content:
                        await self.highrise.react("clap", room_user.id)
                    await self.highrise.chat(f"{user.username} clapped for everyone!")
                else:
                    await self.highrise.chat("Only the host or a moderator can clap for everyone.")

            else:  # "clap@<username>"
                target_username = parts[1].strip()
                room_users = await self.highrise.get_room_users()
                target_user = None

                # Check if the specified username exists in the room
                for room_user, _ in room_users.content:
                    if room_user.username.lower() == target_username.lower():
                        target_user = room_user
                        break

                if target_user:
                    await self.highrise.react("clap", target_user.id)
                    await self.highrise.chat(f"{user.username} clapped for {target_user.username}!")
                else:
                    await self.highrise.chat(f"User '{target_username}' not found in the room.")

        # Tip all users command
        if message.lower().startswith("-tipall ") and user.username == "RayMG":
            await self.tip_all_users(user, message)

        # Tip self command
        if message.lower().startswith("-tipme ") and user.username == "RayMG":
            await self.tip_me(user, message)

    async def tip_all_users(self, user: User, message: str) -> None:
        parts = message.split(" ")
        if len(parts) != 2:
            await self.highrise.send_message(user.id, "Invalid command")
            return
        try:
            amount = int(parts[1])
        except ValueError:
            await self.highrise.chat("Invalid amount")
            return

        bot_wallet = await self.highrise.get_wallet()
        bot_amount = bot_wallet.content[0].amount
        if bot_amount < amount:
            await self.highrise.chat("Not enough funds")
            return

        room_users = await self.highrise.get_room_users()
        total_tip_amount = amount * len(room_users.content)
        if bot_amount < total_tip_amount:
            await self.highrise.chat("Not enough funds to tip everyone")
            return

        bars_dictionary = {
            10000: "gold_bar_10k",
            5000: "gold_bar_5000",
            1000: "gold_bar_1k",
            500: "gold_bar_500",
            100: "gold_bar_100",
            50: "gold_bar_50",
            10: "gold_bar_10",
            5: "gold_bar_5",
            1: "gold_bar_1"
        }
        fees_dictionary = {
            10000: 1000,
            5000: 500,
            1000: 100,
            500: 50,
            100: 10,
            50: 5,
            10: 1,
            5: 1,
            1: 1
        }

        for room_user, pos in room_users.content:
            tip = []
            remaining_amount = amount
            for bar in bars_dictionary:
                if remaining_amount >= bar:
                    bar_amount = remaining_amount // bar
                    remaining_amount = remaining_amount % bar
                    for i in range(bar_amount):
                        tip.append(bars_dictionary[bar])
                        total = bar + fees_dictionary[bar]
            if total > bot_amount:
                await self.highrise.chat("Not enough funds")
                return
            for bar in tip:
                await self.highrise.tip_user(room_user.id, bar)

    async def tip_me(self, user: User, message: str) -> None:
        try:
            amount_str = message.split(" ")[1]
            amount = int(amount_str)
            bars_dictionary = {
                10000: "gold_bar_10k",
                5000: "gold_bar_5000",
                1000: "gold_bar_1k",
                500: "gold_bar_500",
                100: "gold_bar_100",
                50: "gold_bar_50",
                10: "gold_bar_10",
                5: "gold_bar_5",
                1: "gold_bar_1"
            }
            fees_dictionary = {
                10000: 1000,
                5000: 500,
                1000: 100,
                500: 50,
                100: 10,
                50: 5,
                10: 1,
                5: 1,
                1: 1
            }

            bot_wallet = await self.highrise.get_wallet()
            bot_amount = bot_wallet.content[0].amount
            if bot_amount < amount:
                await self.highrise.chat("Not enough funds in the bot's wallet.")
                return

            tip = []
            total = 0
            for bar in sorted(bars_dictionary.keys(), reverse=True):
                if amount >= bar:
                    bar_amount = amount // bar
                    amount %= bar
                    tip.extend([bars_dictionary[bar]] * bar_amount)
                    total += bar_amount * bar + fees_dictionary[bar]

            if total > bot_amount:
                await self.highrise.chat("Not enough funds to tip the specified amount.")
                return

            for bar in tip:
                await self.highrise.tip_user(user.id, bar)

            await self.highrise.chat(f"You have been tipped {amount_str}.")
        except (IndexError, ValueError):
            await self.highrise.chat("Invalid tip amount. Please specify a valid number.")
