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

            teamLst.append((team['shortName'], team['id']))
            print(team['shortName'], team['id'])
    return teamLst

def buildStatList():
    boxCat = list(statsapi.boxscore_data(statsapi.last_game(140))['homeBatters'][0].values())
    newBoxCat = ["team name", "team id"]
    for item in boxCat:
        if type(item) == str:
            if item.isupper():
                newBoxCat.append(item)
    pitchCat = list(statsapi.boxscore_data(statsapi.last_game(140))['homePitchers'][0].values())
    newPitchCat = []
    for item in pitchCat:
        if type(item) == str:
            if item.isupper():
                newStr = f'p{item}'
                newPitchCat.append(item)
    return newBoxCat, newPitchCat

def buildHomeAndAwayDatabases():
    pass

def processBoxScore():
    pass



def main():
    buildStatList()

main()