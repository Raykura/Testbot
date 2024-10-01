# follow.py

from highrise import BaseBot, User, Position
import asyncio

async def follow(self: BaseBot, user: User, target_username: str) -> None:
    async def following_loop() -> None:
        while True:
            # Get the user's position
            room_users = (await self.highrise.get_room_users()).content
            user_position = None
            
            for room_user, position in room_users:
                if room_user.username.lower() == target_username.lower():
                    user_position = position
                    break

            if user_position is None:
                await self.highrise.chat(f"User '{target_username}' not found.")
                return
            
            if not isinstance(user_position, AnchorPosition):
                await self.highrise.walk_to(Position(user_position.x + 1, user_position.y, user_position.z))
            await asyncio.sleep(0.5)

    taskgroup = self.highrise.tg
    task_list = list(taskgroup._tasks)

    # Check if the following loop is already running
    for task in task_list:
        if task.get_name() == f"following_loop_{target_username}":
            await self.highrise.chat(f"You are already following {target_username}.")
            return

    # Create a new following task
    task = taskgroup.create_task(following_loop())
    task.set_name(f"following_loop_{target_username}")
    
    await self.highrise.chat(f"Coming to follow you, {target_username}! 🚶‍♂️")


async def stop(self: BaseBot, user: User, target_username: str) -> None:
    taskgroup = self.highrise.tg
    task_list = list(taskgroup._tasks)

    for task in task_list:
        if task.get_name() == f"following_loop_{target_username}":
            task.cancel()
            await self.highrise.chat(f"Stopped following {target_username} 🥲")
            return
            
    await self.highrise.chat(f"You're not following {target_username}.")
