import statsapi
import sqlite3
import matplotlib as plt
import seaborn as sb
import csv


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
    newBoxCat = [("TeamName", "TEXT"), ("TeamID", "INTEGER"), ("Season", "INTEGER"), (f"{locStr}Wins", "INTEGER"), (f"{locStr}Losses", "INTEGER"), (f"{locStr}RScored", "INTEGER"), (f"{locStr}RAllowed", "INTEGER")]
    return newBoxCat

def createDatabase(statList, dbName, tableName):
    conn = sqlite3.connect(dbName)
    cursor = conn.cursor()

    try:
        # Clear data from the table
        clear_data_query = f"DELETE FROM {tableName};"
        cursor.execute(clear_data_query)

        # Create the new table if it doesn't exist
        columns_definition = ', '.join(f'{column} {datatype}' for column, datatype in statList)
        print(columns_definition)
        create_table_query = f'''CREATE TABLE IF NOT EXISTS {tableName} ({columns_definition});'''
        print(create_table_query)
        cursor.execute(create_table_query)
        conn.commit()

    except sqlite3.Error as e:
        print(f"Error: {e}")

    finally:
        conn.close()

def processBoxScore(gamePk):
    game = statsapi.game_scoring_play_data(gamePk)
    homeTeam = game['home']['name']
    homeId = game['home']['id']
    awayTeam = game['away']['name']
    awayId = game['away']['id']
    try: 
        homeScore = game['plays'][-1]['result']['homeScore']
    except:
        return 0
    awayScore = game['plays'][-1]['result']['awayScore']
    homeTeamWin = homeScore > awayScore
    awayTeamWin = awayScore > homeScore
    return (homeTeam, homeId, homeTeamWin, homeScore, awayScore), (awayTeam, awayId, awayTeamWin, awayScore, homeScore)

def createDataDict(season):
    homeResultsDict = {}
    awayResultsDict = {}
    season_startdate, season_enddate = statsapi.get('season', {'seasonId': season, 'sportId': 1})['seasons'][0]['regularSeasonStartDate'], statsapi.get('season', {'seasonId': season, 'sportId': 1})['seasons'][0]['regularSeasonEndDate'], 
    gamedate = statsapi.get('schedule', {'sportId': 1, 'startDate': season_startdate, 'endDate': season_enddate})['dates']
    gamepk_lst = []
    for date in gamedate:
        for i in range(0, len(date['games']), 1):
            gamepk_lst.append(date['games'][i]['gamePk'])
    for gamepk in gamepk_lst: 
        try:
            homeData, awayData = processBoxScore(gamepk)
        except:
            continue
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
    print(len(homeResultsDict), len(awayResultsDict))
    return homeResultsDict, awayResultsDict


def populateTable(tableName, TeamName, resultsDict, dbName, location = "HOME"):
    conn = sqlite3.connect(dbName)
    cursor = conn.cursor()
    # Insert data into the table
    insert_data_query = f'''
    INSERT INTO {tableName} (TeamName, TeamId, Season, {location}Wins, {location}Losses, {location}RScored, {location}RAllowed)
    VALUES (?, ?, ?, ?, ?, ?, ?);
    '''

    # Assuming resultsDict contains only one team's data
    team_data = resultsDict.get(TeamName, None)
    if team_data:
        team_id = team_data.get("TeamID", None) # Assuming TeamID is passed as an argument
        season = team_data.get("Season", None)
        wins = team_data.get(f"{location}Wins", None)
        losses = team_data.get(f"{location}Losses", None)
        rscored = team_data.get(f"{location}RScored", None)
        rallowed = team_data.get(f"{location}RAllowed", None)

        cursor.execute(insert_data_query, (TeamName, team_id, season, wins, losses, rscored, rallowed))

    conn.commit()
    conn.close()

