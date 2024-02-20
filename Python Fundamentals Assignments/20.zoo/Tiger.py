import Animal

class Tiger (Animal):
    def __init__(self, name, age=0, health=0,happiness=0):
        super().__init__(name,age,health,happiness)

    def feed(self):
        self.health_level += 12
        self.happiness += 12