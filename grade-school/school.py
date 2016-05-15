from collections import defaultdict


class School:

    def __init__(self, name):
        self.school_name = name
        self.grades = defaultdict(set)

    def add(self, student, student_grade):
        self.grades[student_grade].add(student)

    def grade(self, school_grade):
        return self.grades[school_grade]

    def sort(self):
        return [(grade, tuple(students))
                for grade, students in sorted(self.grades.iteritems())]
