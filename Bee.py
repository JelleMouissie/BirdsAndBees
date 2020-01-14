import random

FOOD_BIAS = 0.75

class Bee:
    def __init__(self, hive_location):
        self.employed = False
        self.hive_location = hive_location
        self.pos_x = hive_location[0]
        self.pos_y = hive_location[1]
        self.food_cargo = 0
        self.age = 0

        self.food_location = []
        self.food_priority = 0
        self.hive_distance = 0

    def update(self, grid):
        self.age += 1
        if self.employed:
            pass
        else:
            self.search(grid)

        return self.still_alive()


    def search(self, grid):
        self.pos_x = random.randint(0,2) - 1
        self.pos_y = random.randint(0,2) - 1

        tile_value = grid[self.pos_x][self.pos_y]
        if tile_value > FOOD_BIAS:
            self.employed = True
            self.food_location[self.pos_x, self.pos_y]
            self.food_priority = tile_value


    def check_block():
        pass
