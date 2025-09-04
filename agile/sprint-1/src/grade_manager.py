from typing import Dict, List

class Student:
    def __init__(self, name: str) -> None:
        self.name = name
        self.courses: List[str] = []

    def enroll_in_course(self, course_name: str) -> bool:
        if course_name in self.courses:
            return False
        self.courses.append(course_name)
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