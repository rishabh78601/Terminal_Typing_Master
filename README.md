# 🎮 Terminal Typing Master 🕹️

Objective : A terminal-based application that tests your typing speed by presenting random words from a selected category. The program measures metrics like words typed, time taken, and words per minute (WPM).

## 📚 Table of Contents
- [🧠 Prerequisites](#prerequisites)
- [🚀 Installation](#installation)
- [💡 Usage](#usage)
- [🔧 Code Components](#code-components)
- [📁 Files](#files)
- [🚀 Future Perspective](#future-perspective)

## 🧠 Prerequisites
- Python 3.x installed
- Basic understanding of file I/O, data structures (list, dictionaries), and JSON format.

## 🚀 Installation
1. Clone the repository: `git clone https://github.com/your-username/terminal-typing-master.git`
2. Navigate to the project directory: `cd terminal-typing-master`
3. Run the program: `python main.py` (replace `python` with your Python interpreter if needed).

## 💡 Usage
1. Enter your username when prompted.
2. Choose from the menu options:
   - 1️⃣ Start Typing Test
   - 2️⃣ Show Leaderboard
   - 3️⃣ Exit

## 🔧 Code Components
### Functions
- **update_leaderboard(username, wpm):** Updates and sorts the leaderboard stored in a JSON file.
- **show_leaderboard():** Displays the leaderboard from the JSON file.
- **load_words_from_json(category):** Loads words from a JSON file into a Python dictionary.
- **get_user_input():** Captures user input during the typing challenge.
- **main():** Contains the main game logic.

### Files
- **leaderboard.json:** Stores leaderboard data.
- **random_words.json:** Example JSON file for the random word category.

## 🚀 Future Perspective
1. Add more typing categories for a diverse experience.
2. Implement a time-based challenge mode for additional difficulty.

**Note:** Feel free to contribute by adding new categories, improving algorithms, or enhancing the user interface.

Enjoy improving your typing skills! 🚀
