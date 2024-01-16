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