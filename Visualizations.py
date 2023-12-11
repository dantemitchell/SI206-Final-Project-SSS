import json
import sqlite3
import matplotlib.pyplot as plt

def get_wins_losses_json():
    conn = sqlite3.connect('football_records_combined.db')
    c = conn.cursor()

    # Select home and away wins, home and away losses from the database
    c.execute('SELECT team_name, home_wins, home_losses, away_wins, away_losses FROM football_records')

    # Fetch all rows
    data = c.fetchall()

    conn.close()

    # Convert data to JSON string
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

    avg_home_wins = home_wins_total / num_entries
    avg_home_losses = home_losses_total / num_entries
    avg_away_wins = away_wins_total / num_entries
    avg_away_losses = away_losses_total / num_entries

    return {
        'Average Home Wins': avg_home_wins,
        'Average Home Losses': avg_home_losses,
        'Average Away Wins': avg_away_wins,
        'Average Away Losses': avg_away_losses
    }
averages = calculate_averages(json_data)
categories = list(averages.keys())
values = list(averages.values())

plt.figure(figsize=(10, 6))

# Creating bar plot
plt.bar(categories, values, color=['blue', 'orange', 'green', 'red'])
plt.xlabel('Categories')
plt.ylabel('Average Values')
plt.title('Average Home and Away Wins/Losses')
plt.xticks(rotation=45)
plt.tight_layout()

# Show plot
plt.show()


# def plot_home_away_stats(json_data):
#     data = json.loads(json_data)
#     teams = [f"{''.join(word[0] for word in team.split())} {team.split()[-1][-5:-3]}-{team.split()[-1][-2:]}" for team, *_ in data]
#     home_wins = [home for _, home, _, _, _ in data]
#     away_wins = [away for _, _, away, _, _ in data]
#     home_losses = [loss for _, _, _, loss, _ in data]
#     away_losses = [loss for _, _, _, _, loss in data]


#     # Plotting home wins vs home losses
#     plt.figure(figsize=(10, 6))
#     plt.scatter(home_wins, home_losses, color='blue')
#     plt.title('Home Wins vs Home Losses')
#     plt.xlabel('Home Wins')
#     plt.ylabel('Home Losses')

#     for i, team in enumerate(teams):
#         plt.annotate(team, (home_wins[i], home_losses[i]))

#     plt.grid(True)
#     plt.show()

#     # Plotting away wins vs away losses
#     plt.figure(figsize=(10, 6))
#     plt.scatter(away_wins, away_losses, color='red')
#     plt.title('Away Wins vs Away Losses')
#     plt.xlabel('Away Wins')
#     plt.ylabel('Away Losses')

#     for i, team in enumerate(teams):
#         plt.annotate(team, (away_wins[i], away_losses[i]))

#     plt.grid(True)
#     plt.show()


#     # teams = [team_data[0] for team_data in data]
#     # home_wins = [team_data[1] for team_data in data]
#     # away_wins = [team_data[3] for team_data in data]
#     # home_losses = [team_data[2] for team_data in data]
#     # away_losses = [team_data[4] for team_data in data]
#     # teams = [f"{''.join(word[0] for word in team.split())} {team.split()[-1][-5:-3]}-{team.split()[-1][-2:]}" for team, *_ in data]
#     teams = [
#     f"{''.join(word[0] for word in team.split()[:-1])} {team.split()[-1][-5:-3]}-{team.split()[-1][-2:]}"
#     for team, *_ in data
# ]
#     home_wins = [home for _, home, *_ in data]
#     away_wins = [away for _, _, away, *_ in data]
#     home_losses = [loss for _, _, _, loss, *_ in data]
#     away_losses = [loss for _, _, _, _, loss in data]

#     # Plotting Home Wins vs Away Wins
#     plt.figure(figsize=(12, 8))
#     plt.scatter(home_wins, away_wins, marker='o', color='blue')
#     plt.title('Home Wins vs Away Wins')
#     plt.xlabel('Home Wins')
#     plt.ylabel('Away Wins')

#     for i, team in enumerate(teams):
#         plt.annotate(team, (home_wins[i], away_wins[i]), textcoords="offset points", xytext=(10, 6), ha='center')

#     plt.grid(True)
#     plt.show()

#     plt.grid(True)
#     plt.show()
#     plt.figure(figsize=(12, 8))
#     plt.scatter(home_losses, away_losses, marker='o', color='red')
#     plt.title('Home Losses vs Away Losses')
#     plt.xlabel('Home Losses')
#     plt.ylabel('Away Losses')

#     for i, team in enumerate(teams):
#         plt.annotate(team, (home_losses[i], away_losses[i]), textcoords="offset points", xytext=(10, 6), ha='center')


#     plt.grid(True)
#     plt.show()


plot_home_away_stats(json_data)