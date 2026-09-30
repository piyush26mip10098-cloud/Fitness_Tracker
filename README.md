# 🏋️ Fitness & Habit Tracker

A simple **Python-based command-line Fitness & Habit Tracker** that allows users to record workouts, track fitness habits, monitor progress, and generate basic fitness reports.

The project is divided into separate Python modules so that input validation, data storage, workout management, habit management, progress tracking, and the main menu are handled independently.

---

## 📌 Features

- ➕ Add a workout
- 📋 View workout history
- 🗑️ Delete a workout
- 🎯 Add fitness habits
- ✅ Mark habits as completed for specific dates
- 📊 View overall fitness progress
- 📅 View weekly workout progress
- 📝 Generate a fitness report
- 💾 Store data permanently in a JSON file
- ✔️ Validate numbers, dates, and text input

---

## 📂 Project Structure

```text
Fitness-Habit-Tracker/
│
├── main.py
├── storage.py
├── validation.py
├── workout.py
├── habit.py
├── progress.py
│
└── data/
    └── fitness_data.json
```

> `fitness_data.json` is created automatically inside the `data` folder when the program initializes.

---

# 🧩 Modules & Execution Order

The modules are organized below according to how the application works and how the files depend on one another.

## 1. `storage.py` — Data Storage Layer

This module handles reading and writing the application's data.

### Main responsibilities

- Create the `data` folder if it does not exist
- Create `fitness_data.json` with an initial structure
- Load existing fitness data
- Save updated fitness data

The initial data structure contains:

```python
{
    "workouts": [],
    "habits": []
}
```

### Functions

- `initialize_data()`
- `load_data()`
- `save_data()`

All workout, habit, and progress features use this module to access stored data.

---

## 2. `validation.py` — Input Validation

This module makes sure that user input is valid before it is used by the application.

### Validation functions

#### `get_positive_integer()`

Accepts only positive integers.

Used for values such as:

- Workout duration
- Calories burned
- Workout selection numbers

#### `get_date()`

Accepts dates in:

```text
YYYY-MM-DD
```

format.

#### `get_non_empty_string()`

Prevents the user from entering empty text.

Used for values such as:

- Workout type
- Habit name

---

## 3. `workout.py` — Workout Management

This module manages the user's workout records.

### `add_workout()`

Allows the user to enter:

- Workout type
- Duration in minutes
- Calories burned
- Date

The workout is then added to the stored workout list.

Example workout structure:

```python
{
    "type": "Running",
    "duration": 30,
    "calories": 250,
    "date": "2026-09-30"
}
```

### `view_workouts()`

Displays all recorded workouts along with:

- Workout type
- Duration
- Calories
- Date

### `delete_workout()`

Allows the user to select a workout by its displayed number and remove it from the workout history.

---

## 4. `habit.py` — Habit Tracking

This module manages fitness habits.

### `add_habit()`

Creates a new habit with:

- Habit name
- List of completed dates

Example:

```python
{
    "name": "Drink 2L Water",
    "completed_dates": []
}
```

### `view_habits()`

Displays all tracked habits and the number of days each habit has been completed.

### `complete_habit()`

Allows the user to select a habit and enter the date on which it was completed.

The program also prevents the same habit from being marked complete twice for the same date.

---

## 5. `progress.py` — Progress & Reports

This module analyzes the stored workout and habit data.

### `show_progress()`

Displays overall statistics such as:

- Total workouts
- Total workout time
- Total calories burned
- Number of habits tracked
- Total habit completions

### `weekly_progress()`

Allows the user to enter any date from a particular week.

The program calculates:

- Monday of that week
- Sunday of that week

It then displays workouts that occurred during that week and calculates:

- Number of workouts
- Total workout duration
- Total calories burned

### `generate_report()`

Generates a summary based on all recorded workouts, including:

- Number of workouts
- Total duration
- Total calories
- Average workout duration
- Average calories burned per workout

---

