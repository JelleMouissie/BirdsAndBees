from PlantSpecies import generate_plant_species
from random import random

"""
Project Computational Science
Sander van Oostveen, Jelle Mouissie and Joos Akkerman

This file defines the class Cell,
which contains the behaviour of a cell in the grid.
"""

class Cell:

    def __init__(self, diversity, prop_cell, plant_species):
        self.vegitation = {}
        self.diversity = diversity
        self.intialize_vegitation(prop_cell, plant_species)


    def intialize_vegitation(self, prop_cell, plant_species):
        """
        Initialize the vegitation in the cell based on given properties
        and a list of plant_species
        """
        for i in prop_cell.keys():
            plant_prop = prop_cell[i]
            self.vegitation[plant_species[i]] = [plant_prop[0], plant_prop[1]]


    def get_cell_attractiveness(self, current_date):
        """
        Get the attractiveness of the cell based on the food
        and the attractiveness of the plants in the cell
        """
        total_attractiveness = 0
        for plant in self.vegitation.keys():
            if plant.is_blooming(current_date):
                total_attractiveness += (self.vegitation[plant][1]/plant.get_nutrition()) * plant.get_attractiveness()
        return total_attractiveness


    def gather_food(self, gather_group, current_date):
        """
        Have a group of bees gather food at this cell at the current date.
        You can only gather food from a plant if the plant is blooming.
        """
        gathered_food = 0
        potential_food = len(gather_group)
        for plant in self.vegitation.keys():
            if plant.is_blooming(current_date):
                plant_nutrition = self.vegitation[plant][1]

                if plant_nutrition > potential_food:
                    self.vegitation[plant][1] -= potential_food
                    gathered_food += potential_food
                    break
                else:
                    gathered_food += plant_nutrition
                    potential_food -= plant_nutrition
                    self.vegitation[plant][1] = 0
        return gathered_food


    def get_food_left(self):
        """
        return the amount of food leftover in the cell.
        """
        food_left = 0
        for plant in self.vegitation.keys():
            food_left += self.vegitation[plant][1]
        return food_left


    def increment_year(self):
        """
        Reset the vegitation at the end of the winter based on the percentage of
        the available food that was eaten.
        """
        reproductions = []
        total_reproduction = 0
        for plant in self.vegitation.keys():
            food_amount = plant.get_nutrition() * self.vegitation[plant][0] + 1
            reproduction_coefficient = ((food_amount - self.vegitation[plant][1]) / food_amount + 0.3) * plant.get_reproduction() * self.vegitation[plant][0]
            reproductions += [reproduction_coefficient]
            total_reproduction += reproduction_coefficient


        if total_reproduction > 100:
            plants_per_reproduction = 100 / total_reproduction
        else:
            plants_per_reproduction = 1

        for index, plant in enumerate(self.vegitation.keys()):
            self.vegitation[plant][0] = int(plants_per_reproduction * reproductions[index])
            self.vegitation[plant][1] = int(self.vegitation[plant][0] * plant.get_nutrition())


    def is_mono_culture(self):
        """
        Returns true if the cell only contains one plant
        """
        onePlant = False
        for plant in self.vegitation.keys():
            if self.vegitation[plant][0] != 0 and not onePlant:
                onePlant = True
            elif self.vegitation[plant][0] != 0 and onePlant:
                return True
        return False
