import random
import math
import numpy as np

FOOD_BIAS = 0

class Bee:
    def __init__(self):
        self.age = 0
        self.cargo = 0

    #Determine if bee dies, return False. Else if bee lives, increase age and return True
    def update_age(self, hive, population, currentDate, predators):
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


    #Update scout for 1 simulation step. If employed, do nothing (Handled in Hive.py)
    def update(self, grid):
        if self.food_value > FOOD_BIAS:
            return True
        return self.search(grid)


    def search(self, grid):
        xlim, ylim  = grid.Getlimits()
        self.pos_x = random.randint(0,xlim) - 1
        self.pos_y = random.randint(0,ylim) - 1

        tile_value = grid.Get(self.pos_x,self.pos_y).GetCellAttractiveness()
        if tile_value > FOOD_BIAS:                        #TODO: Determine when food source is good enough.  gather_food           !!!
            self.food_location += [self.pos_x, self.pos_y]
            self.food_value = tile_value
            self.hive_distance = math.sqrt(math.pow((self.pos_x - self.hive_location[0]), 2) + math.pow((self.pos_y - self.hive_location[1]), 2))

            return True
        return False
