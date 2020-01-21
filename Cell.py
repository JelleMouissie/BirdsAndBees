from PlantSpecies import GeneratePlantSpecies
from random import random

class Cell:
    def __init__(self, diversity = 9):
        self.vegitation = {}
        self.diversity = diversity
        self.IntializeVegitation()

    def IntializeVegitation(self):
        plantSpecies = []
        for x in range(self.diversity):
            plantSpecies += [GeneratePlantSpecies(x)]

        # spread plant species over cell
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

    def GetCellAttractiveness(self, currentDate):
        totalAttractiveness = 0
        for plant in self.vegitation.keys():
            if plant.IsBlooming(currentDate):
                totalAttractiveness += (self.vegitation[plant][1]/plant.GetNutrition()) * plant.GetAttractiveNess()
        return totalAttractiveness


    def GatherFood(self, gatherGroup, currentDate):
        # print("bees:", len(gatherGroup), "Food:", self.getFoodLeft())

        gatherAmountPerBee = 1  #todo add randomization and plant attraction
        gatheredFood = 0
        potentialFood = len(gatherGroup) * gatherAmountPerBee
        for plant in self.vegitation.keys():
            if plant.IsBlooming(currentDate):
                plantNutrition = self.vegitation[plant][1]

                if plantNutrition > potentialFood:
                    self.vegitation[plant][1] -= potentialFood
                    gatheredFood += potentialFood
                    break
                else:
                    gatheredFood += plantNutrition
                    potentialFood -= plantNutrition
                    self.vegitation[plant][1] = 0
        return gatheredFood

    def getFoodLeft(self):
        foodLeft = 0
        for plant in self.vegitation.keys():
            foodLeft += self.vegitation[plant][1]
        return foodLeft

    def incrementYear(self):
        reproductions = []
        totalReproduction = 0
        for plant in self.vegitation.keys():
            foodAmount = plant.GetNutrition() * self.vegitation[plant][0]
            print(foodAmount)
            reproductionCoefficient = ((foodAmount - self.vegitation[plant][1]) / foodAmount) * plant.GetReproduction()
            reproductions += [reproductionCoefficient]
            totalReproduction += reproductionCoefficient

        if totalReproduction > 100:
            plantsPerReproduction = 100 / totalReproduction
        else:
            plantsPerReproduction = 1

        for index, plant in enumerate(self.vegitation.keys()):
            self.vegitation[plant][0] = plantsPerReproduction * reproductions[index]
            self.vegitation[plant][1] = self.vegitation[plant][0] * plant.GetNutrition()

        print(self.vegitation)

    def drought(self):
        pass # decrementeer voedsel want droogte

    def burn(self):
        pass # sererely decrease plants
