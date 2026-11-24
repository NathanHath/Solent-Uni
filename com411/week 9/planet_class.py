class Planet:

    def __init__(self, name):
        self.name = name
        self.humans = {}
        self.robots = {}

    def add_human(self, Human_name, Human_age):
        self.humans.add((Human_name, Human_age))

    def remove_human(self):
        Human_name = input("Enter Human name: ")
        Human_age = int(input("Enter Human age: "))
        target = (Human_name, Human_age)

        if target in self.humans:
            self.humans.remove(target)
            return "success"
        else:
            return "Human not found"

    def add_robot(self, Robot_name, Robot_age):
        self.robots.append((Robot_name, Robot_age))

    def remove_robot(self):
        Robot_name = input("Enter Robot name: ")
        Robot_age = int(input("Enter Robot age: "))
        target = (Robot_name, Robot_age)
        if target in self.robots:
            self.robots.remove(target)
            return "success"
        else:
            return "Robot not found"

    def __str__(self):
        return f"wlecome to {self.name} with {self.humans} humans and {self.robots} robots"


P1 = Planet("Mars")
P1.add_human("Nathan", 18)
P1.add_robot("R2D2", 5)
print(P1)