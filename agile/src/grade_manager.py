from typing import Dict, List

class Student:
    def __init__(self, name: str) -> None:
        self.name = name
        self.courses: List[str] = []
        self.grades_by_course: Dict[str, List[int]] = {}
        self.course_credits: Dict[str, float] = {}

    def enroll_in_course(self, course_name: str, credits: float) -> bool:
        course_name = course_name.strip()
        try:
            credits_value = float(credits)
        except (TypeError, ValueError):
            return False
        if not course_name or course_name in self.courses or credits_value <= 0:
            return False
        self.courses.append(course_name)
        if course_name not in self.grades_by_course:
            self.grades_by_course[course_name] = []
        self.course_credits[course_name] = credits_value
        return True

    def remove_course(self, course_name: str) -> bool:
        course_name = course_name.strip()
        if course_name not in self.courses:
            return False
        self.courses.remove(course_name)
        if course_name in self.grades_by_course:
            del self.grades_by_course[course_name]
        if course_name in self.course_credits:
            del self.course_credits[course_name]
        return True

    def add_grade(self, course_name: str, grade: int) -> bool:
        course_name = course_name.strip()
        if course_name not in self.courses:
            return False
        if not isinstance(grade, int) or grade < 0 or grade > 100:
            return False
        self.grades_by_course.setdefault(course_name, []).append(grade)
        return True

    def get_course_average(self, course_name: str) -> float | None:
        course_name = course_name.strip()
        grades = self.grades_by_course.get(course_name)
        if not grades:
            return None
        return sum(grades) / len(grades)

    def compute_overall_average(self) -> float | None:
        all_grades: List[int] = []
        for grades in self.grades_by_course.values():
            all_grades.extend(grades)
        if not all_grades:
            return None
        return sum(all_grades) / len(all_grades)

    def _percentage_to_points(self, percent: float) -> float:
        # Simple 4.0 scale: A>=90:4.0, B>=80:3.0, C>=70:2.0, D>=60:1.0, F<60:0.0
        if percent >= 90:
            return 4.0
        if percent >= 80:
            return 3.0
        if percent >= 70:
            return 2.0
        if percent >= 60:
            return 1.0
        return 0.0

    def compute_weighted_gpa(self) -> float | None:
        total_points_times_credits = 0.0
        total_credits = 0.0
        for course in self.courses:
            avg = self.get_course_average(course)
            credits = self.course_credits.get(course, 0.0)
            if avg is None or credits <= 0:
                continue
            points = self._percentage_to_points(avg)
            total_points_times_credits += points * credits
            total_credits += credits
        if total_credits == 0.0:
            return None
        return total_points_times_credits / total_credits


class GradeManager:
    def __init__(self) -> None:
        self.students: Dict[str, Student] = {}

    def add_student(self, name: str) -> bool:
        key = name.strip().lower()
        if not name.strip() or key in self.students:
            return False
        self.students[key] = Student(name.strip())
        return True

    def remove_student(self, name: str) -> bool:
        key = name.strip().lower()
        if key not in self.students:
            return False
        del self.students[key]
        return True

    def enroll_student_in_course(self, student_name: str, course_name: str, credits: float) -> bool:
        key = student_name.strip().lower()
        if key not in self.students or not course_name.strip():
            return False
        return self.students[key].enroll_in_course(course_name.strip(), credits)

    def remove_course_from_student(self, student_name: str, course_name: str) -> bool:
        key = student_name.strip().lower()
        if key not in self.students or not course_name.strip():
            return False
        return self.students[key].remove_course(course_name.strip())

    def add_grade(self, student_name: str, course_name: str, grade: int) -> bool:
        key = student_name.strip().lower()
        if key not in self.students:
            return False
        return self.students[key].add_grade(course_name.strip(), grade)

    def get_student_report(self, name: str) -> dict | None:
        key = name.strip().lower()
        student = self.students.get(key)
        if not student:
            return None
        courses: Dict[str, dict] = {}
        for course in student.courses:
            grades = list(student.grades_by_course.get(course, []))
            avg = student.get_course_average(course)
            credits = student.course_credits.get(course, 0.0)
            courses[course] = {
                "credits": credits,
                "grades": grades,
                "average": avg,
            }
        return {
            "name": student.name,
            "courses": courses,
            "overall_average": student.compute_overall_average(),
            "weighted_gpa": student.compute_weighted_gpa(),
        }

    def get_all_students_report(self) -> List[dict]:
        reports: List[dict] = []
        for student in self.students.values():
            report = self.get_student_report(student.name)
            if report is not None:
                reports.append(report)
        # Optional: sort by name for stable output
        reports.sort(key=lambda r: r["name"].lower())
        return reports