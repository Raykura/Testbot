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
        # Check if the message starts with the command
        if message.startswith("!whisper ") or message.startswith("-whisper "):
            # Extract the actual message
            actual_message = message.split(maxsplit=1)[1] if len(message.split()) > 1 else ""
            # Check if the user is a host or moderator
            if user.role in ["host", "moderator"]:  # Adjust roles as per your application's role definitions
                # Display the message in the public room
                await self.highrise.send_message(f"{user.username} whispered: {actual_message}")
            else:
                await self.highrise.send_whisper(user.id, "❌ You do not have permission to use this command.")
