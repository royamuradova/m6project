# main.py
from schedule import Schedule

CSV_PATH = "data/STEM - Summer 2022 Schedule of Classes as of 05-02-22.csv"

def load_schedule() -> Schedule:
    schedule = Schedule()
    try:
        schedule.load_csv(CSV_PATH)
        print("✅ Schedule data loaded successfully.")
    except FileNotFoundError:
        print("❌ CSV file not found. Check the file path and name.")
    return schedule

def main() -> None:
    schedule = load_schedule()

    while True:
        print("\n--- COURSE SCHEDULE SYSTEM ---")
        print("1. Display all courses")
        print("2. Search by subject")
        print("3. Search by subject and catalog")
        print("4. Search by instructor last name")
        print("5. Quit")

        choice = input("Enter option (1–5): ").strip()

        if choice == "1":
            schedule.print()

        elif choice == "2":
            subject = input("Enter subject (e.g., BIO, CHM, MDE): ").strip().upper()
            results = schedule.find_by_subject(subject)
            if results:
                schedule.print(results)
            else:
                print("No courses found for that subject.")

        elif choice == "3":
            subject = input("Enter subject (e.g., BIO): ").strip().upper()
            catalog = input("Enter catalog number (e.g., 141): ").strip()
            results = schedule.find_by_subject_catalog(subject, catalog)
            if results:
                schedule.print(results)
            else:
                print("No courses found for that subject/catalog.")

        elif choice == "4":
            last_name = input("Enter instructor last name (e.g., Abrahams, Anderson): ").strip()
            results = schedule.find_by_instructor_last_name(last_name)
            if results:
                schedule.print(results)
            else:
                print("No courses found for that instructor.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
