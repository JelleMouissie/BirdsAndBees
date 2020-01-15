

class PlantSpecies:

    def __init__(self, nutrition, reproduction_coefficient, attractiveness, bloom_period):
        self.nutrition = nutrition
        self.reproduction_coefficient = reproduction_coefficient
        self.bloom_period = bloom_period


def GeneratePlantSpecies():
    return PlantSpecies(1, 2, 1, [1, 180])
