from PlantSpecies import GeneratePlantSpecies
from random import random

class Cell:

    def __init__(self, diversity, prop_cell, plantSpecies):
        self.vegitation = {}
        self.diversity = diversity
        self.IntializeVegitation(prop_cell, plantSpecies)


    def IntializeVegitation(self, prop_cell, plantSpecies):

        # DIT HOEFT NIET VOOR IEDERE CELL GEDAAN TE WORDEN TOCH?
        # plantSpecies = []
        # for x in range(self.diversity):
        #     plantSpecies += [GeneratePlantSpecies(x)]
        for i in prop_cell.keys():
            plant_prop = prop_cell[i]
            self.vegitation[plantSpecies[i]] = [plant_prop[0], plant_prop[1]]

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
            foodAmount = plant.GetNutrition() * self.vegitation[plant][0] + 1
            reproductionCoefficient = ((foodAmount - self.vegitation[plant][1]) / foodAmount + 0.3) * plant.GetReproduction() * self.vegitation[plant][0]
            reproductions += [reproductionCoefficient]
            totalReproduction += reproductionCoefficient


        if totalReproduction > 100:
            plantsPerReproduction = 100 / totalReproduction
        else:
            plantsPerReproduction = 1

        for index, plant in enumerate(self.vegitation.keys()):
            self.vegitation[plant][0] = int(plantsPerReproduction * reproductions[index])
            self.vegitation[plant][1] = int(self.vegitation[plant][0] * plant.GetNutrition())


    def drought(self):
        pass # decrementeer voedsel want droogte

    def burn(self):
        pass # sererely decrease plants
