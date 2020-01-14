

class PlantSpecies:

    def __init__(self, nutrition, reproduction_cofficient, bloom_period):
        self.nutrition = nutrition
        self.reproduction_cofficient = reproduction_cofficient
        self.bloom_period = bloom_period


def GeneratePlantSpecies():
    return PlantSpecies(1, 2, [1, 180])
