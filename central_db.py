import sqlite3


def create_or_connect_database(db_name):
    conn = sqlite3.connect(db_name)
    return conn

from baseball_home_vs_away import create_table_function_1
from NBAData import set_up_team_table
from NBAData import set_up_record_table
from soccer_home_vs_away import insert_data_into_combined_table

db_connection = create_or_connect_database('main_database.db')

set_up_record_table(db_connection)
set_up_team_table(db_connection)
set_up_record_table(db_connection)
insert_data_into_combined_table(db_connection)


db_connection.close()