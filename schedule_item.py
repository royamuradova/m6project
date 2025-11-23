# schedule_item.py
from dataclasses import dataclass

@dataclass
class ScheduleItem:
    """
    Stores one course row from the CSV file.
    """
    subject: str
    catalog: str
    section: str
    component: str
    session: str
    units: int
    total_enrolled: int
    capacity: int
    instructor: str

    def get_key(self) -> str:
        """
        Return unique key used in the Schedule dictionary.
        Example: BIO_141_D01
        """
        return f"{self.subject}_{self.catalog}_{self.section}"

    def print(self) -> None:
        """
        Print this course in a formatted row.
        """
        print(f"{self.subject:<7} {self.catalog:<7} {self.section:<8} "
              f"{self.component:<10} {self.session:<7} {self.units:<5} "
              f"{self.total_enrolled:<8} {self.capacity:<7} {self.instructor}")
