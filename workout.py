from storage import load_data, save_data
from validation import (
    get_positive_integer,
    get_date,
    get_non_empty_string
)


def add_workout():
    """Add a new workout."""

    data = load_data()

    print("\n========== ADD WORKOUT ==========")

    workout_type = get_non_empty_string(
        "Enter workout type: "
    )

    duration = get_positive_integer(
        "Enter duration in minutes: "
    )

    calories = get_positive_integer(
        "Enter calories burned: "
    )

    date = get_date(
        "Enter date (YYYY-MM-DD): "
    )

    workout = {
        "type": workout_type,
        "duration": duration,
        "calories": calories,
        "date": date
    }

    data["workouts"].append(workout)

    save_data(data)

    print("\nWorkout added successfully! ✅")


def view_workouts():
    """Display all recorded workouts."""

    data = load_data()

    workouts = data["workouts"]

    print("\n========== WORKOUT HISTORY ==========")

    if not workouts:
        print("No workouts recorded yet.")
        return

    for index, workout in enumerate(workouts, start=1):
        print(f"\nWorkout {index}")
        print(f"Type      : {workout['type']}")
        print(f"Duration  : {workout['duration']} minutes")
        print(f"Calories  : {workout['calories']} kcal")
        print(f"Date      : {workout['date']}")


def delete_workout():
    """Delete a workout from the history."""

    data = load_data()

    workouts = data["workouts"]

    if not workouts:
        print("\nNo workouts available to delete.")
        return

    view_workouts()

    choice = get_positive_integer(
        "\nEnter workout number to delete: "
    )

    if choice > len(workouts):
        print("Invalid workout number.")
        return

    deleted_workout = workouts.pop(choice - 1)

    save_data(data)

    print(
        f"\nDeleted {deleted_workout['type']} workout successfully! 🗑️"
    )