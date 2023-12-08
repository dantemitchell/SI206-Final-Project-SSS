import sqlite3
import bs4 as BeautifulSoup
import requests


# Get name of each player and the number of home goals and away goals, seperately.
# FIRST PAGE
url1 = "https://www.worldfootball.net/schedule/eng-premier-league-2022-2023-spieltag/38/"
r1 = requests.get(url1)
soup = BeautifulSoup(r.content, 'html.parser')
players = soup.find_all()