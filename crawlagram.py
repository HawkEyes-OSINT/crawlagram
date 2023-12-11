from telethon.sync import TelegramClient
import telegram
import settings
from colorama import Fore
import asyncio
import pyfiglet

"""
Main execution file
"""


def ui():
    """
    User Interface
    """
    # display welcome message
    ascii_title = pyfiglet.figlet_format("CrawlaGram")
    print(Fore.GREEN + ascii_title)

    # introduction
    intro_text = """ CrawlaGram finds Telegram groups from a list of locations,
 or receives an input of a list of group IDs. 
 It then identifies relevant groups based on a list of keywords and regexs."""
    print(Fore.YELLOW + intro_text)

    # get instructions
    print(Fore.WHITE + "Please choose an option:")
    print(Fore.WHITE + "1. Find groups from a list of locations")
    print(Fore.WHITE + "2. Filter groups from list")
    print(Fore.WHITE + "3. Change configuration")
    print(Fore.WHITE + "4. Exit")

    return input(Fore.WHITE + "Enter your choice: ")

ui()