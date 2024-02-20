import Zoo
import Bear
import Lion
import Tiger

zoo1 = Zoo("John's Zoo")

zoo1.add_animal(Bear("Bascal",3,5,10))
zoo1.add_animal(Bear("Mero",1,10,10,"White"))
zoo1.add_animal(Lion("Nala",1,0,0))
zoo1.add_animal(Lion("Simba",5,30,30))
zoo1.add_animal(Tiger("Rajah",2,60,60))
zoo1.add_animal(Tiger("Shere Khan",1,12,12))
# zoo1.add_lion("Simba")
# zoo1.add_tiger("Rajah")
# zoo1.add_tiger("Shere Khan")
zoo1.print_all_info()

# Feed all animals
for animal in zoo1.animals:
    animal.feed()
zoo1.print_all_info()
