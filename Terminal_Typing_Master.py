import json
import random
import time
import os
import getpass 

# Function to update the leaderboard with a new entry
def updating_leaderboard(username, wpm):
    leaderboard = loading_leaderboard()
    leaderboard.append({"username": username, "wpm": wpm})
    leaderboard.sort(key=lambda x: x["wpm"], reverse=True)
    saving_leaderboard(leaderboard)

# Function to display the leaderboard
def showing_leaderboard():
    leaderboard = loading_leaderboard()

    print("\nLeaderboard:")
    print("Username\tWPM")
    print("===================")
    for entry in leaderboard:
        print(f"{entry['username']}\t\t{entry['wpm']}")
    print("===================")

# Function to load words from a JSON file based on the selected category
def loading_words_from_json(category):
    file_path = f"{category.lower()}_words.json"
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            words_data = json.load(file)
            return words_data["words"]
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading words: {e}")
        return []