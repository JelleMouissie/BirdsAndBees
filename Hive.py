FORAGERS_TO_POPULATION = 1/3
SCOUTS_TO_EMPLOYEES = 1/10

#Maintain population and food levels, spawn new bees as needed
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

        num_foragers = int(FORAGERS_TO_POPULATION * population)
        self.scouts = [Scout([pos_x,pos_y]) for _ in range(int(SCOUTS_TO_EMPLOYEES * num_foragers))]
        self.employees = [Employee([pos_x,pos_y]) for _ in range(num_foragers - len(self.scouts))]
        self.employed = []


    # Determine food level based on amount of pollen, nectar and growth rate.
    # Also adjust amount of food left aftwards based on consumption rate of food.
    def update_food_level(self):
        pass

    #Update food levels and bee populations
    def update(self):
        self.update_food_level()
        self.population = self.population * food_level

        num_foragers = int(FORAGERS_TO_POPULATION * self.population)
        num_scouts = int(foragers * SCOUTS_TO_EMPLOYEES)
        num_employees = num_foragers - num_scouts

        new_scouts = num_scouts - len(self.scouts)
        new_employees = num_employees - len(self.employees)

        for _ in range(new_scouts):
            self.scouts.append(Scout([self.pos_x, self.pos_y]))

        for _ in range(new_employees):
            self.scouts.append(Employee([self.pos_x, self.pos_y]))
