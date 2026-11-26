"""
parcel.py

Defines the Parcel class. One Parcel object represents one parcel
that has arrived at the dormitory parcel room.
"""

from datetime import datetime
from typing import TypedDict

# The format used to show dates and times, for example "2026-11-26 14:30".
# %Y = year, %m = month, %d = day, %H = hour (24h), %M = minute.
DATE_FORMAT = "%Y-%m-%d %H:%M"

# The status every new parcel starts with.
STATUS_WAITING = "Waiting for pickup"


class ParcelDict(TypedDict):
    student_name: str
    room_number: str
    tracking_number: str
    arrival_time: str
    status: str


class Parcel:
    """Represents a single parcel stored at the dormitory."""

    def __init__(
        self,
        student_name: str,
        room_number: str,
        tracking_number: str,
        arrival_time: datetime,
        status: str = STATUS_WAITING,
    ) -> None:
        """
        Create a new Parcel.

        Parameters:
            student_name (str): Name of the student the parcel is for.
            room_number (str): The student's room number, e.g. "B204".
            tracking_number (str): The courier's tracking number.
            arrival_time (datetime): When the parcel arrived.
            status (str): Current status. New parcels are waiting.
        """
        self.student_name: str = student_name
        self.room_number: str = room_number
        self.tracking_number: str = tracking_number
        self.arrival_time: datetime = arrival_time
        self.status: str = status

    def display(self) -> None:
        """Print this parcel's information in a readable layout."""
        print("-" * 40)
        print(f"Student name    : {self.student_name}")
        print(f"Room number     : {self.room_number}")
        print(f"Tracking number : {self.tracking_number}")
        print(f"Arrival time    : {self.arrival_time.strftime(DATE_FORMAT)}")
        print(f"Status          : {self.status}")
        print("-" * 40)

    def to_dict(self) -> ParcelDict:
        """
        Convert this parcel into a dictionary so it can be saved as JSON.

        JSON cannot store datetime objects, so the arrival time is
        turned into text first, e.g. "2026-11-20T09:15:00".
        """
        return {
            "student_name": self.student_name,
            "room_number": self.room_number,
            "tracking_number": self.tracking_number,
            "arrival_time": self.arrival_time.isoformat(),
            "status": self.status,
        }


def parcel_from_dict(data: ParcelDict) -> Parcel:
    """
    Create a Parcel object from a dictionary that was loaded from JSON.

    This is the opposite of Parcel.to_dict().

    Raises:
        KeyError: If a required field is missing from the dictionary.
        ValueError: If the arrival time text is not a valid date.
    """

    return Parcel(
        data["student_name"],
        data["room_number"],
        data["tracking_number"],
        datetime.fromisoformat(data["arrival_time"]),
        data["status"],
    )
