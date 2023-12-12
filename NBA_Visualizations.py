#Visualizations

import requests
import http.client
import json
import sqlite3
import unittest
import os
import matplotlib.pyplot as plt

with open('calculations.txt', 'r') as file:
    data = file.readlines()

# Parsing the data
categories = []
values = []

for line in data:
    category, value = line.split(':')
    categories.append(category.strip())
    values.append(float(value.strip()))

colors = ['red', 'green', 'blue', 'orange', 'purple']

plt.figure(figsize=(10, 6))
for i in range(len(categories)):
    plt.bar(categories[i], values[i], color=colors[i])

plt.xlabel('Categories')
plt.ylabel('Average Values')
plt.title('Bar Graph of Average Home and Away, Wins, Losses, and Point Differential')
plt.xticks(rotation=45)
plt.grid(axis='y')

# Display the bar graph
plt.show()