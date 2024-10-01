# functions/vip_mod.py

async def add_vip(bot, user, message):
    parts = message.split(" ")
    if len(parts) != 2:
        await bot.highrise.chat("Usage: !vip @username")
        return
    
    user_mention = parts[1]
    username = extract_username(user_mention)
    
    if username:
        # Implement logic to grant VIP status, e.g., add to a list or database
        await bot.highrise.chat(f"{username} has been granted VIP status!")
    else:
        await bot.highrise.chat("User not found.")

async def add_mod(bot, user, message):
    parts = message.split(" ")
    if len(parts) != 2:
        await bot.highrise.chat("Usage: !mod @username")
        return
    
    user_mention = parts[1]
    username = extract_username(user_mention)
    
    if username:
        # Implement logic to grant Moderator status
        await bot.highrise.chat(f"{username} has been granted Moderator status!")
    else:
        await bot.highrise.chat("User not found.")

def extract_username(user_mention: str) -> str:
    """Extract username from the mention."""
    if user_mention.startswith("@"):
        return user_mention[1:]  # Remove '@' from mention
    return None
