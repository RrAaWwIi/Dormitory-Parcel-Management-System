"""
parcel.py

Defines the Parcel class. One Parcel object represents one parcel
that has arrived at the dormitory parcel room.
"""

# The format used to show dates and times, for example "2026-11-26 14:30".
# %Y = year, %m = month, %d = day, %H = hour (24h), %M = minute.
DATE_FORMAT = "%Y-%m-%d %H:%M"

# The status every new parcel starts with.
STATUS_WAITING = "Waiting for pickup"


class Parcel:
    """Represents a single parcel stored at the dormitory."""

    def __init__(self, student_name, room_number, tracking_number,
                 arrival_time, status=STATUS_WAITING):
        """
        Create a new Parcel.
        ...
        """
        self.student_name = student_name
        self.room_number = room_number
        self.tracking_number = tracking_number
        self.arrival_time = arrival_time
        self.status = status

    def display(self):
        """Print this parcel's information in a readable layout."""
        print("-" * 40)
        print(f"Student name    : {self.student_name}")
        print(f"Room number     : {self.room_number}")
        print(f"Tracking number : {self.tracking_number}")
        print(f"Arrival time    : {self.arrival_time.strftime(DATE_FORMAT)}")
        print(f"Status          : {self.status}")
        print("-" * 40)