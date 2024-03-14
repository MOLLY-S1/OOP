""" System to store students and class info"""

student_list = []  # Empty list to store students


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


import csv

with open('random_students.csv', newline='') as csvfile:
    filereader = csv.reader(csvfile, delimiter='|')
    for line in filereader:
        if line[5] == "True":
            is_male = True
        else:
            is_male = False
        Students(line[0], int(line[1]), line[2], line[3], line[4], is_male)


def count_students():
    count = 0
    subject = input("What class are you looking for: ").upper()
    for student in student_list:
        if subject in student.classes:
            count += 1
            if count > 0:
                return f"\nThere are {count} students in {subject}"
            else:
                return f"\nThere are no students in {subject}"


def find_student(text):
    name = input(text).title()
    for student in student_list:
        if student.name == name:
            student.display_info()


# Main Routine

choice = ""
while choice != "Q":
    choice = input(f"##### MAIN MENU #####\n"
                   f"Please enter a number:\n"
                   f"1) Count students taking a subject\n"
                   f"2) Print a full list of students\n"
                   f"3) Find a student\n"
                   f"4) Find all students of a specific age\n"
                   f"Press 'Q' to quit\n").upper()
    if choice == "1":
        print(count_students())
    elif choice == "2":
        print_details(Students)
    elif choice == "3":
        find_student("Enter the name of the student you are looking for: ")
    elif choice == "4":
        sort_student_age()


print("GOODBYE")