def joinTables(dbName, homeTableName, awayTableName, outputTableName):
    conn = sqlite3.connect(dbName)
    cursor = conn.cursor()

    # Check if the output table already exists
    existing_table_query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{outputTableName}';"
    cursor.execute(existing_table_query)
    existing_table = cursor.fetchone()

    # If the output table exists, drop it
    if existing_table:
        drop_table_query = f"DROP TABLE {outputTableName};"
        cursor.execute(drop_table_query)

    # Define the SQL command to join tables and create the output table
    join_tables_query = f'''
    CREATE TABLE IF NOT EXISTS {outputTableName} AS
    SELECT
        h.TeamName AS TeamName,
        h.TeamID AS TeamID,
        h.Season AS Season,
        h.HOMEWins AS HOMEWins,
        h.HOMELosses AS HOMELosses,
        h.HOMERScored AS HOMERScored,
        h.HOMERAllowed AS HOMERAllowed,
        a.AWAYWins AS AWAYWins,
        a.AWAYLosses AS AWAYLosses,
        a.AWAYRScored AS AWAYRScored,
        a.AWAYRAllowed AS AWAYRAllowed
    FROM {homeTableName} h
    JOIN {awayTableName} a ON h.TeamID = a.TeamID AND h.Season = a.Season;
    '''

    cursor.execute(join_tables_query)
    conn.commit()
    conn.close()

def calculateAvgRDiff(dbName, combinedTableName):
    conn = sqlite3.connect(dbName)
    cursor = conn.cursor()

    # Check if the new columns already exist
    existing_column_query = f"PRAGMA table_info({combinedTableName});"
    cursor.execute(existing_column_query)
    columns_info = cursor.fetchall()

    # Check if HOMEAvgRDiff column already exists
    home_avg_rdiff_exists = any("HOMEAvgRDiff" in column_info for column_info in columns_info)

    # Check if AWAYAvgRDiff column already exists
    away_avg_rdiff_exists = any("AWAYAvgRDiff" in column_info for column_info in columns_info)

    # If the HOMEAvgRDiff column already exists, drop it
    if home_avg_rdiff_exists:
        drop_home_column_query = f"ALTER TABLE {combinedTableName} DROP COLUMN HOMEAvgRDiff;"
        cursor.execute(drop_home_column_query)

    # If the AWAYAvgRDiff column already exists, drop it
    if away_avg_rdiff_exists:
        drop_away_column_query = f"ALTER TABLE {combinedTableName} DROP COLUMN AWAYAvgRDiff;"
        cursor.execute(drop_away_column_query)

    # Add new columns to the table
    add_home_column_query = f"ALTER TABLE {combinedTableName} ADD COLUMN HOMEAvgRDiff REAL;"
    cursor.execute(add_home_column_query)

    add_away_column_query = f"ALTER TABLE {combinedTableName} ADD COLUMN AWAYAvgRDiff REAL;"
    cursor.execute(add_away_column_query)

    # Update the new columns with the calculated values
    update_home_column_query = f'''
    UPDATE {combinedTableName}
    SET HOMEAvgRDiff = (HOMERScored - HOMERAllowed) / (HOMEWins + HOMELosses);
    '''
    cursor.execute(update_home_column_query)

    update_away_column_query = f'''
    UPDATE {combinedTableName}
    SET AWAYAvgRDiff = (AWAYRScored - AWAYRAllowed) / (AWAYWins + AWAYLosses);
    '''
    cursor.execute(update_away_column_query)

    conn.commit()
    conn.close()

def calculateWinPctDiff(dbName, combinedTableName):
    conn = sqlite3.connect(dbName)
    cursor = conn.cursor()

    # Check if the WinPctDiff column already exists
    existing_column_query = f"PRAGMA table_info({combinedTableName});"
    cursor.execute(existing_column_query)
    columns_info = cursor.fetchall()

    win_pct_diff_exists = any("WinPctDiff" in column_info for column_info in columns_info)

    # If the WinPctDiff column already exists, drop it
    if win_pct_diff_exists:
        drop_column_query = f"ALTER TABLE {combinedTableName} DROP COLUMN WinPctDiff;"
        cursor.execute(drop_column_query)

    # Add the WinPctDiff column to the table
    add_column_query = f"ALTER TABLE {combinedTableName} ADD COLUMN WinPctDiff REAL;"
    cursor.execute(add_column_query)

    # Update the WinPctDiff column with the calculated values
    update_column_query = f'''
    UPDATE {combinedTableName}
    SET WinPctDiff = (HOMEWins * 1.0 / (HOMEWins + HOMELosses)) -
                    (AWAYWins * 1.0 / (AWAYWins + AWAYLosses));
    '''
    cursor.execute(update_column_query)

    conn.commit()
    conn.close()

