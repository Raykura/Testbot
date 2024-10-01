import random
import os
import importlib.util
from highrise import *
from highrise import BaseBot, Position
from highrise.models import SessionMetadata

class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("working")
        await self.highrise.walk_to(Position(3.0, 0.25, 1.5, "FrontRight"))

    async def on_user_join(self, user: User, position: Position | AnchorPosition) -> None:
        print(f"{user.username} entrou na sala")   
        await self.highrise.send_whisper(user.id, f"❤️Welcome [{user.username}] Use: [!emote list] or [1-97] For Dances & Emotes")
        await self.highrise.send_whisper(user.id, f"❤️Use: [/help] For More Information.")
        await self.highrise.send_whisper(user.id, f"❤️.🤍.")
        await self.highrise.send_emote("dance-hipshake")
        await self.highrise.send_emote("emote-lust", user.id)

    async def on_chat(self, user: User, message: str) -> None:
        print(f"{user.username}: {message}")

        # Tip all users (Only for specific user)
        if message.lower().startswith("-tipall ") and user.username == "RayMG":
            parts = message.split(" ")
            if len(parts) != 2:
                await self.highrise.send_message(user.id, "Invalid command")
                return
            try:
                amount = int(parts[1])
            except:
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

        # Tip specific user
        if message.lower().startswith("-tipme ") and user.username == "RayMG":
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
                await self.highrise.chat("Invalid tip amount. Please specify a valid 

        # Clap to specific user or multiple claps to user
        if message.lower().startswith("clap@") or message.lower().startswith("clap."):
            parts = message.split("@") if "@" in message else message.split(".")
            if len(parts) >= 2:
                target_username = parts[1].split()[0]
                clap_count = 1  # Default to 1 clap
                if len(parts[1].split()) > 1 and parts[1].split()[1].isdigit():
                    clap_count = min(int(parts[1].split()[1]), 10)  # Limit to 10 claps
                for _ in range(clap_count):
                    await self.highrise.react("clap", target_username)

        # Clap all users (host or moderator only)
        if (message.startswith("!clapall") or message.startswith("-clapall")) and user.is_host_or_moderator:
            try:
                clap_count = int(message.split()[1])
                clap_count = min(clap_count, 10)  # Limit to 10 claps
                room_users = await self.highrise.get_room_users()
                for room_user in room_users.content:
                    for _ in range(clap_count):
                        await self.highrise.react("clap", room_user.id)
            except:
                await self.highrise.chat("Invalid command format.")

        # Heart to specific user or multiple hearts to user
        if message.lower().startswith("heart@") or message.lower().startswith("heart."):
            parts = message.split("@") if "@" in message else message.split(".")
            if len(parts) >= 2:
                target_username = parts[1].split()[0]
                heart_count = 1  # Default to 1 heart
                if len(parts[1].split()) > 1 and parts[1].split()[1].isdigit():
                    heart_count = min(int(parts[1].split()[1]), 10)  # Limit to 10 hearts
                for _ in range(heart_count):
                    await self.highrise.react("heart", target_username)

        # Heart all users (host or moderator only)
        if (message.startswith("!heartall") or message.startswith("-heartall")) and user.is_host_or_moderator:
            try:
                heart_count = int(message.split()[1])
                heart_count = min(heart_count, 10)  # Limit to 10 hearts
                room_users = await self.highrise.get_room_users()
                for room_user in room_users.content:
                    for _ in range(heart_count):
                        await self.highrise.react("heart", room_user.id)
            except:
                await self.highrise.chat("Invalid command format.")

        # Check bot's wallet balance
        if message.lower() == "!iwallet":
            bot_wallet = await self.highrise.get_wallet()
            bot_amount = bot_wallet.content[0].amount
            await self.highrise.chat(f"Bot's wallet balance: {bot_amount}")
