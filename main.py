import random
from highrise import *
from highrise import BaseBot, Position
from highrise.models import SessionMetadata

class MGBot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("Bot is online")
        # Bot moves to a specific position in the room
        await self.highrise.walk_to(Position(3.0, 0.25, 1.5, "FrontRight"))

    async def on_user_join(self, user: User, position: Position | AnchorPosition) -> None:
        print(f"{user.username} entered the room")
        # Bot sends welcome whispers to the user
        await self.highrise.send_whisper(user.id, f"❤️ Welcome [{user.username}]! Use: [!emote list] or [1-97] For Dances & Emotes")
        await self.highrise.send_whisper(user.id, f"❤️ Use: [/help] For More Information.")
        await self.highrise.send_whisper(user.id, f"❤ Type -4 to go up 🤍.")
        # Bot performs emotes
        await self.highrise.send_emote("dance-hipshake")
        await self.highrise.send_emote("emote-lust", user.id)

    async def on_whisper(self, user, message: str):
        # Check if the user is the host or a moderator
        if user.is_host or user.is_moderator:  # Assuming these attributes exist
            # If the message starts with "-w" or "!w", broadcast the rest of the message to the room
            if message.startswith("-w") or message.startswith("!w"):
                await self.send_room_message(f"{user.username} whispered: {message[2:].strip()}")
            else:
                # If no command prefix is used, broadcast the entire message
                await self.send_room_message(f"{user.username} whispered: {message}")

# This is the main entry point of the bot. Make sure to initialize and run the bot correctly.
