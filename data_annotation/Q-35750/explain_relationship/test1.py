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







from datetime import datetime

# Create instances
student1 = Student("Alice")
student2 = Student("Bob")
course1 = Course("Python Programming")
course2 = Course("Data Structures and Algorithms")

# Enroll students in courses
student1.enroll(course1)
student1.enroll(course2)
student2.enroll(course1)

# Access enrollments
student1_enrollments = student1.get_enrollments()
for enrollment in student1_enrollments:
    print(f"{student1.name} enrolled in {enrollment.course.title} on {enrollment.get_enrollment_date()}")

course1_enrollments = course1.get_enrollments()
print(f"\nStudents enrolled in {course1.title}:")
for enrollment in course1_enrollments:
    print(enrollment.student.name)

# Demonstrate aggregate functions (after fixing aggregate_average_grade)
enrollments_per_day = Enrollment.aggregate_enrollments_per_day()
print("\nEnrollments per day:")
for date, count in enrollments_per_day.items():
    print(f"{date}: {count}")

# Example demonstrating the course count:
print(f"\n{student1.name} is enrolled in {student1.course_count()} courses.")
student1.enroll(course1)
student1_enrollments = student1.get_enrollments()
student1_enrollments[0].set_grade(90)  # Set grade for the first enrollment

print(student1.aggregate_average_grade())
# Example demonstrating the (currently broken) grade averaging.
# This needs to be fixed by implementing the _grades attribute appropriately
# and integrating it with the Enrollment objects.
# print(f"\n{student1.name}'s average grade is: {student1.aggregate_average_grade()}")
