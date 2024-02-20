from Animal import Animal

class Bear (Animal):
    def __init__(self, name, age=0, health=0,happiness=0,color="Brown"):
        self.color = color
        super().__init__(name,age,health,happiness) 
    
    def display_info(self):
        print(f"{self.name} is {self.age} years old and has a health level of {self.health_level} and a happiness level of {self.happiness} and has a {self.color} color")

    def sleep(self):
        print(f"{self.name} ia sleeping")
        