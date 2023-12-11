from config import getconfig
import csv
import os
import re
from telethon import functions, types, sync
import asyncio

"""
Find groups in 10km radious of given coordinates
"""

def retreive_cordinates():
    """
    verify cordinates file exists
    and contains at least one cordinate

    create list of cordinates to check
    """
    cordinates = []
    format = re.compile(r'^(-\d{1,3}|\d{1,3})\.[0-9]+$')

    # verify file exists
    if os.path.isfile("inputs/cordinates.csv"):
        with open("inputs/cordinates.csv", "r") as f:
            lines = f.readlines()
            for indx, line in enumerate(lines[1:]):
                lat = line.split(',')[0]
                lon = line.split(',')[1]
            
                # invalid data
                if not format.match(lat) or not format.match(lon):
                    print(f'[-] Invalid data in line {indx+1}')
                
                # append cordinates to list
                else:
                    cordinates.append({'lat': float(lat), 'lon': float(lon)})
    else:
        print('[-] Missing inputs/cordinates.csv')

    return cordinates 


async def find_groups(client):
    """
    find groups around provided cordinates
    """
    found_groups = []
    cordinates = retreive_cordinates()

    # get groups from cordinates
    for cordinate in cordinates:
        cord = f'{cordinate["lat"]},{cordinate["lon"]}'
        print(f'[+] Checking {cord} for groups/channels')
        result = await client(functions.contacts.GetLocatedRequest(
            geo_point = types.InputGeoPoint(lat=cordinate['lat'], long=cordinate['lon']
        ), self_expires=42))
            
        if result:
            # get relevant data from results
            channels = [chat for chat in result.chats]
            print(f'[+] Found {len(channels)} channels/groups at location {cord}')
            
            # add groups/channels to list
            for channel in channels:
                # Check if the channel ID already exists in the list
                if not any(group['ID'] == channel.id for group in found_groups):
                    found_groups.append({
                        'ID': channel.id, 
                        'Name': channel.title, 
                        'Type': 'Channel', 
                        'Location': cord
                    })

        else:
            print('[-] No groups/channels found')

    return found_groups
    