""" System to store students and class info"""

student_list = []  # Empty list to store students


class Teachers:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        teacher_list.append(self)

    def display_teacher(self):
        print("\n################")
        print("Teacher: ", self.name)
        print("Subject: ", self.subject)

def print_teacher():
    for teacher in teacher_list:
        teacher.display_teacher()


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


def generate_students():
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
            return student
    if name not in student_list:
        print(f"\n There are no students named '{name}' in the system.\n")


def add_student():
    name = input("Enter the student name (first then last): ").title()
    age = int_check("Enter the student age: ")
    phone = input("Enter student phone number: ")
    form_class = input("Enter the student form class (eg 'Baker'): ").upper()
    classes = enter_classes()
    gender = get_gender()
    Students(name, age, phone, form_class, classes, gender)
    print("\n{name} has been added to the student database\n")


def int_check(text):
    valid = False
    while not valid:
        try:
            number_to_check = int(input(text))
            if isinstance(number_to_check, int):
                valid = True
                return number_to_check
        except ValueError:
            print("Entry must be an integer")


def enter_classes():
    subject = ""
    subject_list = []
    while subject != "X":
        subject = input("Enter the 3 digit class code, or 'X' to stop: ").upper()
        if subject == "X":
            break
        else:
            subject_list.append(subject)
    return ','.join(subject_list)


def get_gender():
    valid_gender = False
    while not valid_gender:
        gender = input("Enter gender as 'M' or 'F': ").upper()
        if gender == 'M':
            return True
        elif gender == 'F':
            return False
        else:
            print(f"Gender can only be 'M' or 'F' not '{gender}'\n")


def delete_student():
    student_to_delete = find_student("Enter student name to delete: ")
    if student_to_delete:
        confirm_delete = input(f"\nPress <enter> to confirm that you want to"
                               f"delete\n\t{student_to_delete.name} from the"
                               f"student database OR any other key"
                               f" and <enter> to return to the main menu\n")
        if not confirm_delete:
            student_list.remove(student_to_delete)
            print(f"{student_to_delete.name} has been removed from the student database\n")


# Main Routine
generate_students()
teacher_list = []

Teachers("Baker", "GRA")
Teachers("Barker", "MAT")
Teachers("Graham", "BIO")
Teachers("Morgan", "DTC")
Teachers("Bell", "PHY")
Teachers("McNoil", "ENG")
# MENU LOOP
choice = ""
while choice != "Q":
    choice = input(f"##### MAIN MENU #####\n"
                   f"Please enter a number:\n"
                   f"1) Count students taking a subject\n"
                   f"2) Print a full list of students\n"
                   f"3) Find a student\n"
                   f"4) Find all students of a specific age\n"
                   f"5) Delete student"
                   f"6) Add student"
                   f"7) Add full teacher list"
                   f"Press 'Q' to quit\n").upper()
    if choice == "1":
        print(count_students())
    elif choice == "2":
        print_details(Students)
    elif choice == "3":
        find_student("Enter the name of the student you are looking for: ")
    elif choice == "4":
        sort_student_age()
    elif choice == '5':
        delete_student()
    elif choice == "6":
        add_student()
    elif choice == "7":
        print_teacher()


print("GOODBYE")
