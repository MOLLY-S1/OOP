# setting up student class
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    # Method to return student grade
    def get_grade(self):
        return self.grade
