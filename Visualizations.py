import json
import sqlite3
import matplotlib.pyplot as plt

def calculate_averages_sql():
    conn = sqlite3.connect('football_records_combined.db')
    c = conn.cursor()

    c.execute('''
        SELECT 
            AVG(home_wins) AS avg_home_wins,
            AVG(home_losses) AS avg_home_losses,
            AVG(away_wins) AS avg_away_wins,
            AVG(away_losses) AS avg_away_losses,
            AVG(home_goal_diff) AS avg_home_goal_diff,
            AVG(away_goal_diff) AS avg_away_goal_diff
        FROM football_records
    ''')

    averages = c.fetchone()
    conn.close()

    return {
        'Average Home Wins': averages[0],
        'Average Home Losses': averages[1],
        'Average Away Wins': averages[2],
        'Average Away Losses': averages[3],
        'Average Home Goal Differential': averages[4],
        'Average Away Goal Differential': averages[5]
    }

averages_sql = calculate_averages_sql()
categories = list(averages_sql.keys())
values = list(averages_sql.values())

plt.figure(figsize=(10, 6))

plt.bar(categories, values, color=['blue', 'orange', 'green', 'red', 'cyan', 'magenta'])
plt.xlabel('Categories')
plt.ylabel('Average Values')
plt.title('Average Home and Away Wins, Losses, and Goal Differential')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()


