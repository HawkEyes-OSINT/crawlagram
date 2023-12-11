from telethon.sync import TelegramClient
from config import getconfig
from colorama import Fore
import asyncio
import pyfiglet
from telethon.sync import TelegramClient
from telethon.errors import SessionPasswordNeededError
from geoloc import find_groups
from filter import filter_groups, get_groups

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
    print(Fore.WHITE + "3. Exit")

    return input(Fore.WHITE + "Enter your choice: ")



async def main():
    exit = False

    # create client session
    print('[+] Creating Telegram client session')
    config = getconfig()
    client = TelegramClient('session', config['api_id'], config['api_hash'])
    await client.start(config['phone'])
    if not client.is_user_authorized():
        client.send_code_request(config['phone'])
        try:
            client.sign_in(config['phone'], input('Enter the code: '))
        except SessionPasswordNeededError: # 2FA auth
            client.sign_in(phone=config['phone'], password=input('Enter 2FA password: '))
        except Exception as e:
            print('[-] ' + e)
            exit(0)
    print('[+] Client session created')

    while not exit:
        input = ui()

        # change bot configuration
        if input == "1":
            try: # get groups from locations
                groups = await find_groups(client)
            except Exception as e:
                print(Fore.RED + "Error: " + str(e))
                continue

            if groups: # filter groups by keyword
                try:
                    await filter_groups(client, groups)
                    print(Fore.GREEN + "Completed search and filter of groups/channels")
                    print(Fore.GREEN + "List of groups can be found in output/groups.csv")
                    print(Fore.GREEN + "Chat history can be found in output/chat/<group-name>.csv")
                except:
                    print(Fore.RED + "Error: " + str(e))
                    continue

        if input == "2":
            try: # get groups from csv
                groups = get_groups()
            except Exception as e:
                print(Fore.RED + "Error: " + str(e))
                continue

            if groups: # filter groups by keyword
                try:
                    await filter_groups(client, groups)
                    print(Fore.GREEN + "List of groups can be found in output/groups.csv")
                    print(Fore.GREEN + "Chat history can be found in output/chat/<group-name>.csv")
                except Exception as e:
                    print(Fore.RED + "Error: " + str(e))
                    continue

        if input == "3":
            print(Fore.RED + "Exiting...")
            exit = True

if __name__ == "__main__":
    asyncio.run(main())
