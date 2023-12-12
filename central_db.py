import sqlite3

def copy_table(source_conn, source_table_name, dest_conn):
    source_cursor = source_conn.cursor()
    dest_cursor = dest_conn.cursor()

    source_cursor.execute(f"SELECT sql FROM sqlite_master WHERE type='table' AND name='{source_table_name}'")
    create_table_query = source_cursor.fetchone()[0]
    
    dest_cursor.execute(create_table_query)

    source_cursor.execute(f"SELECT * FROM {source_table_name}")
    rows = source_cursor.fetchall()
    
    for row in rows:
        placeholders = ', '.join('?' * len(row))
        dest_cursor.execute(f"INSERT INTO {source_table_name} VALUES ({placeholders})", row)

    dest_conn.commit()

conn_db1 = sqlite3.connect('NBAData2.db')
conn_db2 = sqlite3.connect('Baseball Data.db')
conn_db3 = sqlite3.connect('football_records_combined.db')

conn_main = sqlite3.connect('main_database.db')

copy_table(conn_db1, 'team_records', conn_main)
copy_table(conn_db2, 'CombinedData', conn_main)
copy_table(conn_db3, 'football_records', conn_main)

conn_db1.close()
conn_db2.close()
conn_db3.close()
conn_main.close()
