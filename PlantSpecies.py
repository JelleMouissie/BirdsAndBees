
"""
Project Computational Science
Sander van Oostveen, Jelle Mouissie and Joos Akkerman

This file defines the class PlantSpecies, Which contins the values for different
plants, it's behaviour and a mehtod to generate the objects
"""

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

class plant_species:

    def __init__(self, nutrition, reproduction_coefficient, attractiveness, bloom_period):
        self.nutrition = nutrition
        self.reproduction_coefficient = reproduction_coefficient
        self.bloom_period = bloom_period
        self.attractiveness = attractiveness


    def get_nutrition(self):
        """
        return the nutritional value for a plant.
        """
        return self.nutrition


    def get_attractiveness(self):
        """
        return the attractiveness of a plant.
        """
        return self.attractiveness


    def get_reproduction(self):
        """
        Return the reproduction_coefficient for a plant.
        """
        return self.reproduction_coefficient


    def is_blooming(self, current_date):
        """
        Return true if the plant is blooming based on a given date.
        """
        return current_date[0] >= self.bloom_period[0] and current_date[0] <= self.bloom_period[1]


def generate_plant_species(species):
    """
    Generate a given species of plant.
    """
    plant = ALL_PLANTS[species]
    return plant_species(plant[0], plant[1], plant[2], plant[3])
