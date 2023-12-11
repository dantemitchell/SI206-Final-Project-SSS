import json
import sqlite3
import matplotlib.pyplot as plt

def get_wins_losses_json():
    conn = sqlite3.connect('football_records_combined.db')
    c = conn.cursor()

    c.execute('SELECT team_name, home_wins, home_losses, away_wins, away_losses, home_goal_diff, away_goal_diff  FROM football_records')

    data = c.fetchall()

    conn.close()

    json_data = json.dumps(data)

    return json_data
json_data = get_wins_losses_json()

def calculate_averages(json_string):
    
    data = json.loads(json_string)
    num_entries = len(data)
    home_wins_total = sum(entry[1] for entry in data)
    home_losses_total = sum(entry[2] for entry in data)
    away_wins_total = sum(entry[3] for entry in data)
    away_losses_total = sum(entry[4] for entry in data)
    home_goal_diff_total = sum(entry[5] for entry in data)
    away_goal_diff_total = sum(entry[6] for entry in data)

    avg_home_wins = home_wins_total / num_entries
    avg_home_losses = home_losses_total / num_entries
    avg_away_wins = away_wins_total / num_entries
    avg_away_losses = away_losses_total / num_entries
    avg_home_goal_diff = home_goal_diff_total / num_entries
    avg_away_goal_diff = away_goal_diff_total / num_entries

    return {
        'Average Home Wins': avg_home_wins,
        'Average Home Losses': avg_home_losses,
        'Average Away Wins': avg_away_wins,
        'Average Away Losses': avg_away_losses,
        'Average Home Goal Differential': avg_home_goal_diff,
        'Average Away Goal Differential': avg_away_goal_diff
    }
averages = calculate_averages(json_data)
categories = list(averages.keys())
values = list(averages.values())

plt.figure(figsize=(10, 6))

plt.bar(categories, values, color=['blue', 'orange', 'green', 'red', 'cyan', 'magenta'])
plt.xlabel('Categories')
plt.ylabel('Average Values')
plt.title('Average Home and Away Wins, Losses, and Goal Differential')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()


