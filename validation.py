from datetime import datetime


def get_positive_integer(message):
    """Ask the user for a positive integer."""

    while True:
        try:
            value = int(input(message))

            if value > 0:
                return value

            print("Please enter a number greater than 0.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def get_date(message):
    """Ask the user for a date in YYYY-MM-DD format."""

    while True:
        date = input(message)

        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date

        except ValueError:
            print("Invalid date. Use YYYY-MM-DD.")


def get_non_empty_string(message):
    """Ask the user for non-empty text."""

    while True:
        value = input(message).strip()

        if value:
            return value

        print("Input cannot be empty.")