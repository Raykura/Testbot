import streamlit as st
import asyncio
from main import MGBot  # Replace 'main' with your bot module name and 'MGBot' with your actual class name

# Bot configuration
API_KEY = "432f23df3fc5076fe6c95ade994a533c9d473ecdb56acc31346899a94d6aaa6d"
ROOM_ID = "66d2726b2e80dd1f614c4dbb"
BOT_NAME = "MGBot"

# Initialize the bot
bot = MGBot(api_key=API_KEY, room_id=ROOM_ID, bot_name=BOT_NAME)

# Function to run the bot
async def run_bot():
    await bot.start()  # This method should handle the connection and bot logic

# Streamlit UI
st.title("MGBot Control Panel")

# Input for user commands
command_input = st.text_input("Enter Command:", "")

if st.button("Send Command"):
    if command_input:
        # Run the command asynchronously
        asyncio.run(bot.command_handler(None, command_input))  # Replace None with actual user if needed
        st.success("Command sent successfully!")
    else:
        st.warning("Please enter a command.")

# Display bot status
st.subheader("Bot Status")
st.text("Bot is running...")  # You can update this to reflect the actual status of your bot

# Optional: Display logs or other information
st.subheader("Logs")
# Use a placeholder or text area to display logs
log_placeholder = st.empty()
log_placeholder.text("Log output will appear here...")  # Update this with real logs as needed

if __name__ == "__main__":
    asyncio.run(run_bot())
