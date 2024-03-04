# setting up student class
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    # Method to return student grade
    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_student):
        self.name = name
        self.max_student = max_student
        self.students = []  # Empty list to hold student details

    def add_student(self, student):
        # Test that there is room in the course
        if len(self.students) < self.max_student:
            self.students.append(student)
            return True
        return False

    # Method to get average grade
    def get_average_grade(self):
        total = 0
        for student in self.students:
            total += student.get_grade()
        return total / len(self.students)


# Instate students
s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 65)

# print(Student.get_grade(s1))
# print(Student.get_grade(s2))
# print(Student.get_grade(s3))


# Instate course
course1 = Course("Computer Science", 3)

course1.add_student(s1)
course1.add_student(s2)
course1.add_student(s3)

# Confirm student entry
for student in course1.students:
    print(student.name)

# Get the average grade
print(f"The average grade is {course1.name} is {course1.get_average_grade()}")
