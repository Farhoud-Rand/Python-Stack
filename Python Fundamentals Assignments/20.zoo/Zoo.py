class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    
    def add_animal(self, animal):
        self.animals.append( animal )
    # def add_bear(self, name,age,health,happiness,color):
    #     self.animals.append( Lion(name,age,health,happiness,color) )

    # def add_lion(self, name,age,health,happiness):
    #     self.animals.append( Lion(name,age,health,happiness) )
    
    # def add_tiger(self, name,age,health,happiness):
    #     self.animals.append( Tiger(name,age,health,happiness) )
    
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()