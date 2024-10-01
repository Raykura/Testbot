import random
import os
import importlib.util
from highrise import *
from highrise import BaseBot, Position
from highrise.models import SessionMetadata

casa = ["I Marry You 💍", "Of course I do 💍❤️", "I don't want to 💍💔", "Of course I don't 💍💔", "I Love You Of course I marry you 💍"]

class MGBot(BaseBot):
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

        # Clap reaction logic with specified number of claps
        if message.lower().startswith("clap"):
            parts = message.split("@")
            
            if len(parts) == 1:  # No @username, just "clap" command (self clap)
                await self.clap(user, user, 1)  # Default 1 clap for self

            elif parts[1].strip().lower().startswith("all"):  # "clap@all <number>"
                await self.clap_for_all(user, parts)

            else:  # "clap@<username> <number>"
                await self.clap_for_user(user, parts)

        # Check wallet command
        if message.lower().startswith("!wallet"):
            await self.display_wallet(user)

    async def on_whisper(self, user: User, message: str):
        # Check if the user is the host (RayMG) or a moderator
        if user.username == "RayMG" or user.is_moderator:
            if message.startswith("-w") or message.startswith("!w"):
                await self.send_room_message(f"{user.username} whispered: {message[2:].strip()}")
            else:
                await self.send_room_message(f"{user.username} whispered: {message}")

    async def clap_for_all(self, user: User, parts: list) -> None:
        # Check if the user is the host or a moderator
        room_users = await self.highrise.get_room_users()
        room_user = next((ru for ru, _ in room_users.content if ru.id == user.id), None)
        
        if room_user and (room_user.is_host or room_user.is_moderator):
            # Default to 1 clap if no amount is specified
            num_claps = 1
            if len(parts) > 1 and parts[1].strip().lower().split(" ")[-1].isdigit():
                num_claps = int(parts[1].strip().lower().split(" ")[-1])

            for room_user, _ in room_users.content:
                await self.clap(user, room_user, num_claps)

            await self.highrise.chat(f"{user.username} clapped for everyone {num_claps} times!")
        else:
            await self.highrise.chat("Only the host or a moderator can clap for everyone.")

    async def clap_for_user(self, user: User, parts: list) -> None:
        target_username = parts[1].split(" ")[0].strip()  # Get the target username
        num_claps = 1  # Default to 1 clap

        if len(parts[1].split(" ")) > 1:  # If a number of claps is specified
            try:
                num_claps = int(parts[1].split(" ")[1].strip())
            except ValueError:
                await self.highrise.chat("Invalid number of claps.")
                return

        room_users = await self.highrise.get_room_users()
        target_user = None

        # Find the specified user in the room
        for room_user, _ in room_users.content:
            if room_user.username.lower() == target_username.lower():
                target_user = room_user
                break

        if target_user:
            await self.clap(user, target_user, num_claps)
            await self.highrise.chat(f"{user.username} clapped for {target_user.username} {num_claps} times!")
        else:
            await self.highrise.chat(f"User '{target_username}' not found in the room.")

    async def clap(self, sender: User, target: User, num_claps: int) -> None:
        for _ in range(num_claps):
            await self.highrise.react("clap", target.id)

    # Tip all users command
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

    # Display the bot's wallet.
