"""
main.py

Starting point of the Dormitory Parcel Management System.
It shows the terminal menu and asks the user for input.

Stage 3: registration, searching and JSON saving/loading are working.
"""

import os
from datetime import datetime

from parcel import DATE_FORMAT
from parcel_manager import ParcelManager

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "parcels.json")


def get_non_empty_input(prompt):
    """Ask the user for text and keep asking until something is typed."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty. Please try again.")


def get_arrival_time():
    """
    Ask the user for the parcel's arrival date and time.

    Pressing Enter uses the current date and time. Otherwise the user
    must type a date in the format YYYY-MM-DD HH:MM.

    Returns:
        datetime: The arrival date and time.
    """
    while True:
        text = input("Arrival time (YYYY-MM-DD HH:MM), "
                     "or press Enter for now: ").strip()

        if text == "":
            return datetime.now()

        try:
            arrival_time = datetime.strptime(text, DATE_FORMAT)
        except ValueError:
            print("Invalid date/time. Example of a valid value: "
                  "2026-11-26 14:30")
            continue

        if arrival_time > datetime.now():
            print("The arrival time cannot be in the future.")
            continue

        return arrival_time


def register_parcel_menu(manager):
    """Collect parcel details from the user and register the parcel."""
    print("\n--- Register Incoming Parcel ---")
    student_name = get_non_empty_input("Student name: ")
    room_number = get_non_empty_input("Room number: ").upper()
    tracking_number = get_non_empty_input("Tracking number: ").upper()
    arrival_time = get_arrival_time()

    try:
        parcel = manager.register_parcel(student_name, room_number,
                                         tracking_number, arrival_time)
    except ValueError as error:
        print(f"Registration failed: {error}")
        return
    except OSError as error:
        print(f"Warning: the parcel was registered but could not be "
              f"saved to the file: {error}")
        return

    print("\nParcel registered and saved successfully!")
    parcel.display()
    print(f"Total parcels registered: {manager.count_parcels()}")


def search_by_name_menu(manager):
    """Ask for a student name and show every matching parcel."""
    print("\n--- Search Parcel by Student Name ---")
    name = get_non_empty_input("Enter student name (full or part): ")
    results = manager.search_by_student_name(name)

    if len(results) == 0:
        print(f"No parcels found for '{name}'.")
        return

    print(f"\nFound {len(results)} parcel(s):")
    for parcel in results:
        parcel.display()


def search_by_tracking_menu(manager):
    """Ask for a tracking number and show the matching parcel."""
    print("\n--- Search Parcel by Tracking Number ---")
    tracking_number = get_non_empty_input("Enter tracking number: ")
    parcel = manager.find_by_tracking_number(tracking_number)

    if parcel is None:
        print(f"No parcel found with tracking number "
              f"'{tracking_number.upper()}'.")
        return

    print("\nParcel found:")
    parcel.display()


def show_menu():
    """Print the main menu options."""
    print("\n===== Dormitory Parcel Management System =====")
    print("1. Register Incoming Parcel")
    print("2. Search Parcel by Student Name")
    print("3. Search Parcel by Tracking Number")
    print("4. Save and Exit")


def main():
    """Run the main menu loop until the user chooses to exit."""
    manager = ParcelManager(DATA_FILE)
    print(manager.load_from_file())

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            register_parcel_menu(manager)
        elif choice == "2":
            search_by_name_menu(manager)
        elif choice == "3":
            search_by_tracking_menu(manager)
        elif choice == "4":
            try:
                manager.save_to_file()
            except OSError as error:
                # Stay in the menu so the records in memory are not lost.
                print(f"Error: could not save records: {error}")
                continue
            print(f"Saved {manager.count_parcels()} parcel(s) "
                  "to parcels.json. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
