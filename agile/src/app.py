from grade_manager import GradeManager


def main() -> None:
    gm = GradeManager()

    MENU = """
1. Add student
2. Remove student
3. Add course to student
4. Remove course from student
5. Add grade to a course
6. Display student info
7. Display all students info
8. Exit
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
                    credits_str = input(f"Enter credits for {course} (e.g., 3): ").strip()
                    try:
                        credits = float(credits_str)
                    except ValueError:
                        print("❌ Invalid credits. Enter a number greater than 0.")
                        continue
                    if credits <= 0:
                        print("❌ Credits must be greater than 0.")
                        continue
                    if gm.enroll_student_in_course(name, course, credits):
                        print(f"✅ Added course {course} ({credits} cr) for {name}.")
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
                credits_str = input(f"Enter credits for {course} (e.g., 3): ").strip()
                try:
                    credits = float(credits_str)
                except ValueError:
                    print("❌ Invalid credits. Enter a number greater than 0.")
                    continue
                if credits <= 0:
                    print("❌ Credits must be greater than 0.")
                    continue
                if gm.enroll_student_in_course(name, course, credits):
                    print(f"✅ Added course {course} ({credits} cr) for {name}.")
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
            name = input("Enter student name to display: ").strip()
            report = gm.get_student_report(name)
            if not report:
                print("❌ Student not found.")
            else:
                print(f"\nStudent: {report['name']}")
                if not report["courses"]:
                    print("  (no courses)")
                else:
                    for course_name, info in report["courses"].items():
                        credits = info.get("credits", 0)
                        grades = info.get("grades", [])
                        grades_str = ", ".join(str(g) for g in grades) if grades else "(no grades)"
                        avg = info.get("average")
                        avg_str = f"{avg:.2f}" if avg is not None else "N/A"
                        print(f"  - {course_name} ({credits} cr): grades [{grades_str}], avg {avg_str}")
                overall = report.get("overall_average")
                overall_str = f"{overall:.2f}" if overall is not None else "N/A"
                gpa = report.get("weighted_gpa")
                gpa_str = f"{gpa:.3f}" if gpa is not None else "N/A"
                print(f"Overall average: {overall_str}")
                print(f"Weighted GPA (4.000 scale): {gpa_str}\n")
        elif choice == "7":
            reports = gm.get_all_students_report()
            if not reports:
                print("No students yet.")
            else:
                for report in reports:
                    print(f"\nStudent: {report['name']}")
                    if not report["courses"]:
                        print("  (no courses)")
                    else:
                        for course_name, info in report["courses"].items():
                            credits = info.get("credits", 0)
                            grades = info.get("grades", [])
                            grades_str = ", ".join(str(g) for g in grades) if grades else "(no grades)"
                            avg = info.get("average")
                            avg_str = f"{avg:.2f}" if avg is not None else "N/A"
                            print(f"  - {course_name} ({credits} cr): grades [{grades_str}], avg {avg_str}")
                    overall = report.get("overall_average")
                    overall_str = f"{overall:.2f}" if overall is not None else "N/A"
                    gpa = report.get("weighted_gpa")
                    gpa_str = f"{gpa:.3f}" if gpa is not None else "N/A"
                    print(f"Overall average: {overall_str}")
                    print(f"Weighted GPA (4.000 scale): {gpa_str}")
                print("")
        elif choice == "8":
            print("Bye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()