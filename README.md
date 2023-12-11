# CrawlaGram - Installation and Usage Guide

## Overview

CrawlaGram is a Python program designed to find and filter Telegram groups based on various criteria, such as location, keywords, and regular expressions. Follow this guide to download, install, and use CrawlaGram.

## Installation

1. **Clone the Repository:**
   - Open a terminal or command prompt.
   - Run the following command to clone the CrawlaGram repository from GitHub:
     ```bash
     git clone https://github.com/HawkEyes-OSINT/crawlagram.git
     ```

2. **Navigate to the CrawlaGram Directory:**
   - Change your working directory to the CrawlaGram folder:
     ```bash
     cd crawlagram
     ```

3. **Install Dependencies:**
   - Install the required Python dependencies using pip:
     ```bash
     pip install -r requirements.txt
     ```

## Configuration

1. **Telegram API Bot Configuration:**
   - Open the `inputs/config.csv` file and enter your Telegram API bot configurations.
   - Ensure you provide values for `api_id`, `api_hash`, and `phone`.

2. **Coordinates Configuration:**
   - If using the geolocation feature, provide coordinates in the `inputs/cordinates.csv` file.

3. **Groups Configuration:**
   - Edit the `inputs/groups.csv` file:
     - If you wish to provide a list of groups, enter the group usernames in the ID column.

4. **Filter Configuration:**
   - Edit the `inputs/filters.csv` file:
     - Add keywords and/or regex to filter groups. Each row represents a filter.

## Usage

1. **Run CrawlaGram:**
   - Execute the main script, `crawlagram.py`, to start CrawlaGram:
     ```bash
     python crawlagram.py
     ```

2. **User Interface:**
   - Follow the on-screen instructions to choose an option:
     - Option 1: Find and filter groups based on coordinates and filters.
     - Option 2: Filter groups based on usernames from `groups.csv`.

3. **Follow Instructions:**
   - For Option 1:
     - CrawlaGram will find groups and channels in the area of the coordinates from `cordinates.csv` and filter them based on keywords and regex from `filters.csv`.
   - For Option 2:
     - CrawlaGram will filter groups based on keywords and regex from `filters.csv` using the provided group usernames in `groups.csv`.
   - Follow any additional prompts for input or authentication.

4. **View Results:**
   - Check the `outputs` directory for the results, including filtered groups and chat histories.

## Important Notes:

- Ensure you have the necessary permissions and configurations in place for your Telegram API bot.
- The program may prompt for additional information during execution.
- Use CrawlaGram responsibly and comply with Telegram's terms of service.

**Disclaimer:** CrawlaGram is intended for educational and research purposes. The developers are not responsible for any misuse or consequences resulting from the use of this program.
