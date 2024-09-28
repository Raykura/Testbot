import os
import importlib.util
from typing import Optional

class MGBot:
    def __init__(self, highrise, room_id: str):
        self.highrise = highrise
        self.room_id = room_id

    async def teleport_user_next_to(self, target_username: str, requester_user: User) -> None:
        try:
            # Get the position of the requester_user
            room_users = await self.highrise.get_room_users()
            requester_position = None
            for user, position in room_users.content:
                if user.id == requester_user.id:
                    requester_position = position
                    break

            # Find the target user and their position
            for user, position in room_users.content:
                if user.username.lower() == target_username.lower():
                    z = requester_position.z
                    new_z = z + 1  # Example: Move +1 on the z-axis (upwards)
                    await self.teleport(user, Position(requester_position.x, requester_position.y, new_z, requester_position.facing))
                    break
        except Exception as e:
            print(f"An error occurred while teleporting {target_username} next to {requester_user.username}: {e}")

    async def teleporter(self, message: str) -> None:
        """Teleports the user to the specified user or coordinate"""
        try:
            command, username, coordinate = message.split(" ")
        except ValueError:
            return

        room_users = (await self.highrise.get_room_users()).content
        user_id = None
        for user in room_users:
            if user[0].username.lower() == username.lower():
                user_id = user[0].id
                break

        if user_id is None:
            return

        try:
            x, y, z = coordinate.split(",")
        except ValueError:
            return

        await self.highrise.teleport(user_id=user_id, dest=Position(float(x), float(y), float(z)))

    async def command_handler(self, user: User, message: str) -> None:
        parts = message.split(" ")
        command = parts[0][1:]
        functions_folder = "functions"

        for file_name in os.listdir(functions_folder):
            if file_name.endswith(".py"):
                module_name = file_name[:-3]
                module_path = os.path.join(functions_folder, file_name)
                
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                if hasattr(module, command) and callable(getattr(module, command)):
                    function = getattr(module, command)
                    await function(self, user, message)

    async def on_whisper(self, user: User, message: str) -> None:
        print(f"{user.username} whispered: {message}")

        if any(message.startswith(cmd) for cmd in ["/tele", "/tp", "/fly", "!tele", "!tp", "!fly"]):
            if user.username in ["FallonXOXO", "Its.Melly.Moo.XoXo", "sh1n1gam1699", "Abbie_38", "hidinurbasement", "@emping", "BabygirlFae", "RayMG"]:
                await self.teleporter(message)

        if message.startswith("/") or message.startswith("-") or message.startswith(".") or message.startswith("!"):
            await self.command_handler(user, message)

        if any(message.startswith(cmd) for cmd in ["Summon", "Summom", "!summom", "/summom", "/summon", "!summon"]):
            if user.username in ["FallonXOXO", "iced_yu", "@Its.Melly.Moo.XoXo", "mghaa"]:
                target_username = message.split("@")[-1].strip()
                await self.teleport_user_next_to(target_username, user)

        if any(message.startswith(cmd) for cmd in ["Carteira", "Wallet", "wallet", "carteira"]):
            if user.username in ["FallonXOXO", "RayMG"]:
                wallet = (await self.highrise.get_wallet()).content
                await self.highrise.send_whisper(user.id, f"AMOUNT : {wallet[0].amount} {wallet[0].type}")
                await self.highrise.send_emote("emote-blowkisses")

        if message.startswith("Iheart"):
            await self.send_heart(message, user)

        if message.startswith("Follow"):
            await self.follow_user(message, user)

        if user.username == "FallonXOXO":  # Only allow specific users to execute the following
            await self.send_public_message(user, message)

    async def send_heart(self, message: str, user: User) -> None:
        # Parse the message for number of hearts and target user
        parts = message.split()
        if len(parts) < 2:
            return
        
        target = parts[1]
        try:
            count = int(parts[2]) if len(parts) > 2 else 1
            if count > 100:
                count = 100
        except ValueError:
            return

        hearts = "❤️" * count
        if target.lower() == "all":
            await self.highrise.send_room_message(f"{user.username} sends {hearts} to everyone!")
        else:
            await self.highrise.send_whisper(target, f"{user.username} sends you {hearts}!")

    async def send_public_message(self, user: User, message: str) -> None:
        await self.highrise.send_room_message(message)

    async def follow_user(self, message: str, user: User) -> None:
        # Extract user ID to follow
        user_id = message.split("@")[-1].strip()
        await self.highrise.follow(user_id)

    async def on_user_move(self, user: User, pos: Position) -> None:
        print(f"{user.username} moved to {pos}")

    async def on_emote(self, user: User, emote_id: str, receiver: Optional[User]) -> None:
        print(f"{user.username} emoted: {emote_id}")
