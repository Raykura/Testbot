import random
import os
import importlib.util
from highrise import *
from highrise import BaseBot, Position
from highrise.models import SessionMetadata

casa = ["I Marry You 💍", "Of course I do 💍❤️", "I don't want to 💍💔", "Of course I don't 💍💔", "I Love You Of course I marry you 💍"]

class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("working")
        await self.highrise.walk_to(Position(3.0, 0.25, 1.5, "FrontRight"))

    async def on_user_join(self, user: User, position: Position | AnchorPosition) -> None:
        print(f"{user.username} entrou na sala")
        await self.highrise.send_whisper(user.id, f"❤️Welcome [{user.username}] Use: [!emote list] or [1-97] For Dances & Emotes")
        await self.highrise.send_whisper(user.id, f"❤️Use: [/help] For More Informations.")
        await self.highrise.send_whisper(user.id, f"❤type -4 .to go up 🤍.")
        await self.highrise.send_emote("dance-hipshake")
        await self.highrise.send_emote("emote-lust", user.id)

    async def on_chat(self, user: User, message: str) -> None:
        print(f"{user.username}: {message}")

        # Follow logic
        if message.lower().startswith("follow@"):
            parts = message.split("@")
            if len(parts) == 2:
                target_username = parts[1].strip()
                # Check if the user is host or moderator
                room_users = await self.highrise.get_room_users()
                room_user = next((ru for ru, _ in room_users.content if ru.id == user.id), None)

                if room_user and (room_user.is_host or room_user.is_moderator):
                    target_user = None
                    # Find the specified user in the room
                    for room_user, _ in room_users.content:
                        if room_user.username.lower() == target_username.lower():
                            target_user = room_user
                            break
                    
                    if target_user:
                        # Follow the target user (implement follow logic as needed)
                        await self.highrise.follow(target_user.id)
                        await self.highrise.chat(f"{user.username} is now following {target_user.username}!")
                    else:
                        await self.highrise.chat(f"User '{target_username}' not found in the room.")
                else:
                    await self.highrise.chat("Only the host or a moderator can follow users.")

        # Handle whispers with !whisper or -whisper
        if message.lower().startswith("!whisper ") or message.lower().startswith("-whisper "):
            # Extract the message content
            whisper_message = message.split(" ", 1)[1].strip()  # Remove the command prefix and get the rest of the message
            # Check if the user is host or moderator
            room_users = await self.highrise.get_room_users()
            room_user = next((ru for ru, _ in room_users.content if ru.id == user.id), None)

            if room_user and (room_user.is_host or room_user.is_moderator):
                await self.highrise.chat(f"{user.username} whispered: {whisper_message}")
            else:
                await self.highrise.chat("Only hosts or moderators can send whispers.")
