import streamlit as st
from your_bot_module import MGBot  # Replace with the actual path to your bot module

# Configuration
API_KEY = "432f23df3fc5076fe6c95ade994a533c9d473ecdb56acc31346899a94d6aaa6d"
ROOM_ID = "66d2726b2e80dd1f614c4dbb"

# Initialize your bot
bot = MGBot(highrise=YourHighriseClient(API_KEY), room_id=ROOM_ID)

# Streamlit UI
st.title("MGBot Control Panel")

# Add Streamlit components to interact with the bot, e.g., buttons, input fields
# Example: if st.button("Start Bot"):
#     await bot.start()
