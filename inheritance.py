class AllStaff:
    def __init__(self, name, age, id, job):
        self.name = name
        self.age = age
        self.id = id
        self.job = job

    def show(self):
        print(f" Employee {self.name} age {self.age} is employee #{self.id} works in {self.job}")


class Management(AllStaff):
    def __init__(self, name, age, id, job, car):
        super().__init__(name, age, id, job)
        self.car = car

    def show(self):
        print(f" Employee {self.name} age {self.age} is employee #{self.id} works in {self.job} has car {self.car}")


class Clerical(AllStaff):
    def __init__(self, name, age, id, job, typing_speed):
        super().__init__(name, age, id, job)
        self.typing_speed = typing_speed

    def show(self):
        print(f" Employee {self.name} age {self.age} is employee #{self.id} works in {self.job} can type at speed "
              f"{self.typing_speed}")


class Factory(AllStaff):
    pass


e1 = Management("Jenny", 22, "ID007", "Mangaging", "Jaguar")
e1.show()
print()
e2 = Clerical("Tim", 17, "ID119", "Secretary", "123")
e2.show()
print()
e3 = Factory("Jake", 16, "ID 125", "Labourer")
e3.show()
print()

