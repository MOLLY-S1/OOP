# Class for buses
class Bus:
    bus_list = []

    def __init__(self, number, route, driver):
        self.number = number
        self.route = route
        self.driver = driver
        Bus.bus_list.append(self)

    def print_details(self):
        for bus in Bus.bus_list:
            if bus == self:
                print(f"Bus driver {self.driver} drives bus number {self.number} on route {self.route}\n")


bus1 = Bus(2343, 70, "Tim")
bus2 = Bus(1892, 45, "Mary")
bus3 = Bus(2349, 125, "Todd")

for bus in range(len(Bus.bus_list)):
    print(Bus.print_details(Bus.bus_list[bus]))
