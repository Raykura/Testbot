import os
import importlib.util

class YourBot:
    
    async def teleport_user_next_to(self, target_username: str, requester_user: User) -> None:
        try:
            # Get the position of the requester_user
            room_users = await self.highrise.get_room_users()
            requester_position = next(
                (position for user, position in room_users.content if user.id == requester_user.id), None
            )

            if requester_position is None:
                print(f"Requester {requester_user.username} is not in the room.")
                return
            
            # Find the target user and their position
            target_user = next(
                (user for user, position in room_users.content if user.username.lower() == target_username.lower()), None
            )
            
            if target_user is None:
                print(f"Target user {target_username} not found.")
                return

            # Teleport the target user next to the requester
            new_z = requester_position.z + 1  # Example: Move +1 on the z-axis (upwards)
            await self.teleport(target_user, Position(requester_position.x, requester_position.y, new_z, requester_position.facing))
        except Exception as e:
            print(f"An error occurred while teleporting {target_username} next to {requester_user.username}: {e}")

    async def teleporter(self, message: str) -> None:
        """
        Teleports the user to the specified user or coordinate.
        Usage: /teleport <username> <x,y,z>
        """
        try:
            command, username, coordinate = message.split(" ")
        except ValueError:
            print("Invalid command format.")
            return

        # Check if the user is in the room
        room_users = (await self.highrise.get_room_users()).content
        user_id = next((user[0].id for user in room_users if user[0].username.lower() == username.lower()), None)

        if user_id is None:
            print(f"User {username} not found in the room.")
            return

        # Check if the coordinate is in the correct format (x,y,z)
        try:
            x, y, z = map(float, coordinate.split(","))
        except ValueError:
            print("Invalid coordinates format.")
            return

        # Teleport the user to the specified coordinate
        await self.highrise.teleport(user_id=user_id, dest=Position(x, y, z))

    async def send_hearts(self, message: str, user: User) -> None:
        """Send hearts to a user or to everyone in the room."""
        try:
            # Check if user is moderator or room owner
            if user.role not in ['moderator', 'owner']:
                print("Only moderators or room owners can use this command.")
                return
            
            parts = message.split(" ")
            heart_count = int(parts[1]) if len(parts) > 1 else 1  # Default to 1 heart if not specified
            target_username = parts[2] if len(parts) > 2 else None  # Target user, optional
            
            if heart_count < 1 or heart_count > 100:
                print("You can send between 1 to 100 hearts.")
                return
            
            hearts = "❤️" * heart_count
            
            if target_username:
                await self.highrise.send_whisper(target_username, hearts)  # Send to specific user
            else:
                room_users = await self.highrise.get_room_users()
                for user in room_users.content:
                    await self.highrise.send_whisper(user[0].id, hearts)  # Send to all users
            
        except ValueError:
            print("Invalid heart count.")
        except Exception as e:
            print(f"An error occurred while sending hearts: {e}")

    async def echo_message(self, message: str, user: User) -> None:
        """Echo the whispered message in public chat."""
        await self.highrise.send_message(message)

    async def follow_user(self, user_id: str, requester_user: User) -> None:
        """Follow a user by user ID."""
        await self.highrise.follow(user_id)

    async def vip_command(self, username: str, requester_user: User) -> None:
        """Grant VIP status to a user."""
        # Only moderators or room owners can give VIP status
        if requester_user.role not in ['moderator', 'owner']:
            print("Only moderators or room owners can assign VIP status.")
            return
        
        # Logic to mark the user as VIP (implementation depends on your specific use case)
        # For example, you could add the user to a VIP list or modify their permissions.
        print(f"{username} has been given VIP status.")

    async def command_handler(self, user: User, message: str) -> None:
        parts = message.split(" ")
        command = parts[0][1:]  # Remove the leading slash
        functions_folder = "functions"

        # Check if the function exists in the module
        for file_name in os.listdir(functions_folder):
            if file_name.endswith(".py"):
                module_name = file_name[:-3]  # Remove the '.py' extension
                module_path = os.path.join(functions_folder, file_name)

                # Load the module
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                # Check if the function exists in the module
                if hasattr(module, command) and callable(getattr(module, command)):
                    function = getattr(module, command)
                    await function(self, user, message)
                    return  # Exit once the function is executed

        print(f"No matching function found for command: {command}")

    async def on_whisper(self, user: User, message: str) -> None:
        print(f"{user.username} whispered: {message}")

        if any(message.startswith(prefix) for prefix in ["/tele", "/tp", "/fly", "!tele", "!tp", "!fly"]):
            if user.username in ["FallonXOXO", "Its.Melly.Moo.XoXo", "sh1n1gam1699", "Abbie_38", "hidinurbasement", "@emping", "BabygirlFae", "RayMG"]:
                await self.teleporter(message)

        if message.startswith("/") or message.startswith("-") or message.startswith(".") or message.startswith("!"):
            await self.command_handler(user, message)

        if any(message.startswith(command) for command in ["Summon", "Summom", "!summom", "/summom", "!summon", "/summon"]):
            if user.username in ["FallonXOXO", "iced_yu", "@Its.Melly.Moo.XoXo", "mghaa"]:
                target_username = message.split("@")[-1].strip()
                await self.teleport_user_next_to(target_username, user)

        if any(message.startswith(keyword) for keyword in ["Carteira", "Wallet", "wallet", "carteira"]):
            if user.username in ["FallonXOXO", "RayMG"]:
                wallet = (await self.highrise.get_wallet()).content
                await self.highrise.send_whisper(user.id, f"AMOUNT: {wallet[0].amount} {wallet[0].type}")
                await self.highrise.send_emote("emote-blowkisses")

        # Echo the whispered message to public chat
        await self.echo_message(message, user)

        # Follow command
        if message.startswith("follow@"):
            user_id = message.split("@")[1]
            await self.follow_user(user_id, user)

        # VIP command
        if message.startswith("!vip "):
            target_username = message.split(" ", 1)[1]
            await self.vip_command(target_username, user)

        # Send hearts command
        if message.startswith("Iheart"):
            await self.send_hearts(message, user)

    async def on_user_move(self, user: User, pos: Position) -> None:
        print(f"{user.username} moved to {pos}")

    async def on_emote(self, user: User, emote_id: str, receiver: User | None) -> None:
        print(f"{user.username} emoted: {emote_id}")
