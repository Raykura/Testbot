import random
import os
import importlib.util
from highrise import*
from highrise import BaseBot,Position
from highrise.models import SessionMetadata

# List of random flirty messages
flirty_messages = [
    "You're amazing! Sending you a heart ❤️",
    "Just wanted to let you know how wonderful you are! 💖",
    "You make my day brighter! Here’s a heart for you! 💕",
    "You have a special place in my heart! ❤️",
    "Is your name Google? Because you have everything I’m searching for! 💘",
    "You're like a fine wine; you get better with time! 🍷❤️",
    "Sending you hearts because you're so lovely! 💗",
]

class MGBot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("Bot is online")
        await self.highrise.walk_to(Position(3.0, 0.25, 1.5, "FrontRight"))

    async def on_user_join(self, user: User, position: Position | AnchorPosition) -> None:
        print(f"{user.username} entrou na sala")
        await self.highrise.send_whisper(user.id, f"❤️ Welcome [{user.username}] Use: [!emote list] or [1-97] For Dances & Emotes")

    async def on_chat(self, user: User, message: str) -> None:
        print(f"{user.username}: {message}")

        # Check for heart commands
        if message.startswith("!heart"):
            await self.handle_heart_command(user, message)

        # Check for clap commands
        elif message.startswith("!clap"):
            await self.handle_clap_command(user, message)

        # Check for heart reactions from any user
        elif message.lower().startswith("heart@"):
            target_user_id = message.split('@')[1].strip()
            await self.send_heart_to_user(user, target_user_id)

        # Check for clap reactions from any user
        elif message.lower().startswith("clap@"):
            target_user_id = message.split('@')[1].strip()
            await self.send_clap_to_user(user, target_user_id)

    async def handle_heart_command(self, user: User, message: str) -> None:
        parts = message.split()
        if len(parts) == 3 and parts[1].lower() == "all":
            try:
                num_hearts = int(parts[2])
                if self.is_authorized(user) and 1 <= num_hearts <= 20:
                    await self.send_hearts_to_all(user, num_hearts)
                else:
                    await self.highrise.chat("You are not authorized or the number of hearts is invalid (1-20).")
            except ValueError:
                await self.highrise.chat("Invalid number of hearts.")

        elif len(parts) == 2 and "@" in parts[1]:  # Check for sending heart to a specific user
            target_user_id = parts[1].split('@')[1].strip()
            await self.send_heart_to_user(user, target_user_id, parts[2] if len(parts) > 2 else None)

    async def handle_clap_command(self, user: User, message: str) -> None:
        parts = message.split()
        if len(parts) == 3 and parts[1].lower() == "all":
            try:
                num_claps = int(parts[2])
                if self.is_authorized(user) and 1 <= num_claps <= 20:
                    await self.send_claps_to_all(user, num_claps)
                else:
                    await self.highrise.chat("You are not authorized or the number of claps is invalid (1-20).")
            except ValueError:
                await self.highrise.chat("Invalid number of claps.")

        elif len(parts) == 2 and "@" in parts[1]:  # Check for sending clap to a specific user
            target_user_id = parts[1].split('@')[1].strip()
            await self.send_clap_to_user(user, target_user_id)

    async def send_hearts_to_all(self, user: User, num_hearts: int) -> None:
        room_users = await self.highrise.get_room_users()
        for room_user, _ in room_users.content:
            for _ in range(num_hearts):
                await self.highrise.react("heart", room_user.id)
        await self.highrise.chat(f"{user.username} sent {num_hearts} hearts to everyone!")

    async def send_heart_to_user(self, sender: User, target_user_id: str, amount: str = None) -> None:
        room_users = await self.highrise.get_room_users()
        target_user = None

        # Find the specified user in the room
        for room_user, _ in room_users.content:
            if str(room_user.id) == target_user_id:
                target_user = room_user
                break

        if target_user:
            # Default to 1 heart if no amount specified
            num_hearts = 1
            if amount and amount.isdigit() and int(amount) <= 20:
                num_hearts = int(amount)
            for _ in range(num_hearts):
                await self.highrise.react("heart", target_user.id)  # Send the heart reaction
            flirty_message = random.choice(flirty_messages)
            await self.highrise.chat(f"{sender.username} sent {num_hearts} hearts to {target_user.username}! {flirty_message}")
        else:
            await self.highrise.chat(f"User with ID '{target_user_id}' not found in the room.")

    async def send_claps_to_all(self, user: User, num_claps: int) -> None:
        room_users = await self.highrise.get_room_users()
        for room_user, _ in room_users.content:
            for _ in range(num_claps):
                await self.highrise.react("clap", room_user.id)
        await self.highrise.chat(f"{user.username} clapped for everyone {num_claps} times!")

    async def send_clap_to_user(self, sender: User, target_user_id: str) -> None:
        room_users = await self.highrise.get_room_users()
        target_user = None

        # Find the specified user in the room
        for room_user, _ in room_users.content:
            if str(room_user.id) == target_user_id:
                target_user = room_user
                break

        if target_user:
            await self.highrise.react("clap", target_user.id)
            await self.highrise.chat(f"{sender.username} clapped for {target_user.username}!")
        else:
            await self.highrise.chat(f"User with ID '{target_user_id}' not found in the room.")

    def is_authorized(self, user: User) -> bool:
        return user.username in ["RayMG", "sh1n1gam1699"] or user.is_moderator
