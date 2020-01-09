FORAGERS_TO_POPULATION = 1/3
SCOUTS_TO_EMPLOYEES = 1/10

class Hive:
    def __init__(self, pos_x, pos_y, start_population, start_pollen, start_nectar, growth_rate, consumption_rate):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.population =  start_population
        self.growth_rate = growth_rate
        self.consumption_rate = consumption_rate
        self.pollen = start_pollen
        self.nectar = start_nectar
        self.food_level = 1.1

        foragers = int(FORAGERS_TO_POPULATION * population)
        self.scouts = [Scout([pos_x,pos_y]) for _ in range(int(SCOUTS_TO_EMPLOYEES * foragers))]
        self.employees = [Employee([pos_x,pos_y]) for _ in range(foragers - len(self.scouts))]


    # Determine food level based on amount of pollen, nectar and growth rate. 
    # Also adjust amount of food left aftwards based on consumption rate of food.
    def update_food_level():
        pass


    def update():
        update_food_level()
        self.population = self.population * food_level
