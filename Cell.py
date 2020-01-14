from PlantSpecies import GeneratePlantSpecies
from random import random

class Cell:
    def __init__(self, diversity = 1):
        self.vegitation = {}
        self.diversity = diversity
        self.IntializeVegitation()

    def IntializeVegitation(self):
        plantSpecies = []
        for x in range(self.diversity):
            plantSpecies += [GeneratePlantSpecies()]

        randomindexes = []
        for y in range(self.diversity-1):
            randomindexes += [int(random()*100)]
        randomindexes.sort()
        randomindexes += [100]
        currentindex = 0
        for i in range(len(randomindexes)):
            amount = randomindexes[i] - currentindex
            currentindex = randomindexes[i]
            self.vegitation[plantSpecies[i]] = amount

        print(self.vegitation)

    def GetVegitation(self):
        return self.vegitation
#
# cell = Cell(3)
# cell.IntializeVegitation()
