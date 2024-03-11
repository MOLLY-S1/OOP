""" System to store students and class info"""


class Students:
    def __init__(self, name, age, phone_number, form_class, classes, is_male):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.form_class = form_class
        self.classes = classes
        # Gender stated as True False variable
        self.is_male = is_male
        self.enrolled = True
        student_list.append(self)

    def student_details(self):
        if self.is_male:
            gender = "Male"
        else:
            gender = "Female"

        if self.enrolled:
            enrolled = "Yes"
        else:
            enrolled = "No"

        print(f"Name: {self.name}\n"
              f"Age: {self.age}\n"
              f"Phone Number: {self.phone_number}\n"
              f"Form Class: {self.form_class}\n"
              f"Subjects: {self.classes}\n"
              f"Gender: {gender}\n"
              f"Enrolled: {enrolled}\n")
        print("########################\n")


def print_details(self):
    for student in student_list:
        student.student_details()


# Print students aged 16 and over
def sort_student_age():
    find_age = int(input("Enter age to find all students this age and above: "))
    print("########################\n")
    for student in student_list:
        if student.age >= find_age:
            student.student_details()


# Main Routine
student_list = []  # Empty list to store students



# print_details(Students)
sort_student_age()
