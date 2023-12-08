import sqlite3
from bs4 import BeautifulSoup
import requests


url1 = "https://www.worldfootball.net/schedule/eng-premier-league-2022-2023-spieltag/38/"

def get_22_23_away_records(url1, bgcolors):
    # Get name of each player and the number of home goals and away goals, seperately.
    # FIRST PAGE
    away_url = f"{url1}auswaerts/"
    r1 = requests.get(away_url)
    soup = BeautifulSoup(r1.content, 'html.parser')

    team_names = []
    wins_draws_losses = []
    

    for color in bgcolors:
        team_data = []
        current_team = ''
        team_count = 0
        print(color)
        td_elements = soup.find_all('td', bgcolor=color)
        for td in td_elements:
            if td.find('a'):
                if team_count > 0 and team_data:
                    wins_draws_losses.append((team_data[1], team_data[2], team_data[3]))  # Append tuple to list
                    team_data = []  # Reset team_data for the next team
                current_team = td.get_text(strip=True)
                team_names.append(current_team)
                team_count += 1
            else:
                if current_team and td.text.isdigit():
                    team_data.append(int(td.get_text(strip=True)))  # Append numeric value to team_data

        if team_data:
            wins_draws_losses.append((team_data[1], team_data[2], team_data[3]))

    return team_names, wins_draws_losses

bgcolor_list = ['#AFD179', '#CCCCCC', '#FFA500', '#90EE90', '#FFC0CB']

# Call the function with the soup and bgcolor list
# print(get_22_23_away_records(url1, bgcolor_list))
team_names, wins_and_losses = get_22_23_away_records(url1, bgcolor_list)
print(team_names, wins_and_losses)

    # for td in soup.find_all('td', bgcolor='#AFD179'):
    #     if td.find('a'):
    #         # If 'a' tag found, it's a team name
    #         if team_data:
    #             # If there's existing data, append to records_list
    #             wins_draws_losses.append((team_data[1], team_data[2], team_data[3]))  # Append tuple to list
    #             team_data = []  # Reset team_data for the next team
    #         current_team = td.get_text(strip=True)
    #         team_names.append(current_team)
    #     else:
    #         # Extract 2nd and 4th numbers if it's a numeric value
    #         if current_team and td.text.isdigit():
    #             team_data.append(int(td.get_text(strip=True)))  # Append numeric value to team_data
    # # Append the last team's data if any
    # if team_data:
    #     wins_draws_losses.append((team_data[1], team_data[2], team_data[3])) 


    # # ateams2 = soup.find_all('td', bgcolor='#D6EAB6')
    # for line2 in soup.find_all('td', bgcolor='#D6EAB6'):
    #     ateam2 = line2.find('a')
    #     if ateam2 != None:
    #         team_names.append(ateam2.text)


    # # ateams3 = soup.find_all('td', bgcolor='#E8F5D3')
    # for line3 in soup.find_all('td', bgcolor='#E8F5D3'):
    #     ateam3 = line3.find('a')
    #     if ateam3 != None:
    #         team_names.append(ateam3.text)
    # # ateams4 = soup.find_all('td', bgcolor='#FFFFFF')
    # for line4 in soup.find_all('td', bgcolor='#FFFFFF'):
    #     ateam4 = line4.find('a')
    #     if ateam4 != None:
    #         team_names.append(ateam4.text)
    # # ateams5 = soup.find_all('td', bgcolor='#A5CCE9')
    # for line5 in soup.find_all('td', bgcolor='#A5CCE9'):
    #     ateam5 = line5.find('a')
    #     if ateam5 != None:
    #         team_names.append(ateam5.text)
    
    

    # return team_names, wins_draws_losses

    # home_url = f"{url1}heim/"
    # r2 = requests.get(home_url)
    # soup1 = BeautifulSoup(r2.content, 'html.parser')
    
    # hteams1 = soup1.find_all('td', bgcolor='#AFD179')
    # hteams2 = soup1.find_all('td', bgcolor='#D6EAB6')
    # hteams3 = soup1.find_all('td', bgcolor='#E8F5D3')
    # hteams4 = soup1.find_all('td', bgcolor='#FFFFFF')
    # hteams5 = soup1.find_all('td', bgcolor='#A5CCE9')

    # hteams = (hteams1, hteams2, hteams3, hteams4, hteams5)

    




# print(get_22_23_away_records(url1))
    # for listing in soup.find_all('div', class_="g1qv1ctd cb4nyux dir dir-ltr"):
    #     title = listing.find('div', class_="t1jojoys dir dir-ltr").get_text(strip=True)
    #     url = listing.find('div',class_="t1jojoys dir dir-ltr")['id']
    #     listing_id = url.split('_')[-1]