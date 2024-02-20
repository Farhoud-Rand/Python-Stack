class Animal:
    def __init__(self, name,age=0,health=0,happiness=0):
        self.name = name
        self.age = age
        self.health_level = health
        self.happiness = happiness

    # Display informathion method that shows the animal's name, health, and happiness
    def display_info(self):
        print(f"{self.name} is {self.age} years old and has a health level of {self.health_level} and a happiness level of {self.happiness}")

    # Feed method that increases health and happiness by 10
    def feed(self):
        self.health_level += 10
        self.happiness += 10