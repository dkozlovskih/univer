class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor):
        self.new_floor = new_floor
        for i in range(new_floor):
            if new_floor > self.number_of_floors:
                continue
            print(i+1)

        if self.new_floor > self.number_of_floors or self.new_floor < 1:
            print("Такого этажа не существует")


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(4)
h2.go_to(10)