from Bee import Scout, Bee

FORAGERS_TO_POPULATION = 1/3
SCOUTS_TO_FORAGERS = 1/10

PRIORITY_BIAS = 2     #TODO: Decide Bias in determining priority of found food source.

#Maintain population and food levels, spawn new bees as needed
class Hive:
    def __init__(self, pos_x, pos_y, start_population, start_food, growth_rate, consumption_rate):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.population =  start_population
        self.growth_rate = growth_rate
        self.consumption_rate = consumption_rate
        self.food_level = start_food

        num_foragers = int(FORAGERS_TO_POPULATION * self.population)
        self.scouts = [Scout([pos_x,pos_y]) for _ in range(int(SCOUTS_TO_FORAGERS * num_foragers))]
        self.employees = [Bee() for _ in range(num_foragers - len(self.scouts))]
        self.gather_group_id = 0


    #Do stuff with food?
    def update_food_level(self):
        pass       #TODO: Implement this                                                                                                   !!!!


    #Increase population and determine new amount of foragers and scouts.
    def update_population(self, currentDate):
        growth = (1+0.03*(-(currentDate[0]/100 - 1)**2+1)+0.8)**(1/7)
        print(growth)
        self.population = int(self.population * growth) #TODO: implement actual growth based on food supplies                          !!!!

        num_foragers = int(FORAGERS_TO_POPULATION * self.population)
        num_scouts = int(num_foragers * SCOUTS_TO_FORAGERS)
        num_employees = num_foragers - num_scouts

        new_scouts = num_scouts - len(self.scouts)
        new_employes = num_employees - len(self.employees)

        for _ in range(new_scouts):
            self.scouts.append(Scout([self.pos_x, self.pos_y]))

        for _ in range(new_employes):
            self.employees.append(Bee())


    #Gather unemployed bees based on priority, and collectivly gather food
    def gather_food(self, scout, grid):
        priority = PRIORITY_BIAS * scout.food_value / scout.hive_distance    # Amount of employee bees assigned to food source
        start_slice = self.gather_group_id
        end_slice = int(start_slice + priority)
        self.gather_group_id = end_slice

        gather_group = self.employees[start_slice : end_slice]
        self.food_level += grid.Get(scout.food_location[0], scout.food_location[1]).GatherFood(gather_group)
        scout.food_value = grid.Get(scout.food_location[0], scout.food_location[1]).GetCellAttractiveness()

    #Kill Bees >:)
    def update_bee_age(self):
        alive_scouts = [scout for scout in self.scouts if scout.update_age()]
        alive_employees = [employee for employee in self.employees if employee.update_age()]
        num_dead = len(self.scouts) - len(alive_scouts) + len(self.employees) - len(alive_employees)

        # print(self.population)
        self.population -= num_dead
        # print(self.population)
        self.scouts = alive_scouts
        self.employees = alive_employees

    #First update scouts. If scout has a source, gather food with employee bees. Finally update age of all bees.
    def update_bees(self, grid):
        updated_scouts = []
        for scout in self.scouts:
            if scout.update(grid):
                self.gather_food(scout, grid)
        self.update_bee_age()
        self.gather_group_id = 0


    #Update food levels, bee populations and perform bee actions
    def update(self, grid, currentDate):
        self.update_food_level()
        self.update_population(currentDate)
        self.update_bees(grid)

    def incrementYear(self):
        pass

    def GetStatus(self):
        return [self.population, len(self.scouts), len(self.employees)]
