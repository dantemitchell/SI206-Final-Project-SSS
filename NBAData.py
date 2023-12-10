#NBA Data File

import requests
import json
import sqlite3
import unittest
import os

def get_api_info(url, params=None):
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except:
        print("Exception!")
        return None