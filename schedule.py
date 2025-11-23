# schedule.py
import csv
from typing import List, Iterable
from schedule_item import ScheduleItem

class Schedule:
    """
    Manages all schedule items using a dictionary (hash table).
    Keys are strings like 'BIO_141_D01'.
    """
    def __init__(self) -> None:
        self.data: dict[str, ScheduleItem] = {}

    def add_entry(self, item: ScheduleItem) -> None:
        """
        Add a ScheduleItem to the internal dictionary.
        """
        self.data[item.get_key()] = item

    def load_csv(self, filename: str) -> None:
        """
        Load data from the CSV file using csv.DictReader.
        """
        with open(filename, encoding="utf-8-sig", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Create ScheduleItem from required columns
                item = ScheduleItem(
                    subject=row["Subject"],
                    catalog=row["Catalog"],
                    section=row["Section"],
                    component=row["Component"],
                    session=row["Session"],
                    units=int(row["Units"]),
                    total_enrolled=int(row["TotEnrl"]),
                    capacity=int(row["CapEnrl"]),
                    instructor=row["Instructor"],
                )
                self.add_entry(item)

    def print_header(self) -> None:
        """
        Print the header row for the schedule report.
        """
        print("Subject  Catalog Section  Component  Session Units TotEnrl  CapEnrl Instructor")
        print("-------  ------- -------- ---------- ------- ----- -------- ------- ----------")

    def print(self, items: Iterable[ScheduleItem] | None = None) -> None:
        """
        Print either all items or a filtered list.
        """
        self.print_header()
        if items is None:
            items = self.data.values()
        for item in items:
            item.print()

    # --------- Search methods using list comprehensions --------- #

    def find_by_subject(self, subject: str) -> List[ScheduleItem]:
        """
        Return all courses that match a given subject (e.g., 'BIO').
        """
        return [
            item for item in self.data.values()
            if item.subject.lower() == subject.lower()
        ]

    def find_by_subject_catalog(self, subject: str, catalog: str) -> List[ScheduleItem]:
        """
        Return all courses that match a given subject and catalog (e.g., 'BIO', '141').
        """
        return [
            item for item in self.data.values()
            if item.subject.lower() == subject.lower()
            and item.catalog == catalog
        ]

    def find_by_instructor_last_name(self, last_name: str) -> List[ScheduleItem]:
        """
        Return all courses where the instructor last name starts with last_name.
        Example CSV field: 'Abrahams,Shaheem' or 'Anderson Jr.,William Michael'
        """
        last_name = last_name.lower()
        return [
            item for item in self.data.values()
            if item.instructor.lower().startswith(last_name)
        ]
