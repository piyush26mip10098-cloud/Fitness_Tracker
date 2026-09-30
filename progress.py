from datetime import datetime, timedelta

from storage import load_data
from validation import get_date


def show_progress():
    """Display overall fitness statistics."""

    data = load_data()

    workouts = data["workouts"]
    habits = data["habits"]

    print("\n========== FITNESS PROGRESS ==========")

    total_workouts = len(workouts)

    total_duration = 0
    total_calories = 0

    for workout in workouts:
        total_duration += workout["duration"]
        total_calories += workout["calories"]

    total_habit_completions = 0

    for habit in habits:
        total_habit_completions += len(habit["completed_dates"])

    print(f"Total workouts        : {total_workouts}")
    print(f"Total workout time    : {total_duration} minutes")
    print(f"Total calories burned : {total_calories} kcal")
    print(f"Habits tracked        : {len(habits)}")
    print(f"Habit completions     : {total_habit_completions}")


def generate_report():
    """Generate a detailed fitness report."""

    data = load_data()

    workouts = data["workouts"]

    print("\n========== FITNESS REPORT ==========")

    if not workouts:
        print("No workout data available.")
        return

    total_duration = 0
    total_calories = 0

    for workout in workouts:
        total_duration += workout["duration"]
        total_calories += workout["calories"]

    average_duration = total_duration / len(workouts)
    average_calories = total_calories / len(workouts)

    print(f"Number of workouts : {len(workouts)}")
    print(f"Total duration     : {total_duration} minutes")
    print(f"Total calories     : {total_calories} kcal")
    print(f"Average duration   : {average_duration:.2f} minutes")
    print(f"Average calories   : {average_calories:.2f} kcal")


def weekly_progress():
    """Display workouts completed during a selected week."""

    data = load_data()

    workouts = data["workouts"]

    print("\n========== WEEKLY PROGRESS ==========")

    if not workouts:
        print("No workouts recorded yet.")
        return

    # Get a date from the user
    selected_date = get_date(
        "Enter any date from the week (YYYY-MM-DD): "
    )

    # Convert string into a date object
    selected_date = datetime.strptime(
        selected_date,
        "%Y-%m-%d"
    ).date()

    # Find Monday of that week
    week_start = selected_date - timedelta(
        days=selected_date.weekday()
    )

    # Find Sunday of that week
    week_end = week_start + timedelta(days=6)

    weekly_workouts = []

    # Check every workout
    for workout in workouts:

        workout_date = datetime.strptime(
            workout["date"],
            "%Y-%m-%d"
        ).date()

        if week_start <= workout_date <= week_end:
            weekly_workouts.append(workout)

    print(
        f"\nWeek: {week_start} to {week_end}"
    )

    if not weekly_workouts:
        print("No workouts recorded during this week.")
        return

    total_duration = 0
    total_calories = 0

    print("\nWorkouts this week:")

    for workout in weekly_workouts:

        print(
            f"- {workout['date']} | "
            f"{workout['type']} | "
            f"{workout['duration']} minutes | "
            f"{workout['calories']} kcal"
        )

        total_duration += workout["duration"]
        total_calories += workout["calories"]

    print("\n========== SUMMARY ==========")
    print(f"Number of workouts : {len(weekly_workouts)}")
    print(f"Total duration     : {total_duration} minutes")
    print(f"Total calories     : {total_calories} kcal")