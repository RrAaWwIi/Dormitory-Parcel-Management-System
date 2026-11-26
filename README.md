# Dormitory-Parcel-Management-System

Dormitory Parcel Management System
A terminal-based Python program that helps dormitory staff manage parcels that arrive for students. Staff can register parcels, search for them, record when they are collected, and calculate overdue storage fees. All records are saved to a JSON file, so nothing is lost when the program closes.

Author: Your name Course: Course name and code Date: Submission date

Features
Menu option	What it does
1. Register Incoming Parcel	Records the student's name, room number, tracking number and arrival time. New parcels start as "Waiting for pickup".
2. Search Parcel by Student Name	Finds every parcel for a student. Ignores upper/lower case and accepts part of a name.
3. Search Parcel by Tracking Number	Finds one parcel by its unique tracking number.
4. Save and Exit	Saves all records to parcels.json and closes the program.
5. Record Parcel Pickup	Marks a parcel as "Collected", saves the pickup time and shows any fee owed.
6. View Parcel Collection Information	Shows two tables: parcels still waiting, and parcels already collected.
7. Calculate Overdue Storage Fee	Shows the fee for one parcel, or lists every overdue parcel with the total owed.
Storage fee rules
The first 3 days of storage are free.
After that, the fee is $1.00 for each full day.
For a collected parcel, the fee stops growing at the pickup time.
Example: a parcel stored for 6 days 8 hours has 6 full days, minus the 3 free days, which gives 3 overdue days, so the fee is $3.00.

The rules can be changed in parcel.py:

FREE_STORAGE_DAYS = 3
FEE_PER_DAY = 1.00
CURRENCY = "$"
Requirements
Python 3.7 or newer. No extra packages are needed. The program only uses Python's built-in json, os and datetime modules.
How to run
In VS Code
Install Python from python.org, and install the Python extension in VS Code.
Choose File → Open Folder… and open the project folder.
Open main.py and click the ▶ Run button in the top-right corner.
In a terminal
python3 main.py
(On Windows, use python main.py.)

When typing dates, use the format YYYY-MM-DD HH:MM, for example 2026-11-26 14:30. Press Enter to use the current date and time instead.

Project structure
parcel_system/
├── main.py            # Terminal menu: asks for input and shows results
├── parcel.py          # Parcel class: one parcel's data and fee calculation
├── parcel_manager.py  # ParcelManager class: list of parcels, rules, JSON saving/loading
├── parcels.json       # Saved records (created automatically on first save)
└── README.md          # This file
How the files work together
main.py only talks to the user (input() and print()).
parcel_manager.py holds the list of all parcels and enforces the rules, such as no duplicate tracking numbers and no pickup before arrival. It saves to the JSON file every time a record changes.
parcel.py describes a single parcel. It can convert itself to and from a dictionary for JSON, and it can calculate its own overdue fee.
Design choices
Classes: Parcel groups the data for one parcel. ParcelManager keeps every rule and the saving logic in one place.
List: all parcels are stored in a list, because the number of parcels keeps growing and we often need to loop through them.
Dictionaries: each parcel is converted to a dictionary before saving, because JSON objects and Python dictionaries have the same key/value shape.
JSON: a simple, readable text format that is supported by Python's built-in json module.
datetime: used for arrival and pickup times. Subtracting two datetimes gives the storage duration that the fee is based on.
Data file (parcels.json)
Each parcel is saved like this:

{
    "student_name": "Aisha Rahman",
    "room_number": "B204",
    "tracking_number": "TRK123",
    "arrival_time": "2026-11-20T09:15:00",
    "status": "Collected",
    "pickup_time": "2026-11-23T10:00:00"
}
pickup_time is null for parcels that are still waiting.

Error handling
Empty input, invalid dates, future dates and invalid menu choices are rejected with a message, and the user is asked again.
Duplicate tracking numbers are blocked.
A parcel cannot be collected twice, or before it arrived.
Pickup must be confirmed with y before it is recorded.
Missing file: on the first run the program simply starts with no records.
Damaged file: the file is renamed to parcels.json.backup so the old data is never overwritten, and the program starts with no records.
Records are saved right after every change, so a crash does not lose data.
Testing
Each stage was tested before the next one was started:

Registration: valid input, empty fields, invalid and future dates, and duplicate tracking numbers.
Searching: full name, part of a name in a different case, lowercase tracking numbers, and no results.
JSON: records stayed available after restarting the program (including from a different folder), and missing or damaged files were handled.
Pickup: normal pickup, already collected, unknown parcel, pickup before arrival, cancelled pickup, and the pickup still being there after a restart.
Fees: exact boundaries (3 days 23h 59m → $0.00, exactly 4 days → $1.00), and a collected parcel's fee staying the same over time.
Full system: every menu option in one session, followed by a restart.
Possible future improvements
Let staff edit or delete a parcel that was entered by mistake.
Record whether the overdue fee has been paid.
Send an email notification to the student when a parcel arrives.
