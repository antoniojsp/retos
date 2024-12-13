from datetime import datetime

class Student:
    def __init__(self, name):
        self.name = name
        self._enrollments = []

    def enroll(self, course):
        if isinstance(course, Course):
            enrollment = Enrollment(self, course)
            self._enrollments.append(enrollment)
            course.add_enrollment(enrollment)
        else:
            raise TypeError("course must be an instance of Course")

    def get_enrollments(self):
        return self._enrollments.copy()

    def course_count(self):
        return len(self._enrollments)

    def aggregate_average_grade(self):
        # lets assume the grades are stored in a protected attribute called _grades.
        total_grades = sum(self._grades.values())
        num_courses = len(self._grades)
        average_grade = total_grades / num_courses

        return average_grade


class Course:
    def __init__(self, title):

        self.title = title
        self._enrollments = []

    def add_enrollment(self, enrollment):
        if isinstance(enrollment, Enrollment):
            self._enrollments.append(enrollment)
        else:
            raise TypeError("enrollment must be an instance of Enrollment")

    def get_enrollments(self):
        return self._enrollments.copy()


class Enrollment:
    all = []

    def __init__(self, student, course):
        if isinstance(student, Student) and isinstance(course, Course):
            self.student = student
            self.course = course
            self._enrollment_date = datetime.now()
            type(self).all.append(self)
        else:
            raise TypeError("Invalid types for student and/or course")

    def get_enrollment_date(self):
        return self._enrollment_date

    @classmethod
    def aggregate_enrollments_per_day(cls):
        enrollment_count = {}
        for enrollment in cls.all:
            date = enrollment.get_enrollment_date().date()
            enrollment_count[date] = enrollment_count.get(date, 0) + 1
        return enrollment_count


# Create Students
student1 = Student("Alice")
student2 = Student("Bob")

# Create Courses
course1 = Course("Math 101")
course2 = Course("Physics 101")

# Enroll students in courses
student1.enroll(course1)
student1.enroll(course2)
student2.enroll(course1)

# Retrieve enrollments for a student
print("Enrollments for Alice:")
for enrollment in student1.get_enrollments():
    print(f"Course: {enrollment.course.title}, Date: {enrollment.get_enrollment_date()}")

print("\nEnrollments for Bob:")
for enrollment in student2.get_enrollments():
    print(f"Course: {enrollment.course.title}, Date: {enrollment.get_enrollment_date()}")

# Count courses a student is enrolled in
print(f"\nAlice is enrolled in {student1.course_count()} courses.")
print(f"Bob is enrolled in {student2.course_count()} courses.")

# Assuming we manually add a `_grades` dictionary to each student to test aggregate_average_grade
# Let's say Alice has grades in Math 101 and Physics 101
student1._grades = {course1: 85, course2: 90}
print(f"\nAlice's average grade: {student1.aggregate_average_grade()}")

# Aggregate enrollments per day across all enrollments
print("\nEnrollments per day:")
for date, count in Enrollment.aggregate_enrollments_per_day().items():
    print(f"Date: {date}, Enrollments: {count}")

print(student1.aggregate_average_grade())