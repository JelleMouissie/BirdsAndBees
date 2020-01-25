
# DEZE IN EEN APART TXT FILE ZETTEN??
NUTRITION_PER_PLANT = 500
ALL_PLANTS = {0: [NUTRITION_PER_PLANT, 2, 1, [1, 60]],
                1: [NUTRITION_PER_PLANT, 2, 1, [10, 70]],
                2: [NUTRITION_PER_PLANT, 2, 1, [30, 100]],
                3: [NUTRITION_PER_PLANT, 2, 1, [50, 110]],
                4: [NUTRITION_PER_PLANT, 2, 1, [70, 120]],
                5: [NUTRITION_PER_PLANT, 2, 1, [90, 140]],
                6: [NUTRITION_PER_PLANT, 2, 1, [110, 160]],
                7: [NUTRITION_PER_PLANT, 2, 1, [130, 170]],
                8: [NUTRITION_PER_PLANT, 2, 1, [160, 190]],
                9: [NUTRITION_PER_PLANT, 2, 1, [180, 200]]}

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
    plant = ALL_PLANTS[species]
    return PlantSpecies(plant[0], plant[1], plant[2], plant[3])
