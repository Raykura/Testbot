import random
from highrise import BaseBot, Position
from highrise.models import User, SessionMetadata

class HighriseBot(BaseBot):
    def __init__(self):
        super().__init__()
        self.moderators = []  # List of moderator usernames
        self.host = None  # Set the host username

    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("Bot started and ready to go!")
        await self.highrise.walk_to(Position(3.0, 0.25, 1.5, "FrontRight"))

    async def on_user_join(self, user: User, position: Position) -> None:
        print(f"{user.username} joined the room")
        await self.highrise.send_whisper(user.id, f"❤️ Welcome {user.username}! Type /help for commands.")
        await self.highrise.send_emote("dance-hipshake")

    async def on_chat(self, user: User, message: str) -> None:
        print(f"{user.username}: {message}")

        # Respond to the help command
        if message.lower() == "!help":
            await self.highrise.send_message(user.id, "Available commands: !heart, !tipall, !tipme, etc.")

        # Heart command handling
        if message.lower().startswith("!heart"):
            await self.send_heart(message, user)

        # Tip all command handling
        if message.lower().startswith("-tipall ") and user.username == "RayMG":
            await self.handle_tip_all(user, message)

        # Tip me command handling
        if message.lower().startswith("-tipme ") and user.username == "RayMG":
            await self.handle_tip_me(user, message)

    async def send_heart(self, message: str, user: User) -> None:
        # Parse the heart command
        parts = message.split()
        if len(parts) == 3 and parts[1].isdigit() and user.username in self.moderators:
            count = int(parts[1])
            recipient = parts[2].replace('@', '')  # Extract the username
            
            if count < 1 or count > 10:
                await self.highrise.send_message(user.id, "You can send between 1 to 10 hearts.")
                return
            
            heart_message = "❤️" * count  # Create heart message
            await self.highrise.send_message(recipient, heart_message)
            await self.highrise.send_message(user.id, f"Sent {count} hearts to {recipient}!")
        else:
            await self.highrise.send_message(user.id, "Usage: !heart [number]@[username] (1-10)")

    async def handle_tip_all(self, user: User, message: str) -> None:
        parts = message.split(" ")
        if len(parts) != 2:
            await self.highrise.send_message(user.id, "Invalid command")
            return
        # Check if the amount is valid
        try:
            amount = int(parts[1])
        except ValueError:
            await self.highrise.chat("Invalid amount")
            return
        # Check if the bot has the amount
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
        for room_user in room_users.content:
            tip = []
            remaining_amount = amount
            for bar in bars_dictionary:
                if remaining_amount >= bar:
                    bar_amount = remaining_amount // bar
                    remaining_amount = remaining_amount % bar
                    for _ in range(bar_amount):
                        tip.append(bars_dictionary[bar])
            total = amount + sum(fees_dictionary[bar] for bar in tip)
            if total > bot_amount:
                await self.highrise.chat("Not enough funds")
                return
            for bar in tip:
                await self.highrise.tip_user(room_user.id, bar)

    async def handle_tip_me(self, user: User, message: str) -> None:
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

# To run the bot
if __name__ == "__main__":
    import asyncio
    from highrise import Highrise

    highrise = Highrise(token="YOUR_TOKEN")  # Replace with your token
    bot = HighriseBot()
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bot.start(highrise))
