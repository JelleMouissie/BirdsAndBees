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
            self.vegitation[plantSpecies[i]] = [amount, amount * plantSpecies[i].GetNutrition()]


    def GetVegitation(self):
        return self.vegitation

    def GetCellAttractiveness(self):
        totalAttractiveness = 0
        for plant in self.vegitation.keys():
            totalAttractiveness += (self.vegitation[plant][1]/plant.GetNutrition()) * plant.GetAttractiveNess()
        return totalAttractiveness


    def GatherFood(self, gatherGroup):
        print(len(gatherGroup))
        print(self.vegitation)

        gatherAmountPerBee = 1  #todo add randomization and plant attraction
        gatheredFood = 0
        potentialFood = len(gatherGroup) * gatherAmountPerBee
        for plant in self.vegitation.keys():
            plantNutrition = self.vegitation[plant][1]

            if plantNutrition > potentialFood:
                self.vegitation[plant][1] -= potentialFood
                gatheredFood += potentialFood
                break
            else:
                gatheredFood += plantNutrition
                potentialFood -= plantNutrition
                self.vegitation[plant][1] = 0
        print(self.vegitation)
        print()
        return gatheredFood