## 6. `main.py` — Main Program / Entry Point

`main.py` is the starting point of the application.

It imports the functions from the other modules and connects them through the main menu.

The application menu provides:

```text
1. Add Workout
2. View Workouts
3. Delete Workout
4. Add Habit
5. View Habits
6. Complete Habit
7. View Fitness Progress
8. Weekly Progress
9. Generate Fitness Report
10. Exit
```

Before the menu starts, the program initializes the data storage.

The program then continuously displays the menu until the user selects **10. Exit**.

---

# 🔄 How the Application Works

The overall flow of the program is:

```text
                    ┌─────────────┐
                    │   main.py   │
                    │ Main Menu   │
                    └──────┬──────┘
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼
     workout.py        habit.py        progress.py
          │                │                │
          └────────────────┼────────────────┘
                           │
                           ▼
                    ┌─────────────┐
                    │ storage.py  │
                    │ JSON Data   │
                    └──────┬──────┘
                           │
                           ▼
                 data/fitness_data.json

        validation.py supports user input
        throughout workout.py and habit.py
```

---

# 💾 Data Storage

The project uses a JSON file instead of a database.

Data is stored in:

```text
data/fitness_data.json
```

The program automatically creates the folder and JSON file if they do not already exist.

This makes the application simple to run without requiring an external database.

---

# ▶️ How to Run

## Requirements

- Python 3.x

No external Python packages are required.

## Run the application

Open a terminal in the project directory and run:

```bash
python main.py
```

The main menu will appear in the terminal.

---

# 🧪 Example Usage

```text
========================================
        FITNESS & HABIT TRACKER
========================================
1. Add Workout
2. View Workouts
3. Delete Workout
4. Add Habit
5. View Habits
6. Complete Habit
7. View Fitness Progress
8. Weekly Progress
9. Generate Fitness Report
10. Exit
========================================
```

For example, a user can:

1. Add a running workout.
2. Add a habit such as daily exercise.
3. Mark the habit as completed.
4. View overall fitness progress.
5. Check progress for a particular week.
6. Generate a fitness report.

---

# 🛡️ Input Validation

The application validates important user inputs.

### Positive numbers

Values such as duration and calories must be greater than zero.

### Dates

Dates must follow:

```text
YYYY-MM-DD
```

### Text

Workout types and habit names cannot be empty.

### Menu choices

The main menu checks whether the entered option is between `1` and `10`.

---

# 🧱 Design Approach

The project uses a **modular programming approach**.

Instead of placing the entire application inside one Python file, functionality is separated into modules:

| Module | Responsibility |
|---|---|
| `storage.py` | JSON data storage |
| `validation.py` | Input validation |
| `workout.py` | Workout management |
| `habit.py` | Habit management |
| `progress.py` | Statistics and reports |
| `main.py` | Main menu and program flow |

This separation makes the program easier to understand, maintain, and extend.

---

# 🚀 Possible Future Improvements

The current project can be extended with features such as:

- 🔐 User accounts and login
- 📈 Graphical progress charts
- 🔥 Workout streak tracking
- 🎯 Fitness goals
- 🏆 Achievement/badge system
- 📆 Monthly and yearly reports
- 🔎 Search and filter workouts
- ✏️ Edit existing workouts
- 💻 GUI version using Tkinter
- 🌐 Web version with Flask or Django
- 🗄️ Database support using SQLite

---

# 👨‍💻 Technologies Used

- **Python**
- **JSON**
- **Command-Line Interface (CLI)**
- Python standard library modules:
  - `json`
  - `os`
  - `datetime`

---

# 📚 Project Learning Outcomes

This project demonstrates practical use of:

- Functions
- Modules and imports
- Lists and dictionaries
- Loops and conditional statements
- Exception handling
- Input validation
- File handling
- JSON data storage
- Date manipulation
- Basic data analysis
- Modular program design

---

## 📄 License

This project is created for educational and learning purposes.
