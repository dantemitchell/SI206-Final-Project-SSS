import sqlite3
from bs4 import BeautifulSoup
import requests
import os


# url1 = "https://www.worldfootball.net/schedule/eng-premier-league-2022-2023-spieltag/38/"
# bgcolor_list = ['#AFD179', '#D6EAB6', '#E8F5D3', '#FFFFFF', '#A5CCE9']

def get_22_23_records(url1, bgcolors):
    # Get name of each player and the number of home goals and away goals, seperately.
    # FIRST PAGE
    season = "22-23"
    away_url = f"{url1}auswaerts/"
    r1 = requests.get(away_url)
    soup_away = BeautifulSoup(r1.content, 'html.parser')

    home_url = f"{url1}heim/"
    r2 = requests.get(home_url)
    soup_home = BeautifulSoup(r2.content, 'html.parser')

    away_team_names23 = []
    home_team_names23 = []
    home_wins_draws_losses23 = []
    away_wins_draws_losses23 = []
    
    for color in bgcolors:
        team_data = []
        current_team = ''
        team_count = 0        
        td_elements = soup_away.find_all('td', bgcolor=color)
        for td in td_elements:
            if td.find('a'):
                if team_count > 0 and team_data:
                    away_wins_draws_losses23.append((team_data[1], team_data[2], team_data[3]))  # Append tuple to list
                    team_data = []  # Reset team_data for the next team
                current_team = td.get_text(strip=True)
                away_team_names23.append(f"{current_team} {season}")
                team_count += 1
            else:
                if current_team and td.text.isdigit():
                    team_data.append(int(td.get_text(strip=True)))  # Append numeric value to team_data
        if team_data:
            away_wins_draws_losses23.append((team_data[1], team_data[2], team_data[3]))
    for color in bgcolors:
        team_data = []
        current_team = ''
        team_count = 0
        td_elements = soup_home.find_all('td', bgcolor=color)
        for td in td_elements:
            if td.find('a'):
                if team_count > 0 and team_data:
                    home_wins_draws_losses23.append((team_data[1], team_data[2], team_data[3]))  # Append tuple to list
                    team_data = []  # Reset team_data for the next team
                current_team = td.get_text(strip=True)
                home_team_names23.append(f"{current_team} {season}")
                team_count += 1
            else:
                if current_team and td.text.isdigit():
                    team_data.append(int(td.get_text(strip=True)))  # Append numeric value to team_data
        if team_data:
            home_wins_draws_losses23.append((team_data[1], team_data[2], team_data[3]))
    return away_team_names23, away_wins_draws_losses23, home_team_names23, home_wins_draws_losses23
# Call the function with the soup and bgcolor list
# away_team_names23, away_wins_and_losses23, home_team_names23, home_wins_draws_losses23 = get_22_23_records(url1, bgcolor_list)
# print(away_team_names23, away_wins_and_losses23)
# print(home_team_names23, home_wins_draws_losses23)


# url2 = "https://www.worldfootball.net/schedule/eng-premier-league-2021-2022-spieltag/38/"
def get_21_22_records(url2, bgcolors):
    # Get name of each player and the number of home goals and away goals, seperately.
    # FIRST PAGE
    season = "21-22"
    away_url = f"{url2}auswaerts/"
    r1 = requests.get(away_url)
    soup_away = BeautifulSoup(r1.content, 'html.parser')

    home_url = f"{url2}heim/"
    r2 = requests.get(home_url)
    soup_home = BeautifulSoup(r2.content, 'html.parser')

    away_team_names22 = []
    home_team_names22 = []
    home_wins_draws_losses22 = []
    away_wins_draws_losses22 = []
    
    for color in bgcolors:
        team_data = []
        current_team = ''
        team_count = 0 
        td_elements = soup_away.find_all('td', bgcolor=color)
        for td in td_elements:
            if td.find('a'):
                if team_count > 0 and team_data:
                    away_wins_draws_losses22.append((team_data[1], team_data[2], team_data[3]))  # Append tuple to list
                    team_data = []  # Reset team_data for the next team
                current_team = td.get_text(strip=True)
                away_team_names22.append(f"{current_team} {season}")
                team_count += 1
            else:
                if current_team and td.text.isdigit():
                    team_data.append(int(td.get_text(strip=True)))  # Append numeric value to team_data
        if team_data:
            away_wins_draws_losses22.append((team_data[1], team_data[2], team_data[3]))
    for color in bgcolors:
        team_data = []
        current_team = ''
        team_count = 0
        td_elements = soup_home.find_all('td', bgcolor=color)
        for td in td_elements:
            if td.find('a'):
                if team_count > 0 and team_data:
                    home_wins_draws_losses22.append((team_data[1], team_data[2], team_data[3]))  # Append tuple to list
                    team_data = []  # Reset team_data for the next team
                current_team = td.get_text(strip=True)
                home_team_names22.append(f"{current_team} {season}")
                team_count += 1
            else:
                if current_team and td.text.isdigit():
                    team_data.append(int(td.get_text(strip=True)))  # Append numeric value to team_data
        if team_data:
            home_wins_draws_losses22.append((team_data[1], team_data[2], team_data[3]))
    return away_team_names22, away_wins_draws_losses22, home_team_names22, home_wins_draws_losses22
