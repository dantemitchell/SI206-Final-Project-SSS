#NBA Data File

import requests
import http.client
import json
import sqlite3
import unittest
import os

def get_api_info_2022(url, api_key, teamNum):
    headers = {
        'X-RapidAPI-Key': api_key,
        'X-RapidAPI-Host': 'api-nba-v1.p.rapidapi.com'
    }
    querystring = {"season":"2022","team":teamNum}
    try:
        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"

def get_api_info_2021(url, api_key, teamNum):
    headers = {
        'X-RapidAPI-Key': api_key,
        'X-RapidAPI-Host': 'api-nba-v1.p.rapidapi.com'
    }
    querystring = {"season":"2021","team":teamNum}
    try:
        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"

def get_api_info_2020(url, api_key, teamNum):
    headers = {
        'X-RapidAPI-Key': api_key,
        'X-RapidAPI-Host': 'api-nba-v1.p.rapidapi.com'
    }
    querystring = {"season":"2020","team":teamNum}
    try:
        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"
    
def get_api_info_2019(url, api_key, teamNum):
    headers = {
        'X-RapidAPI-Key': api_key,
        'X-RapidAPI-Host': 'api-nba-v1.p.rapidapi.com'
    }
    querystring = {"season":"2019","team":teamNum}
    try:
        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"

def count_team_wins_losses_2022(data, team_id):
    home_wins = 0
    home_losses = 0
    away_wins = 0
    away_losses = 0
    home_points = 0
    away_points = 0
    
    try:
        for game in data['response']:
            visitor_score = game['scores']['visitors']['points']
            home_score = game['scores']['home']['points']

            if game['teams']['visitors']['id'] == team_id:
                away_points += visitor_score
                if visitor_score > home_score:
                    away_wins += 1
                if visitor_score < home_score:
                    away_losses += 1
            else:
                home_points += home_score
                if home_score > visitor_score:
                    home_wins += 1
                if home_score < visitor_score:
                    home_losses += 1
        finalDict = {'team_id':str(team_id)+' 22-23','Home Wins':home_wins, 'Home Losses':home_losses, 'Away Wins':away_wins, 'Away Losses':away_losses, 'Home Points':home_points, 'Away Points':away_points}
    except:
        finalDict = {'team_id':str(team_id)+' 22-23','Home Wins':home_wins, 'Home Losses':home_losses, 'Away Wins':away_wins, 'Away Losses':away_losses, 'Home Points':home_points, 'Away Points':away_points}
    return finalDict

def count_team_wins_losses_2021(data, team_id):
    home_wins = 0
    home_losses = 0
    away_wins = 0
    away_losses = 0
    home_points = 0
    away_points = 0
    
    try:
        for game in data['response']:
            visitor_score = game['scores']['visitors']['points']
            home_score = game['scores']['home']['points']

            if game['teams']['visitors']['id'] == team_id:
                away_points += visitor_score
                if visitor_score > home_score:
                    away_wins += 1
                if visitor_score < home_score:
                    away_losses += 1
            else:
                home_points += home_score
                if home_score > visitor_score:
                    home_wins += 1
                if home_score < visitor_score:
                    home_losses += 1
        finalDict = {'team_id':str(team_id)+' 21-22','Home Wins':home_wins, 'Home Losses':home_losses, 'Away Wins':away_wins, 'Away Losses':away_losses, 'Home Points':home_points, 'Away Points':away_points}
    except:
        finalDict = {'team_id':str(team_id)+' 21-22','Home Wins':home_wins, 'Home Losses':home_losses, 'Away Wins':away_wins, 'Away Losses':away_losses, 'Home Points':home_points, 'Away Points':away_points}
    return finalDict

def count_team_wins_losses_2020(data, team_id):
    home_wins = 0
    home_losses = 0
    away_wins = 0
    away_losses = 0
    home_points = 0
    away_points = 0
    
    try:
        for game in data['response']:
            visitor_score = game['scores']['visitors']['points']
            home_score = game['scores']['home']['points']

            if game['teams']['visitors']['id'] == team_id:
                away_points += visitor_score
                if visitor_score > home_score:
                    away_wins += 1
                if visitor_score < home_score:
                    away_losses += 1
            else:
                home_points += home_score
                if home_score > visitor_score:
                    home_wins += 1
                if home_score < visitor_score:
                    home_losses += 1
        finalDict = {'team_id':str(team_id)+' 20-21','Home Wins':home_wins, 'Home Losses':home_losses, 'Away Wins':away_wins, 'Away Losses':away_losses, 'Home Points':home_points, 'Away Points':away_points}
    except:
        finalDict = {'team_id':str(team_id)+' 20-21','Home Wins':home_wins, 'Home Losses':home_losses, 'Away Wins':away_wins, 'Away Losses':away_losses, 'Home Points':home_points, 'Away Points':away_points}
    return finalDict

def count_team_wins_losses_2019(data, team_id):
    home_wins = 0
    home_losses = 0
    away_wins = 0
    away_losses = 0
    home_points = 0
    away_points = 0
    
    try:
        for game in data['response']:
            visitor_score = game['scores']['visitors']['points']
            home_score = game['scores']['home']['points']

            if game['teams']['visitors']['id'] == team_id:
                away_points += visitor_score
                if visitor_score > home_score:
                    away_wins += 1
                if visitor_score < home_score:
                    away_losses += 1
            else:
                home_points += home_score
                if home_score > visitor_score:
                    home_wins += 1
                if home_score < visitor_score:
                    home_losses += 1
        finalDict = {'team_id':str(team_id)+' 19-20','Home Wins':home_wins, 'Home Losses':home_losses, 'Away Wins':away_wins, 'Away Losses':away_losses, 'Home Points':home_points, 'Away Points':away_points}
    except:
        finalDict = {'team_id':str(team_id)+' 19-20','Home Wins':home_wins, 'Home Losses':home_losses, 'Away Wins':away_wins, 'Away Losses':away_losses, 'Home Points':home_points, 'Away Points':away_points}
    return finalDict

