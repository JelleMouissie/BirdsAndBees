import random
import math
import numpy as np

"""
Project Computational Science
Sander van Oostveen, Jelle Mouissie and Joos Akkerman

This file defines the class Bee, which contains functions for bee behaviour.
"""

class Bee:
    def __init__(self):
        self.age = 0
        self.cargo = 0


    def update_age(self, hive, population, current_date, predators):
        """
        Determine if bee dies, return False. Else if bee lives, increase age and return True
        """
        self.age += 1
        death_chance = 0.0014 + predators

        if death_chance*self.age > np.random.rand():
            hive.total_death += 1
            return False
        else:
            return True

class Scout(Bee):

    def __init__(self, hive_location):
        super().__init__()
        self.hive_location = hive_location
        self.pos_x = hive_location[0]
        self.pos_y = hive_location[1]

        self.food_location = []
        self.food_value = 0
        self.hive_distance = 0

    def update(self, grid, current_date):
        """
        Update scout for 1 simulation step. If employed, do nothing (Handled in Hive.py)
        """
        if self.food_value > 0:
            return True
        return self.search(grid, current_date)


    def pos_in_grid(self, pos, limit):
        """
        Update the location of the scout
        """
        if pos < 0:
            return 0
        elif pos > (limit - 1):
            return limit -1
        return pos


    def search(self, grid, current_date):
        """
        Move in the grid and set the current location,
        the value of the food at the location and the distance to the hive.
        """
        xlim, ylim  = grid.get_limits()

        x_cof = random.randint(-5,5)
        y_cof = random.randint(-5,5)

        new_posX = self.pos_x + x_cof
        new_posY = self.pos_y + y_cof

        self.pos_x = self.pos_in_grid(new_posX, xlim)
        self.pos_y = self.pos_in_grid(new_posY, ylim)

        tile_value = grid.get(self.pos_x,self.pos_y).get_cell_attractiveness(current_date)
        if tile_value > 0:
            self.food_location += [self.pos_x, self.pos_y]
            self.food_value = tile_value
            self.hive_distance = math.sqrt(math.pow((self.pos_x - self.hive_location[0]), 2) + math.pow((self.pos_y - self.hive_location[1]), 2))

            return True
        return False