# away_team_names22, away_wins_and_losses22, home_team_names22, home_wins_draws_losses22 = get_21_22_records(url2, bgcolor_list)
# print(away_team_names22, away_wins_and_losses22)
# print(home_team_names22, home_wins_draws_losses22)


# url3 = "https://www.worldfootball.net/schedule/eng-premier-league-2020-2021-spieltag/38/"
def get_20_21_records(url3, bgcolors):
    # Get name of each player and the number of home goals and away goals, seperately.
    # FIRST PAGE
    season = "20-21"
    away_url = f"{url3}auswaerts/"
    r1 = requests.get(away_url)
    soup_away = BeautifulSoup(r1.content, 'html.parser')

    home_url = f"{url3}heim/"
    r2 = requests.get(home_url)
    soup_home = BeautifulSoup(r2.content, 'html.parser')

    away_team_names21 = []
    home_team_names21 = []
    home_wins_draws_losses21 = []
    away_wins_draws_losses21 = []
    
    for color in bgcolors:
        team_data = []
        current_team = ''
        team_count = 0 
        td_elements = soup_away.find_all('td', bgcolor=color)
        for td in td_elements:
            if td.find('a'):
                if team_count > 0 and team_data:
                    away_wins_draws_losses21.append((team_data[1], team_data[2], team_data[3]))  # Append tuple to list
                    team_data = []  # Reset team_data for the next team
                current_team = td.get_text(strip=True)
                away_team_names21.append(f"{current_team} {season}")
                team_count += 1
            else:
                if current_team and td.text.isdigit():
                    team_data.append(int(td.get_text(strip=True)))  # Append numeric value to team_data
        if team_data:
            away_wins_draws_losses21.append((team_data[1], team_data[2], team_data[3]))
    for color in bgcolors:
        team_data = []
        current_team = ''
        team_count = 0
        td_elements = soup_home.find_all('td', bgcolor=color)
        for td in td_elements:
            if td.find('a'):
                if team_count > 0 and team_data:
                    home_wins_draws_losses21.append((team_data[1], team_data[2], team_data[3]))  # Append tuple to list
                    team_data = []  # Reset team_data for the next team
                current_team = td.get_text(strip=True)
                home_team_names21.append(f"{current_team} {season}")
                team_count += 1
            else:
                if current_team and td.text.isdigit():
                    team_data.append(int(td.get_text(strip=True)))  # Append numeric value to team_data
        if team_data:
            home_wins_draws_losses21.append((team_data[1], team_data[2], team_data[3]))
    return away_team_names21, away_wins_draws_losses21, home_team_names21, home_wins_draws_losses21
# away_team_names21, away_wins_and_losses21, home_team_names21, home_wins_draws_losses21 = get_20_21_records(url3, bgcolor_list)
# print(away_team_names21, away_wins_and_losses21)
# print(home_team_names21, home_wins_draws_losses21)


