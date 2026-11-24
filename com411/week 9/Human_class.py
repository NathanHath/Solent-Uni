class Human:
    MAX_ENERGY = 100

    def __init__(self, name):
        self.energy  = Human.MAX_ENERGY
        self.name = name
        self.age = 0

    def __str__(self):
        return f"I am {self.name}"