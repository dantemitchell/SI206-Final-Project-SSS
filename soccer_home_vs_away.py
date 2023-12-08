import sqlite3
from bs4 import BeautifulSoup
import requests


url1 = "https://www.worldfootball.net/schedule/eng-premier-league-2022-2023-spieltag/38/"

def get_22_23_away_records(url1):
    # Get name of each player and the number of home goals and away goals, seperately.
    # FIRST PAGE
    away_url = f"{url1}auswaerts/"
    r1 = requests.get(away_url)
    soup = BeautifulSoup(r1.content, 'html.parser')

    team_names = []
    # ateams1 = soup.find_all('td', bgcolor='#AFD179')
    for line in soup.find_all('td', bgcolor='#AFD179'):
        ateam1 = line.find('a')
        if ateam1 != None:
            team_names.append(ateam1.text)
    # ateams2 = soup.find_all('td', bgcolor='#D6EAB6')
    for line2 in soup.find_all('td', bgcolor='#D6EAB6'):
        ateam2 = line2.find('a')
        if ateam2 != None:
            team_names.append(ateam2.text)
    # ateams3 = soup.find_all('td', bgcolor='#E8F5D3')
    for line3 in soup.find_all('td', bgcolor='#E8F5D3'):
        ateam3 = line3.find('a')
        if ateam3 != None:
            team_names.append(ateam3.text)
    # ateams4 = soup.find_all('td', bgcolor='#FFFFFF')
    for line4 in soup.find_all('td', bgcolor='#FFFFFF'):
        ateam4 = line4.find('a')
        if ateam4 != None:
            team_names.append(ateam4.text)
    # ateams5 = soup.find_all('td', bgcolor='#A5CCE9')
    for line5 in soup.find_all('td', bgcolor='#A5CCE9'):
        ateam5 = line5.find('a')
        if ateam5 != None:
            team_names.append(ateam5.text)
    
    

    return team_names

    # home_url = f"{url1}heim/"
    # r2 = requests.get(home_url)
    # soup1 = BeautifulSoup(r2.content, 'html.parser')
    
    # hteams1 = soup1.find_all('td', bgcolor='#AFD179')
    # hteams2 = soup1.find_all('td', bgcolor='#D6EAB6')
    # hteams3 = soup1.find_all('td', bgcolor='#E8F5D3')
    # hteams4 = soup1.find_all('td', bgcolor='#FFFFFF')
    # hteams5 = soup1.find_all('td', bgcolor='#A5CCE9')

    # hteams = (hteams1, hteams2, hteams3, hteams4, hteams5)

    




print(get_22_23_records(url1))
    # for listing in soup.find_all('div', class_="g1qv1ctd cb4nyux dir dir-ltr"):
    #     title = listing.find('div', class_="t1jojoys dir dir-ltr").get_text(strip=True)
    #     url = listing.find('div',class_="t1jojoys dir dir-ltr")['id']
    #     listing_id = url.split('_')[-1]