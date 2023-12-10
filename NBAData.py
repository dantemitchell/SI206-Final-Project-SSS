#NBA Data File

import requests
import http.client
import json
import sqlite3
import unittest
import os

def get_api_info(url, api_key, teamNum):
    headers = {
        'X-RapidAPI-Key': api_key,
        'X-RapidAPI-Host': 'api-nba-v1.p.rapidapi.com'
    }
    querystring = {"season":"2022","team":teamNum}
    try:
        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code == 200:
            return response.json()  # Returns the JSON content of the response
        else:
            return f"Error: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"

def count_team_wins_losses(data, team_id):
    home_wins = 0
    home_losses = 0
    away_wins = 0
    away_losses = 0
    
    for game in data['response']:
        visitor_score = game['scores']['visitors']['points']
        home_score = game['scores']['home']['points']

        if game['teams']['visitors']['id'] == team_id:
            if visitor_score > home_score:
                away_wins += 1
            if visitor_score < home_score:
                away_losses += 1
        else:
            if home_score > visitor_score:
                home_wins += 1
            if home_score < visitor_score:
                home_losses += 1
    finalDict = {'Home Wins':home_wins, 'Home Losses':home_losses, 'Away Wins':away_wins, 'Away Losses':away_losses}
    return finalDict

def set_up_database(db):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path + "/" + db)
    cur = conn.cursor()
    return cur, conn

def set_up_team_table(cur, conn):
    url = "https://api-nba-v1.p.rapidapi.com/teams"
    headers = {
	    "X-RapidAPI-Key": "efc6e04bccmsh098566e98580557p1c5882jsn2d733f042025",
	    "X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    teamNameData = response.json()
    teamList = []
    for team in teamNameData['response']:
        if team['name'] in ["Atlanta Hawks", "Boston Celtics", "Brooklyn Nets", "Charlotte Hornets", 
                            "Chicago Bulls", "Cleveland Cavaliers", "Dallas Mavericks", "Denver Nuggets",
                            "Detroit Pistons", "Golden State Warriors", "Houston Rockets", "Indiana Pacers",
                            "LA Clippers", "Los Angeles Lakers", "Memphis Grizzlies",
                            "Miami Heat", "Milwaukee Bucks", "Minnesota Timberwolves", "New Orleans Pelicans",
                            "New York Knicks", "Oklahoma City Thunder", "Orlando Magic", "Philadelphia 76ers",
                            "Phoenix Suns", "Portland Trail Blazers", "Sacramento Kings", "San Antonio Spurs",
                            "Toronto Raptors", "Utah Jazz", "Washington Wizards"]:
            teamList.append((team['id'], team['name']))
    print(teamList)
    print(len(teamList))

    cur.execute('''CREATE TABLE IF NOT EXISTS teams (
                        team_id INT PRIMARY KEY,
                        team_name TEXT NOT NULL
                      )''')

    
    cur.executemany('INSERT OR IGNORE INTO teams (team_id, team_name) VALUES (?, ?)', teamList)

    conn.commit()
    conn.close()


def main():
    api_key = "efc6e04bccmsh098566e98580557p1c5882jsn2d733f042025"
    url = "https://api-nba-v1.p.rapidapi.com/games/" 
    data = get_api_info(url, api_key, '1')
    #print(data)
    record = count_team_wins_losses(data, 1)
    print(record)
    cur, conn = set_up_database("NBAData.db")
    set_up_team_table(cur, conn)
    
    

if __name__ == "__main__":
    main()