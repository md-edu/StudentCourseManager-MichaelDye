from typing import Dict, List

class Student:
    def __init__(self, name: str) -> None:
        self.name = name
        self.courses: List[str] = []
        self.grades_by_course: Dict[str, List[int]] = {}

    def enroll_in_course(self, course_name: str) -> bool:
        course_name = course_name.strip()
        if not course_name or course_name in self.courses:
            return False
        self.courses.append(course_name)
        if course_name not in self.grades_by_course:
            self.grades_by_course[course_name] = []
        return True

    def remove_course(self, course_name: str) -> bool:
        course_name = course_name.strip()
        if course_name not in self.courses:
            return False
        self.courses.remove(course_name)
        if course_name in self.grades_by_course:
            del self.grades_by_course[course_name]
        return True

    def add_grade(self, course_name: str, grade: int) -> bool:
        course_name = course_name.strip()
        if course_name not in self.courses:
            return False
        if not isinstance(grade, int) or grade < 0 or grade > 100:
            return False
        self.grades_by_course.setdefault(course_name, []).append(grade)
        return True


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

    def enroll_student_in_course(self, student_name: str, course_name: str) -> bool:
        key = student_name.strip().lower()
        if key not in self.students or not course_name.strip():
            return False
        return self.students[key].enroll_in_course(course_name.strip())

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