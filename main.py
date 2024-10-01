# main.py

from highrise import BaseBot, User, Position, SessionMetadata
from follow import follow, stop  # Importing follow and stop functions
import asyncio

class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("Bot is working")
        await self.highrise.walk_to(Position(3.0, 0.25, 1.5, "FrontRight"))

    async def on_user_join(self, user: User, position: Position | AnchorPosition) -> None:
        print(f"{user.username} entered the room")
        await self.highrise.send_whisper(user.id, f"❤️Welcome [{user.username}]! Use: [!follow @username] to follow someone.")

    async def on_chat(self, user: User, message: str) -> None:
        print(f"{user.username}: {message}")

        # Follow logic
        if message.lower().startswith("!follow@"):
            parts = message.split("@")
            if len(parts) == 2:
                target_username = parts[1].strip()
                room_users = await self.highrise.get_room_users()
                room_user = next((ru for ru, _ in room_users.content if ru.id == user.id), None)

                if room_user and (room_user.is_host or room_user.is_moderator):
                    await follow(self, user, target_username)
                else:
                    await self.highrise.chat("Only the host or a moderator can follow users.")

        # Stop following logic
        if message.lower().startswith("!stop@"):
            parts = message.split("@")
            if len(parts) == 2:
                target_username = parts[1].strip()
                room_users = await self.highrise.get_room_users()
                room_user = next((ru for ru, _ in room_users.content if ru.id == user.id), None)

                if room_user and (room_user.is_host or room_user.is_moderator):
                    await stop(self, user, target_username)
                else:
                    await self.highrise.chat("Only the host or a moderator can stop following users.")

# Start the bot (Add your bot startup code here)