# url4 = "https://www.worldfootball.net/schedule/eng-premier-league-2019-2020-spieltag/38/"
def get_19_20_records(url4, bgcolors):
    # Get name of each player and the number of home goals and away goals, seperately.
    # FIRST PAGE
    season = "19-20"
    away_url = f"{url4}auswaerts/"
    r1 = requests.get(away_url)
    soup_away = BeautifulSoup(r1.content, 'html.parser')

    home_url = f"{url4}heim/"
    r2 = requests.get(home_url)
    soup_home = BeautifulSoup(r2.content, 'html.parser')

    away_team_names20 = []
    home_team_names20 = []
    home_wins_draws_losses20 = []
    away_wins_draws_losses20 = []
    
    for color in bgcolors:
        team_data = []
        current_team = ''
        team_count = 0 
        td_elements = soup_away.find_all('td', bgcolor=color)
        for td in td_elements:
            if td.find('a'):
                if team_count > 0 and team_data:
                    away_wins_draws_losses20.append((team_data[1], team_data[2], team_data[3]))  # Append tuple to list
                    team_data = []  # Reset team_data for the next team
                current_team = td.get_text(strip=True)
                away_team_names20.append(f"{current_team} {season}")
                team_count += 1
            else:
                if current_team and td.text.isdigit():
                    team_data.append(int(td.get_text(strip=True)))  # Append numeric value to team_data
        if team_data:
            away_wins_draws_losses20.append((team_data[1], team_data[2], team_data[3]))
    for color in bgcolors:
        team_data = []
        current_team = ''
        team_count = 0
        td_elements = soup_home.find_all('td', bgcolor=color)
        for td in td_elements:
            if td.find('a'):
                if team_count > 0 and team_data:
                    home_wins_draws_losses20.append((team_data[1], team_data[2], team_data[3]))  # Append tuple to list
                    team_data = []  # Reset team_data for the next team
                current_team = td.get_text(strip=True)
                home_team_names20.append(f"{current_team} {season}")
                team_count += 1
            else:
                if current_team and td.text.isdigit():
                    team_data.append(int(td.get_text(strip=True)))  # Append numeric value to team_data
        if team_data:
            home_wins_draws_losses20.append((team_data[1], team_data[2], team_data[3]))
    return away_team_names20, away_wins_draws_losses20, home_team_names20, home_wins_draws_losses20
# away_team_names20, away_wins_and_losses20, home_team_names20, home_wins_draws_losses20 = get_19_20_records(url4, bgcolor_list)
# print(away_team_names20, away_wins_and_losses20)
# print(home_team_names20, home_wins_draws_losses20)



# url5 = "https://www.worldfootball.net/schedule/eng-premier-league-2018-2019-spieltag/38/"
def get_18_19_records(url5, bgcolors):
    # Get name of each player and the number of home goals and away goals, seperately.
    # FIRST PAGE
    season = "18-19"
    away_url = f"{url5}auswaerts/"
    r1 = requests.get(away_url)
    soup_away = BeautifulSoup(r1.content, 'html.parser')

    home_url = f"{url5}heim/"
    r2 = requests.get(home_url)
    soup_home = BeautifulSoup(r2.content, 'html.parser')

    away_team_names19 = []
    home_team_names19 = []
    home_wins_draws_losses19 = []
    away_wins_draws_losses19 = []
    
    for color in bgcolors:
        team_data = []
        current_team = ''
        team_count = 0 
        td_elements = soup_away.find_all('td', bgcolor=color)
        for td in td_elements:
            if td.find('a'):
                if team_count > 0 and team_data:
                    away_wins_draws_losses19.append((team_data[1], team_data[2], team_data[3]))  # Append tuple to list
                    team_data = []  # Reset team_data for the next team
                current_team = td.get_text(strip=True)
                away_team_names19.append(f"{current_team} {season}")
                team_count += 1
            else:
                if current_team and td.text.isdigit():
                    team_data.append(int(td.get_text(strip=True)))  # Append numeric value to team_data
        if team_data:
            away_wins_draws_losses19.append((team_data[1], team_data[2], team_data[3]))
    for color in bgcolors:
        team_data = []
        current_team = ''
        team_count = 0
        td_elements = soup_home.find_all('td', bgcolor=color)
        for td in td_elements:
            if td.find('a'):
                if team_count > 0 and team_data:
                    home_wins_draws_losses19.append((team_data[1], team_data[2], team_data[3]))  # Append tuple to list
                    team_data = []  # Reset team_data for the next team
                current_team = td.get_text(strip=True)
                home_team_names19.append(f"{current_team} {season}")
                team_count += 1
            else:
                if current_team and td.text.isdigit():
                    team_data.append(int(td.get_text(strip=True)))  # Append numeric value to team_data
        if team_data:
            home_wins_draws_losses19.append((team_data[1], team_data[2], team_data[3]))
    return away_team_names19, away_wins_draws_losses19, home_team_names19, home_wins_draws_losses19
