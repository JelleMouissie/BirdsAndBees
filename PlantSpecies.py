

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

    def IsBlooming(self, currentDate):
        return currentDate[0] >= self.bloom_period[0] and currentDate[0] <= self.bloom_period[1]


def GeneratePlantSpecies(species):
    all_plants = {0: [2500, 2, 1, [1, 40]],
                    1: [2500, 2, 1, [20, 60]],
                    2: [2500, 2, 1, [40, 80]],
                    3: [2500, 2, 1, [60, 100]],
                    4: [2500, 2, 1, [80, 120]],
                    5: [2500, 2, 1, [100, 140]],
                    6: [2500, 2, 1, [120, 160]],
                    7: [2500, 2, 1, [140, 180]],
                    8: [2500, 2, 1, [160, 200]],
                    9: [2500, 2, 1, [180, 200]]}
    plant = all_plants[species]
    return PlantSpecies(plant[0], plant[1], plant[2], plant[3])
