class Cat:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def eat(self):
        self.weight += 1

    def getdetails(self):
        return f"{self.name}, {self.weight}"

    def walk(self):
        if self.weight != 1:
            self.weight -= 1