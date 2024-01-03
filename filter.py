import csv
import os

"""
Get groups as imput or from CSV
Filter out irrelevent groups based on inputed keywords from CSV
"""

LIMIT = 300

def get_groups():
    """
    retreive groups from CSV
    """
    groups = []
    with open('inputs/groups.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            groups.append({'Username': row['ID'],
                           'Title': row['Name'],
                           'Hash': '',
                           'Location': ''})
    return groups


def get_filters():
    """
    retreive filters from CSV
    """
    keywords, regex = [], []
    with open('inputs/filters.csv', 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            keywords.append(row['Keywords'])
            regex.append(row['Regex'])

    return keywords, regex

async def filter_groups(client, groups):
    """
    Get groups chat history.
    Filter out irrelevant groups based on keywords and regex
    """
    keywords, regex = get_filters()
    filtered_groups = []

    for group in groups:
        hits = 0
        matches = []
        keep = False

        # get chat history
        try:
            print(f'[+] Getting chat history for {group["Title"]}')
            if group['Username']:
                history = await client.get_messages(group['Username'], limit=LIMIT)
            else:
                history = []
            print(f'[+] Filtering {group["Title"]}')
            if history:
                for message in history:

                    # check keywords list
                    if message.text:
                        for keyword in keywords:
                            if keyword != '' and keyword in message.raw_text:
                                keep = True
                                hits += 1
                                matches.append(keyword)

                        # for pattern in regex:
                        #     if regex != '' and re.search(pattern, message.text):
                        #         keep = True
                        #         hits += 1
                        #         matches.append(pattern)
                        #         print('pattern: ' + pattern)

            # add kept group
            if keep:
                print(f'[+] Keeping {group["Title"]}')
                
                # append group to list
                filtered_groups.append({'Username': group['Username'],
                                    'Title': group['Title'],
                                    'Hash': group['Hash'],
                                    'Location': group['Location'],
                                    'Hits': hits,
                                    'Matches': matches})
            
                # export chat history to csv
                group_folder = os.makedirs(f'outputs/chats', exist_ok=True)
                with open(f'outputs/chats/{group["Title"]}.csv', 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(['Sender ID', 'Sender Title', 'Date', 'Text'])
                    for message in history:

                        # get name of sender
                        if message.sender:
                            if message.sender.username:
                                name = message.sender.username
                            else:
                                name = message.sender.first_name
                                if message.sender.last_name:
                                    name += ' ' + message.sender.last_name
                        else:
                            name = 'N/A'

                        # write to csv
                        writer.writerow([message.sender_id, name, message.date, message.text])
            else:
                print(f'[-] Removing {group["Title"]}')
        
        except Exception as e:
            print(f'[-] Error getting chat history for {group["Title"]}: {e}')
            continue
            
    # export filtered groups to csv
    with open('outputs/filtered_groups.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['Username', 'Title', 'Hash', 'Location', 'Hits', 'Matches'])
        writer.writeheader()
        for group in filtered_groups:
            writer.writerow(group)

    print(f'[+] Output of {len(filtered_groups)} from {len(groups)} initial groups')
    return True
    