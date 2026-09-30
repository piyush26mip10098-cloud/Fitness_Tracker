from workout import (
    add_workout,
    view_workouts,
    delete_workout
)

from habit import (
    add_habit,
    view_habits,
    complete_habit
)

from progress import (
    show_progress,
    generate_report,
    weekly_progress
)

from storage import initialize_data


def display_menu():
    """Display the main menu."""

    print("\n")
    print("========================================")
    print("        FITNESS & HABIT TRACKER")
    print("========================================")
    print("1. Add Workout")
    print("2. View Workouts")
    print("3. Delete Workout")
    print("4. Add Habit")
    print("5. View Habits")
    print("6. Complete Habit")
    print("7. View Fitness Progress")
    print("8. Weekly Progress")
    print("9. Generate Fitness Report")
    print("10. Exit")
    print("========================================")


def main():
    """Run the Fitness & Habit Tracker."""

    initialize_data()

    while True:

        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_workout()

        elif choice == "2":
            view_workouts()

        elif choice == "3":
            delete_workout()

        elif choice == "4":
            add_habit()

        elif choice == "5":
            view_habits()

        elif choice == "6":
            complete_habit()

        elif choice == "7":
            show_progress()

        elif choice == "8":
            weekly_progress()

        elif choice == "9":
            generate_report()



        elif choice == "10":

            print("\nThank you for using Fitness & Habit Tracker! 💪")

            break


        else:

            print("\nInvalid choice. Please select 1-10.")


if __name__ == "__main__":
    main()