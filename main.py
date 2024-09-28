import random
from highrise import BaseBot, Position
from highrise.models import SessionMetadata

class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("Bot is working")
        await self.highrise.walk_to(Position(3.0, 0.25, 1.5, "FrontRight"))

    async def on_user_join(self, user, position) -> None:
        print(f"{user.username} entered the room")   
        await self.highrise.send_whisper(user.id, f"❤️ Welcome [{user.username}]! Use: [!emote list] or [1-97] For Dances & Emotes")
        await self.highrise.send_whisper(user.id, f"❤️ Use: [/help] For More Information.")
        await self.highrise.send_whisper(user.id, f"❤ Type -4 to go up 🤍.")
        await self.highrise.send_emote("dance-hipshake")
        await self.highrise.send_emote("emote-lust", user.id)

    async def on_chat(self, user, message: str) -> None:
        print(f"{user.username}: {message}")

        # Tip all command
        if message.lower().startswith("-tipall ") and user.username == "RayMG":
            parts = message.split(" ")
            if len(parts) != 2:
                await self.highrise.send_message(user.id, "Invalid command")
                return
            # Checks if the amount is valid
            try:
                amount = int(parts[1])
            except:
                await self.highrise.send_message(user.id, "Invalid amount")
                return
            
            # Checks if the bot has the amount
            bot_wallet = await self.highrise.get_wallet()
            bot_amount = bot_wallet.content[0].amount
            if bot_amount < amount:
                await self.highrise.send_message(user.id, "Not enough funds")
                return
            
            # Get all users in the room
            room_users = await self.highrise.get_room_users()
            # Check if the bot has enough funds to tip all users the specified amount
            total_tip_amount = amount * len(room_users.content)
            if bot_amount < total_tip_amount:
                await self.highrise.send_message(user.id, "Not enough funds to tip everyone")
                return
            
            # Tip each user in the room
            for room_user in room_users.content:
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
                total = sum([bar + fees_dictionary[bar] for bar in tip])

                if total > bot_amount:
                    await self.highrise.send_message(user.id, "Not enough funds")
                    return
                
                for bar in tip:
                    await self.highrise.tip_user(room_user.id, bar)

        # Tip me command
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
                # Get bot's wallet balance
                bot_wallet = await self.highrise.get_wallet()
                bot_amount = bot_wallet.content[0].amount
                # Check if bot has enough funds
                if bot_amount < amount:
                    await self.highrise.send_message(user.id, "Not enough funds in the bot's wallet.")
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
                    await self.highrise.send_message(user.id, "Not enough funds to tip the specified amount.")
                    return
                
                # Send tip to the user who issued the command
                for bar in tip:
                    await self.highrise.tip_user(user.id, bar)

                await self.highrise.send_message(user.id, f"You have been tipped {amount_str}.")
            except (IndexError, ValueError):
                await self.highrise.send_message(user.id, "Invalid tip amount. Please specify a valid number.")

        # Heart command implementation
        if message.lower().startswith("!heart"):
            parts = message.split("@")
            if len(parts) != 2 or len(parts[1]) < 2:
                await self.highrise.send_message(user.id, "Invalid command. Use: !heart [number]@[username]")
                return
                
            # Get the number of hearts
            heart_parts = parts[0].split(" ")
            if len(heart_parts) != 2 or not heart_parts[1].isdigit():
                await self.highrise.send_message(user.id, "Invalid heart amount. Use: !heart [number]@[username]")
                return
            
            heart_count = int(heart_parts[1])
            if heart_count < 1 or heart_count > 10:
                await self.highrise.send_message(user.id, "You can only send between 1 and 10 hearts.")
                return
                
            recipient_username = parts[1]
            # Find the recipient's user ID
            room_users = await self.highrise.get_room_users()
            recipient = next((u for u in room_users.content if u.username == recipient_username), None)
            
            if not recipient:
                await self.highrise.send_message(user.id, "User not found in the room.")
                return

            # Send the hearts
            for _ in range(heart_count):
                await self.highrise.send_emote("heart", recipient.id)

            await self.highrise.send_message(user.id, f"You sent {heart_count} hearts to {recipient_username}.")

if __name__ == "__main__":
    bot = Bot(api_key="432f23df3fc5076fe6c95ade994a533c9d473ecdb56acc31346899a94d6aaa6d", room_id="66d2726b2e80dd1f614c4dbb")
    bot.run()