# away_team_names19, away_wins_and_losses19, home_team_names19, home_wins_draws_losses19 = get_18_19_records(url5, bgcolor_list)
# print(away_team_names19, away_wins_and_losses19)
# print(home_team_names19, home_wins_draws_losses19)

def create_db():
    conn = sqlite3.connect('football_records_combined.db')
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS football_records (
            id INTEGER PRIMARY KEY,
            team_name TEXT,
            home_wins INTEGER,
            home_draws INTEGER,
            home_losses INTEGER,
            away_wins INTEGER,
            away_draws INTEGER,
            away_losses INTEGER
        )
    ''')
    return conn, c

def insert_data_into_combined_table(c, home_teams, home_results, away_teams, away_results):
    for i in range(len(home_teams)):
        team_name = home_teams[i]
        home_wins, home_draws, home_losses = home_results[i]
        away_wins, away_draws, away_losses = away_results[i]
        c.execute('''
            INSERT INTO football_records (team_name, home_wins, home_draws, home_losses, away_wins, away_draws, away_losses)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (team_name, home_wins, home_draws, home_losses, away_wins, away_draws, away_losses))


def main():
    urls = [
        ("https://www.worldfootball.net/schedule/eng-premier-league-2022-2023-spieltag/38/", get_22_23_records),
        ("https://www.worldfootball.net/schedule/eng-premier-league-2021-2022-spieltag/38/", get_21_22_records),
        ("https://www.worldfootball.net/schedule/eng-premier-league-2020-2021-spieltag/38/", get_20_21_records),
        ("https://www.worldfootball.net/schedule/eng-premier-league-2019-2020-spieltag/38/", get_19_20_records),
        ("https://www.worldfootball.net/schedule/eng-premier-league-2018-2019-spieltag/38/", get_18_19_records)
    ]
    bgcolor_list = ['#AFD179', '#D6EAB6', '#E8F5D3', '#FFFFFF', '#A5CCE9']

# Load last processed URL and line count
    # if os.path.exists("last_processed.txt"):
    #     with open("last_processed.txt", "r") as file:
    #         last_processed_url, count = file.read().split(",")
    #         count = int(count)
    # else:
    #     last_processed_url = ""
    #     count = 0
    if os.path.exists("last_processed_index.txt"):
        with open("last_processed_index.txt", "r") as file:
            index = int(file.read())
    else:
        with open("last_processed_index.txt", "w") as file:
            index = 0
            file.write(str(index))
        
        # Find the index of the last processed URL to continue from
    url, get_records_func = urls[index]
   
    # Process the data for the current URL
    away_team_names, away_wins_and_losses, home_team_names, home_wins_draws_losses = get_records_func(url, bgcolor_list)

    conn, c = create_db()

    # Process 20 lines of data
    chunk_home_teams = home_team_names[:20]
    chunk_home_results = home_wins_draws_losses[:20]
    chunk_away_teams = away_team_names[:20]
    chunk_away_results = away_wins_and_losses[:20]

    # Insert the chunk of data into the database
    insert_data_into_combined_table(c, chunk_home_teams, chunk_home_results, chunk_away_teams, chunk_away_results)

    # Commit changes and close connection
    conn.commit()
    conn.close()

    # Increment index for the next run
    index = (index + 1) % len(urls)

    # Update the index file for the next run
    with open("last_processed_index.txt", "w") as file:
        file.write(str(index))


if __name__ == "__main__":
    main()
