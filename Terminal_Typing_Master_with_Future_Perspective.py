import json
import random
import time
import os

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
    
# Function to get user input during the typing challenge
def getting_user_input():
    return input("Type the words as shown and press Enter: ")

# Function to save the updated leaderboard to a JSON file
def saving_leaderboard(leaderboard):
    try:
        with open("leaderboard.json", "w") as file:
            json.dump(leaderboard, file)
    except (PermissionError, FileNotFoundError) as e:
        print(f"Error saving leaderboard: {e}")

# Function to load the leaderboard from a JSON file
def loading_leaderboard():
    if not os.path.exists("leaderboard.json"):
        return []
    try:
        with open("leaderboard.json", "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

# Function to allow the user to choose a typing category
def choose_typing_category():
    print("\nAvailable Typing Categories:")
    print("1. Random")
    print("2. Technology")
    # Add more categories...

    category_choice = input("Enter the number corresponding to your desired category: ")
    return {
        1: "random",
        2: "technology",
        # Map other numbers to corresponding categories...
    }.get(int(category_choice), "random")

# Function for the time-based typing challenge
def time_based_typing_challenge(username, duration=60):
    start_time = time.time()
    end_time = start_time + duration

    category = choose_typing_category()
    words = loading_words_from_json(category)
    random.shuffle(words)

    print("\nTyping the following words:")
    print(" ".join(words))

    user_input = ""
    current_time = time.time()

    while current_time < end_time:
        user_input = getting_user_input()
        current_time = time.time()

    time_taken = end_time - start_time
    words_typed = len(user_input.split())
    wpm = words_typed / (time_taken / 60)

    print("\nTyping Metrics:")
    print(f"Words Typed: {words_typed}")
    print(f"Time Taken: {time_taken:.2f} seconds")
    print(f"Words Per Minute (WPM): {wpm:.2f}")

    updating_leaderboard(username, wpm)
    showing_leaderboard()

# Main function to run the terminal typing master program
def main():
    print("🎰 Terminal Typing Master 🎰")
    username = input("Enter your username: ")

    while True:
        print("\nMenu:")
        print("1. Start Typing Test")
        print("2. Show Leaderboard")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        try:
            choice = int(choice)
        except ValueError:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue

        if choice == 1:
            time_based_typing_challenge(username)

        elif choice == 2:
            showing_leaderboard()

        elif choice == 3:
            print("Exiting. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
