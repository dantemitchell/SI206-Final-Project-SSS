import re
import statsapi
import requests
import _sqlite3
import matplotlib as plt
import seaborn as sb
import json

def buildTeamList():
    teamjson = statsapi.get('teams', {'season':'2023'})['teams'] #{'leagueIds':'Major League Baseball'}
    teamLst = []
    for team in teamjson:
        if team['sport']['name'] == "Major League Baseball":

            teamLst.append((team['name'], team['id']))
    return teamLst

def buildStatList(home = True):
    #boxCat = list(statsapi.boxscore_data(statsapi.last_game(140))['homeBatters'][0].values())
    locStr = ""
    if home:
        locStr = "HOME"
    else:
        locStr = "AWAY"
    newBoxCat = [("TeamName", "TEXT PRIMARY KEY"), ("TeamID", "INTEGER"), ("Season", "INTEGER"), (f"{locStr}Wins", "INTEGER"), (f"{locStr}Losses", "INTEGER"), (f"{locStr}RScored", "INTEGER"), (f"{locStr}RAllowed", "INTEGER")]
    return newBoxCat

def createDatabase(statList, dbName, tableName):
    conn = _sqlite3.connect(dbName)
    cursor = conn.cursor()
    # Check if the table already exists
    existing_table_query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{tableName}';"
    cursor.execute(existing_table_query)
    existing_table = cursor.fetchone()

    # If the table exists, drop it
    if existing_table:
        drop_table_query = f"DROP TABLE {tableName};"
        cursor.execute(drop_table_query)
    
    columns_definition = ', '.join(f'{column} {datatype}' for column, datatype in statList)
    create_table_query = f'''
    CREATE TABLE IF NOT EXISTS {tableName} (
        {columns_definition}
    );
    '''
    cursor.execute(create_table_query)
    conn.commit()
    conn.close()

def processBoxScore(gamePk):
    game = statsapi.game_scoring_play_data(gamePk)
    homeTeam = game['home']['name']
    homeId = game['home']['id']
    awayTeam = game['away']['name']
    awayId = game['away']['id']
    homeScore = game['plays'][-1]['result']['homeScore']
    awayScore = game['plays'][-1]['result']['awayScore']
    homeTeamWin = homeScore > awayScore
    awayTeamWin = awayScore > homeScore
    return (homeTeam, homeId, homeTeamWin, homeScore, awayScore), (awayTeam, awayId, awayTeamWin, awayScore, homeScore)

def createDataDict(season):
    homeResultsDict = {}
    awayResultsDict = {}
    season_startdate, season_enddate = statsapi.get('season', {'seasonId': season, 'sportId': 1})['seasons'][0]['regularSeasonStartDate'], statsapi.get('season', {'seasonId': season, 'sportId': 1})['seasons'][0]['regularSeasonEndDate'], 
    firstgamepk = statsapi.get('schedule', {'sportId': 1, 'date': season_startdate})['dates'][0]['games'][0]['gamePk']
    lastgamepk = statsapi.get('schedule', {'sportId': 1, 'date': season_enddate})['dates'][0]['games'][-1]['gamePk']
    gamedate = statsapi.get('schedule', {'sportId': 1, 'startDate': season_startdate, 'endDate': season_enddate})['dates']
    gamepk_lst = []
    for date in gamedate:
        for i in range(0, len(date['games']), 1):
            gamepk_lst.append(date['games'][i]['gamePk'])
    for gamepk in gamepk_lst: 
        homeData, awayData = processBoxScore(gamepk)
        homeWin = 0
        homeLoss = 0
        awayWin = 0
        awayLoss = 0
        if homeData[2] == True:
            homeWin = 1
            awayLoss = 1
        else:
            homeLoss = 1
            awayWin = 1
        if homeData[0] not in homeResultsDict:
            innerDict = {'TeamID': homeData[1], "Season": int(season), 'HOMEWins' : homeWin, 'HOMELosses': homeLoss, "HOMERScored": homeData[3], 'HOMERAllowed': homeData[4]}
            homeResultsDict[homeData[0]] = innerDict
        else:
            homeResultsDict[homeData[0]]['HOMEWins'] += homeWin
            homeResultsDict[homeData[0]]['HOMELosses'] += homeLoss
            homeResultsDict[homeData[0]]['HOMERScored'] += homeData[3]
            homeResultsDict[homeData[0]]['HOMERAllowed'] += homeData[4]

        if awayData[0] not in awayResultsDict:
            innerDict = {'TeamID': awayData[1], "Season": int(season), 'AWAYWins' : awayWin, 'AWAYLosses': awayLoss, "AWAYRScored": awayData[3], 'AWAYRAllowed': awayData[4]}
            awayResultsDict[awayData[0]] = innerDict
        else:
            awayResultsDict[awayData[0]]['AWAYWins'] += awayWin
            awayResultsDict[awayData[0]]['AWAYLosses'] += awayLoss
            awayResultsDict[awayData[0]]['AWAYRScored'] += awayData[3]
            awayResultsDict[awayData[0]]['AWAYRAllowed'] += awayData[4]
    return homeResultsDict, awayResultsDict


def populateTable(tableName, TeamName, resultsDict, dbName, location = "HOME"):
    conn = _sqlite3.connect(dbName)
    cursor = conn.cursor()
    # Insert data into the table
    insert_data_query = f'''
    INSERT INTO {tableName} (TeamName, TeamId, Season, {location}Wins, {location}Losses, {location}RScored, {location}RAllowed)
    VALUES (?, ?, ?, ?, ?, ?, ?);
    '''

    for team_name, team_data in resultsDict.items():
        team_id = team_data.get("TeamID", None)
        season = team_data.get("Season", None)
        wins = team_data.get(f"{location}Wins", None)
        losses = team_data.get(f"{location}Losses", None)
        rscored = team_data.get(f"{location}RScored", None)
        rallowed = team_data.get(f"{location}RAllowed", None)

        cursor.execute(insert_data_query, (team_name, team_id, season, wins, losses, rscored, rallowed))

    conn.commit()
    conn.close()



def main():
    teamLst = buildTeamList()
    homeStatLst = buildStatList(True)
    awayStatLst = buildStatList(False)
    createDatabase(homeStatLst, "Baseball Data.db", "HomeData")
    createDatabase(awayStatLst, "Baseball Data.db", "AwayData")
    seasons = ['2019', '2021', '2022', '2023']
    for season in seasons:
        hDict, aDict = createDataDict(season)
        for team, teamID in teamLst:
            populateTable("HomeData", team, hDict, "Baseball Data.db", 'HOME')
            populateTable("AwayData", team, hDict, "Baseball Data.db", 'HOME')



main()