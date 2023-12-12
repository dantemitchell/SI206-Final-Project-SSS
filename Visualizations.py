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
    
    file_path = 'calculations_soccer.txt'
    with open(file_path, 'w') as file:
        file.write(f"Average Home Wins: {averages[0]}\n")
        file.write(f"Average Home Losses: {averages[1]}\n")
        file.write(f"Average Away Wins: {averages[2]}\n")
        file.write(f"Average Away Losses: {averages[3]}\n")
        file.write(f"Average Home Goal Differential: {averages[4]}\n")
        file.write(f"Average Away Goal Differential: {averages[5]}\n")

    return file_path

calculate_averages_sql()
file_path = 'calculations_soccer.txt'

averages = {}
with open(file_path, 'r') as file:
    for line in file:
        parts = line.strip().split(':')
        if len(parts) == 2:
            key = parts[0].strip()
            value = float(parts[1].strip())
            averages[key] = value

labels = list(averages.keys())
values = list(averages.values())

plt.figure(figsize=(8, 6))
plt.bar(labels, values, color=['blue', 'orange', 'green', 'red', 'cyan', 'magenta'])
plt.xlabel('Categories')
plt.ylabel('Average Values')
plt.title('Average Home and Away Wins, Losses, and Goal Differential')
plt.xticks(rotation=45)
for index, value in enumerate(values):
    plt.text(value, index, str(round(value, 2)))

plt.tight_layout()
plt.show()



