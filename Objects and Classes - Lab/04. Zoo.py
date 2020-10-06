class Zoo :
    __animals = 0

    def __init__(self, name_zoo):
        self.name_zoo = name_zoo
        self.mammal = []
        self.fish = []
        self.bird = []


    def add_animal(self, species, name):
        if species == 'mammal':
            zoo.mammal.append(name)
        elif species == 'fish':
            zoo.fish.append(name)
        elif species == 'bird':
            zoo.bird.append(name)
        zoo.__animals += 1


    def get_info(self, species) :
        if species == 'mammal':
            species = 'Mammals'
            list = ', '.join([animal for animal in zoo.mammal])

        elif species == 'fish':
            species = 'Fishes'
            list = ', '.join([animal for animal in zoo.fish])

        elif species == 'bird':
            species = 'Birds'
            list = ', '.join([animal for animal in zoo.bird])

        print(f"{species} in {name_zoo}: {list}")
        print(f"Total animals: {zoo.__animals}")

name_zoo = input()

zoo = Zoo(name_zoo)

n = int(input())

for _ in range(n):
    animal = input()
    species, name = animal.split(' ')
    zoo.add_animal(species , name)

species = input()

zoo.get_info(species)
