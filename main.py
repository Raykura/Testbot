import sys
import os
import time
import traceback
from importlib import import_module
from highrise.__main__ import *

# BOT SETTINGS
bot_file_name = "xenoichi"
bot_class_name = "xenoichi"
room_id = "66bad059afeca0c24b497205"
bot_token ="e6d943cc2e2b067461ce74bee5b90daa8aaa6960ddf75330b939a3ef2d1870f5"

my_bot = BotDefinition(getattr(import_module(bot_file_name), bot_class_name)(), room_id, bot_token)

while True:
    try:
        definitions = [my_bot]
        arun(main(definitions))
    except Exception as e:
        print(f"An exception occurred: {e}")
        traceback.print_exc()
    time.sleep(5)

