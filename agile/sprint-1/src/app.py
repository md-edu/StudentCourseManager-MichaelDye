from grade_manager import GradeManager


def main() -> None:
    gm = GradeManager()

    MENU = """
1. Add student
2. Remove student
3. Exit
Choose an option: """
    while True:
        choice = input(MENU).strip()
        if choice == "1":
            name = input("Enter student name: ").strip()
            if gm.add_student(name):
                print(f"✅ Student {name} added.")
                # Add courses at creation time (press Enter to finish)
                while True:
                    course = input("Enter course name (press Enter to finish): ").strip()
                    if course == "":
                        break
                    if gm.enroll_student_in_course(name, course):
                        print(f"✅ Added course {course} for {name}.")
                    else:
                        print("❌ Could not add course (maybe duplicate or invalid).")
            else:
                print("❌ Could not add student (maybe exists or invalid).")
        elif choice == "2":
            name = input("Enter student name to remove: ").strip()
            if gm.remove_student(name):
                print(f"✅ Student {name} removed.")
            else:
                print("❌ Student not found.")
        elif choice == "3":
            print("Bye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()