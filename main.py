import random
from highrise import *
from highrise import BaseBot, Position
from highrise.models import SessionMetadata

class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("Bot is online")
        await self.highrise.walk_to(Position(3.0, 0.25, 1.5, "FrontRight"))

    async def on_user_join(self, user: User, position: Position | AnchorPosition) -> None:
        print(f"{user.username} entered the room")   
        await self.highrise.send_whisper(user.id, f"❤️ Welcome [{user.username}]! Use: [!emote list] or [1-97] For Dances & Emotes")
        await self.highrise.send_whisper(user.id, f"❤️ Use: [/help] For More Information.")
        await self.highrise.send_whisper(user.id, f"❤ Type -4 to go up 🤍.")
        await self.highrise.send_emote("dance-hipshake")
        await self.highrise.send_emote("emote-lust", user.id) 

    async def on_user_whisper(self, user: User, message: str) -> None:
        # Check if the whisper is addressed to the bot
        if message:  # Ensure there is a message
            # Broadcast the message to the public room
            await self.highrise.send_message(f"{user.username} whispered: {message}")

# Ensure the bot is initialized correctly