def create_record_list_2022():
    api_key = "efc6e04bccmsh098566e98580557p1c5882jsn2d733f042025"
    url = "https://api-nba-v1.p.rapidapi.com/games/" 
    teamNums = [1,2,4,5,6,7,8,9,10,11,14,15,16,17,19,20,21,22,23,24,25,26,27,28,29]
    final = []

    for num in teamNums:
        data = get_api_info_2022(url, api_key, str(num))
        record = count_team_wins_losses_2022(data, num)
        final.append(record)

    return final

def create_record_list_2021():
    api_key = "efc6e04bccmsh098566e98580557p1c5882jsn2d733f042025"
    url = "https://api-nba-v1.p.rapidapi.com/games/" 
    teamNums = [1,2,4,5,6,7,8,9,10,11,14,15,16,17,19,20,21,22,23,24,25,26,27,28,29]
    final = []

    for num in teamNums:
        data = get_api_info_2021(url, api_key, str(num))
        record = count_team_wins_losses_2021(data, num)
        final.append(record)

    return final

def create_record_list_2020():
    api_key = "efc6e04bccmsh098566e98580557p1c5882jsn2d733f042025"
    url = "https://api-nba-v1.p.rapidapi.com/games/" 
    teamNums = [1,2,4,5,6,7,8,9,10,11,14,15,16,17,19,20,21,22,23,24,25,26,27,28,29]
    final = []

    for num in teamNums:
        data = get_api_info_2020(url, api_key, str(num))
        record = count_team_wins_losses_2020(data, num)
        final.append(record)
    
    return final

def create_record_list_2019():
    api_key = "efc6e04bccmsh098566e98580557p1c5882jsn2d733f042025"
    url = "https://api-nba-v1.p.rapidapi.com/games/" 
    teamNums = [1,2,4,5,6,7,8,9,10,11,14,15,16,17,19,20,21,22,23,24,25,26,27,28,29]
    final = []

    for num in teamNums:
        data = get_api_info_2019(url, api_key, str(num))
        record = count_team_wins_losses_2019(data, num)
        final.append(record)

    return final
        
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
                            "Phoenix Suns", "Portland Trail Blazers"]:
            teamList.append((team['id'], team['name']))
    #print(teamList)
    #print(len(teamList))

    cur.execute('''CREATE TABLE IF NOT EXISTS teams (
                        team_id INT PRIMARY KEY,
                        team_name TEXT NOT NULL
                      )''')

    
    cur.executemany('INSERT OR IGNORE INTO teams (team_id, team_name) VALUES (?, ?)', teamList)

    conn.commit()
    #conn.close()

def set_up_record_table(data, cur, conn):
    cur.execute('''CREATE TABLE IF NOT EXISTS team_records (
                    team_id TEXT PRIMARY KEY,
                    home_wins INT,
                    home_losses INT,
                    away_wins INT,
                    away_losses INT,
                    home_points INT,
                    away_points INT
                   )''')
    insert_stmt = 'INSERT OR IGNORE INTO team_records (team_id, home_wins, home_losses, away_wins, away_losses, home_points, away_points) VALUES (?, ?, ?, ?, ?, ?, ?)'
    
    for record in data:
        values = (record['team_id'], record['Home Wins'], record['Home Losses'], record['Away Wins'], record['Away Losses'], record['Home Points'], record['Away Points'])
        cur.execute(insert_stmt, values)
    conn.commit()

def calculate_averages_and_point_differential_and_write_to_file(db_path):
    conn = sqlite3.connect(db_path)

    # Calculate the averages and point differential
    query_averages = """
    SELECT AVG(home_wins) AS avg_home_wins,
           AVG(home_losses) AS avg_home_losses,
           AVG(away_wins) AS avg_away_wins,
           AVG(away_losses) AS avg_away_losses
    FROM team_records;
    """
    averages = conn.execute(query_averages).fetchone()

    query_point_diff = """
    SELECT AVG(home_points - away_points) AS avg_point_differential
    FROM team_records;
    """
    avg_point_differential = conn.execute(query_point_diff).fetchone()[0]

    # Writing the averages and point differential to a text file
    file_path = 'calculations.txt'
    with open(file_path, 'w') as file:
        file.write(f"Average Home Wins: {averages[0]}\n")
        file.write(f"Average Home Losses: {averages[1]}\n")
        file.write(f"Average Away Wins: {averages[2]}\n")
        file.write(f"Average Away Losses: {averages[3]}\n")
        file.write(f"Average Point Differential: {avg_point_differential}\n")

    return file_path

def main():
    record_list = create_record_list_2019()
    cur, conn = set_up_database("NBAData2.db")
    set_up_team_table(cur, conn)
    set_up_record_table(record_list, cur, conn)

    updated_output_file_path = calculate_averages_and_point_differential_and_write_to_file('NBAData2.db')
    updated_output_file_path



if __name__ == "__main__":
    main()