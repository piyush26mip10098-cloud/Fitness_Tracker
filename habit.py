from storage import load_data, save_data
from validation import get_non_empty_string, get_date


def add_habit():
    """Add a new fitness habit."""

    data = load_data()

    print("\n========== ADD HABIT ==========")

    habit_name = get_non_empty_string(
        "Enter habit name: "
    )

    habit = {
        "name": habit_name,
        "completed_dates": []
    }

    data["habits"].append(habit)

    save_data(data)

    print("\nHabit added successfully! ✅")


def view_habits():
    """Display all habits."""

    data = load_data()

    habits = data["habits"]

    print("\n========== HABITS ==========")

    if not habits:
        print("No habits added yet.")
        return

    for index, habit in enumerate(habits, start=1):

        completed = len(habit["completed_dates"])

        print(f"\n{index}. {habit['name']}")
        print(f"Completed days: {completed}")


def complete_habit():
    """Mark a habit as completed for a particular date."""

    data = load_data()

    habits = data["habits"]

    if not habits:
        print("\nNo habits available.")
        return

    view_habits()

    try:
        choice = int(
            input("\nEnter habit number: ")
        )

        if choice < 1 or choice > len(habits):
            print("Invalid habit number.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    date = get_date(
        "Enter completion date (YYYY-MM-DD): "
    )

    habit = habits[choice - 1]

    if date in habit["completed_dates"]:
        print("Habit is already marked complete for this date.")
        return

    habit["completed_dates"].append(date)

    save_data(data)

    print("\nHabit marked as completed! 🎯")