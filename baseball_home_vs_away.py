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
            teamLst.append(team['shortName'])
            print(team['shortName'])
    print(len(teamLst))
    #teamDict = teamjson
    #mlbDict = [team for team in teamDict if (team['teams'][0]['sport']['name']) == "Major League Baseball"]
    #team = statsapi.lookup_team('det')
    #print(team[0]['id'])

def buildRosterDatabases():
    pass

def processBoxScore():
    pass



def main():
    buildTeamList()

main()