def addSummaryRows(dbName, combinedTableName):
    conn = sqlite3.connect(dbName)
    cursor = conn.cursor()

    # Calculate aggregate stats for each team
    team_summary_query = f'''
    INSERT INTO {combinedTableName} (TeamName, TeamID, Season, HOMEWins, HOMELosses, HOMERScored, HOMERAllowed, HOMEAvgRDiff, AWAYWins, AWAYLosses, AWAYRScored, AWAYRAllowed, AWAYAvgRDiff, WinPctDiff)
    SELECT
        TeamName,
        TeamID,
        'All Seasons' AS Season,
        SUM(HOMEWins) AS HOMEWins,
        SUM(HOMELosses) AS HOMELosses,
        SUM(HOMERScored) AS HOMERScored,
        SUM(HOMERAllowed) AS HOMERAllowed,
        AVG(HOMEAvgRDiff) AS HOMEAvgRDiff,
        SUM(AWAYWins) AS AWAYWins,
        SUM(AWAYLosses) AS AWAYLosses,
        SUM(AWAYRScored) AS AWAYRScored,
        SUM(AWAYRAllowed) AS AWAYRAllowed,
        AVG(AWAYAvgRDiff) AS AWAYAvgRDiff,
        AVG(WinPctDiff) AS WinPctDiff
    FROM {combinedTableName}
    GROUP BY TeamName, TeamID;
    '''
    cursor.execute(team_summary_query)

    # Calculate aggregate stats for each season
    season_summary_query = f'''
    INSERT INTO {combinedTableName} (TeamName, TeamID, Season, HOMEWins, HOMELosses, HOMERScored, HOMERAllowed, HOMEAvgRDiff, AWAYWins, AWAYLosses, AWAYRScored, AWAYRAllowed, AWAYAvgRDiff, WinPctDiff)
    SELECT
        TeamName,
        TeamID,
        Season,
        SUM(HOMEWins) AS HOMEWins,
        SUM(HOMELosses) AS HOMELosses,
        SUM(HOMERScored) AS HOMERScored,
        SUM(HOMERAllowed) AS HOMERAllowed,
        AVG(HOMEAvgRDiff) AS HOMEAvgRDiff,
        SUM(AWAYWins) AS AWAYWins,
        SUM(AWAYLosses) AS AWAYLosses,
        SUM(AWAYRScored) AS AWAYRScored,
        SUM(AWAYRAllowed) AS AWAYRAllowed,
        AVG(AWAYAvgRDiff) AS AWAYAvgRDiff,
        AVG(WinPctDiff) AS WinPctDiff
    FROM {combinedTableName}
    GROUP BY TeamName, TeamID, Season;
    '''
    cursor.execute(season_summary_query)

    conn.commit()
    conn.close()

def exportToCSV(dbName, tableName, csvFileName):
    conn = sqlite3.connect(dbName)
    cursor = conn.cursor()

    # Specify the columns you want to export
    selected_columns = ['TeamName', 'TeamID', 'Season', 'HOMEAvgRDiff', 'AWAYAvgRDiff']

    # Construct the SELECT statement with the specified columns
    select_query = f"SELECT {', '.join(selected_columns)} FROM {tableName}"

    # Fetch data from the SQL table
    cursor.execute(select_query)
    rows = cursor.fetchall()

    # Write data to a CSV file
    with open(csvFileName, 'w', newline='') as csvFile:
        csvWriter = csv.writer(csvFile)
        
        # Write header (column names)
        csvWriter.writerow(selected_columns)

        # Write data rows
        csvWriter.writerows(rows)

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
        print(f"{season} DataDict Built")
        for team, teamID in teamLst:
            populateTable("HomeData", team, hDict, "Baseball Data.db", 'HOME')
            populateTable("AwayData", team, aDict, "Baseball Data.db", 'AWAY')
            print(f"{season} {team} rows populated")
    joinTables("Baseball Data.db", "HomeData", "AwayData", "CombinedData")
    calculateAvgRDiff("Baseball Data.db", "CombinedData")
    calculateWinPctDiff("Baseball Data.db", "CombinedData")
    addSummaryRows("Baseball Data.db", "CombinedData")
    exportToCSV("Baseball Data.db", "CombinedData", "calculated_columns.csv")
    
main()