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
        print(f"Received whisper from {user.username}: {message}")  # Debugging line
        # Check if the message is not empty
        if message:
            # Check if the user is a host or moderator
            if user.role in ["host", "moderator"]:  # Adjust these roles based on your application's definition
                # Broadcast the message to the public room
                await self.highrise.send_message(f"{user.username} whispered: {message}")
            else:
                # Inform the user they do not have permission to use this command
                await self.highrise.send_whisper(user.id, "❌ You do not have permission to use this command.")

    async def on_user_message(self, user: User, message: str) -> None:
        # Check if the message is directed to the bot
        if message.startswith('MGBot'):  # Changed to listen for 'MGBot' instead of '@MGBot'
            # Extract the actual message following the bot mention
            actual_message = message[len('MGBot'):].strip()
            if user.role in ["host", "moderator"]:  # Adjust these roles as needed
                # Broadcast the message to the public room
                await self.highrise.send_message(f"{user.username} said: {actual_message}")
            else:
                # Inform the user they do not have permission to send this command
                await self.highrise.send_whisper(user.id, "❌ You do not have permission to use this command.")

# Ensure the bot is initialized correctly
