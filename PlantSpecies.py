

class PlantSpecies:

    def __init__(self, nutrition, reproduction_coefficient, attractiveness, bloom_period):
        self.nutrition = nutrition
        self.reproduction_coefficient = reproduction_coefficient
        self.bloom_period = bloom_period
        self.attractiveness = attractiveness

    def GetNutrition(self):
        return self.nutrition

    def GetAttractiveNess(self):
        return self.attractiveness

    def GetReproduction(self):
        return self.reproduction_coefficient


def GeneratePlantSpecies():
    return PlantSpecies(10000, 2, 1, [1, 180])
