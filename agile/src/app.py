from grade_manager import GradeManager


def main() -> None:
    gm = GradeManager()

    MENU = """
1. Add student
2. Remove student
3. Add course to student
4. Remove course from student
5. Add grade to a course
6. Exit
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
            name = input("Enter student name: ").strip()
            while True:
                course = input("Enter course name to add (press Enter to finish): ").strip()
                if course == "":
                    break
                if gm.enroll_student_in_course(name, course):
                    print(f"✅ Added course {course} for {name}.")
                else:
                    print("❌ Could not add course (check student or duplicate).")
        elif choice == "4":
            name = input("Enter student name: ").strip()
            while True:
                course = input("Enter course name to remove (press Enter to finish): ").strip()
                if course == "":
                    break
                if gm.remove_course_from_student(name, course):
                    print(f"✅ Removed course {course} from {name}.")
                else:
                    print("❌ Could not remove course (check student or course name).")
        elif choice == "5":
            name = input("Enter student name: ").strip()
            course = input("Enter course name: ").strip()
            while True:
                grade_str = input("Enter grade (0-100) (press Enter to finish): ").strip()
                if grade_str == "":
                    break
                try:
                    grade = int(grade_str)
                except ValueError:
                    print("❌ Invalid grade. Enter an integer 0-100.")
                    continue
                if gm.add_grade(name, course, grade):
                    print(f"✅ Added grade {grade} for {name} in {course}.")
                else:
                    print("❌ Failed to add grade (check student/course or grade range).")
        elif choice == "6":
            print("Bye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()