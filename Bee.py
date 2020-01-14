import random
import math

FOOD_BIAS = 0.75

class Bee:
    def __init__(self):
        self.age = 0
        self.cargo = 0

    #Determine if bee dies, return False. Else if bee lives, increase age and return True
    def update_age(self):
        if self.age > 8:      #TODO: Implement actual death condition based on probability                             !!!
            return False
        else:
            self.age += 1
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
        self.pos_x = random.randint(0,2) - 1
        self.pos_y = random.randint(0,2) - 1

        tile_value = grid[self.pos_x][self.pos_y].value   #TODO: Figure out how to check ground's tile_value                    !!!
        if tile_value > FOOD_BIAS:                        #TODO: Determine when food source is good enough.             !!!
            self.food_location[self.pos_x, self.pos_y]
            self.food_value = tile_value
            self.hive_distance = math.sqrt(math.pow((self.pos_x - self.hive_location[0]), 2) + math.pow((self.pos_y - self.hive_location[1]))

            return True
        return False
