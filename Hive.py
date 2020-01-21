from Bee import Scout, Bee
import numpy as np

"""
Project Computational Science
Sander van Oostveen, Jelle Mouissie and Joos Akkerman

This file defines the class Hive, which contains the functions for population
development.
"""

FORAGERS_TO_POPULATION = 1/3
SCOUTS_TO_FORAGERS = 1/10
food_per_bee = 0.25

PRIORITY_BIAS = 2     #TODO: Decide Bias in determining priority of found food source.

#Maintain population and food levels, spawn new bees as needed
class Hive:
    def __init__(self, pos_x, pos_y, start_population, start_food, growth_rate, consumption_rate):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.population =  start_population
        self.populationhistory = []
        self.deathhistory = []
        self.growth_rate = growth_rate
        self.consumption_rate = consumption_rate
        self.food_level = start_food
        self.total_death = 0
        self.total_born = start_population
        self.growthscale = 1

        num_foragers = int(FORAGERS_TO_POPULATION * self.population)
        self.scouts = [Scout([pos_x,pos_y]) for _ in range(int(SCOUTS_TO_FORAGERS * num_foragers))]
        self.employees = [Bee() for _ in range(num_foragers - len(self.scouts))]
        self.gather_group_id = 0


    #Do stuff with food?
    def update_food_level(self):
        # food_per_bee = 0.2
        needed_food = food_per_bee * self.population
        print("voor vreten", self.food_level, "Needed food:", needed_food)
        if (needed_food > self.food_level):
            needed_food -= self.food_level
            self.food_level = 0
            self.starvation(needed_food / food_per_bee)
            print(f'percentageDeath: {((needed_food / food_per_bee)/self.population)/2}')
        else :
            self.food_level -= needed_food
        print("na vreten", self.food_level)


    def starvation(self, shortage):
        pass
        # print(shortage)
        # percentageDeath = (shortage / self.population) / 2
        # self.population -= self.population * percentageDeath
        # self.scouts = self.scouts[0 : len(self.scouts) - int(len(self.scouts) * percentageDeath)]
        # self.employees = self.employees[0 : len(self.employees) - int(len(self.employees) * percentageDeath)]


    #Increase population and determine new amount of foragers and scouts.
    def update_population(self, currentDate):
        maxpop = 2*10**5
        startpop = 10000
        # startdeath = 0.014*startpop
        # maxdeath = 170000
        k = 25*10**-8
        # l = 1.65*k

        # Use logistic population distribution to simulate 'natural' growth rate, given
        # time in season. Scale natural growth rate by food ratio.
        tot_pop = startpop*(maxpop/(startpop+(maxpop-startpop)*np.exp(-maxpop*k*currentDate[0])))
        next_tot_pop = startpop*(maxpop/(startpop+(maxpop-startpop)*np.exp(-maxpop*k*(currentDate[0]+1))))

        # print(tot_pop)
        # print(next_tot_pop)
        # tot_death = startdeath*(maxdeath/(startdeath+(maxdeath-startdeath)*np.exp(-maxdeath*l*(currentDate[0]+25))))
        # print(tot_pop)
        # print(tot_death)

        growth = 1 + self.growthscale*(next_tot_pop - tot_pop)/next_tot_pop
        # print(f'growth: {growth}')
        self.population = int(self.population*growth) #TODO: implement actual growth based on food supplies                          !!!!

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
    def gather_food(self, scouts, grid):
        priorities = []
        totalpriority = 1
        for scout in scouts:
            priority = (PRIORITY_BIAS * scout.food_value / (scout.hive_distance + 1))/10 # Amount of employee bees assigned to food source
            priorities += [priority]
            totalpriority += priority

        beesPerPrio = len(self.employees) / totalpriority
        start_slice = 0
        # print(priorities)
        # print(beesPerPrio)
        # print(len(self.employees))

        for index, scout in enumerate(scouts):
            end_slice = start_slice + int(priorities[index] * beesPerPrio)
            # print(end_slice)/
            gather_group = self.employees[start_slice : end_slice]
            self.food_level += grid.Get(scout.food_location[0], scout.food_location[1]).GatherFood(gather_group)
            scout.food_value = grid.Get(scout.food_location[0], scout.food_location[1]).GetCellAttractiveness()

            start_slice = end_slice

    #Kill Bees >:)
    def update_bee_age(self, population, currentDate):
        alive_scouts = [scout for scout in self.scouts if scout.update_age(self, population, currentDate)]
        alive_employees = [employee for employee in self.employees if employee.update_age(self, population, currentDate)]
        num_dead = len(self.scouts) - len(alive_scouts) + len(self.employees) - len(alive_employees)

        # print(self.population)
        self.population -= num_dead
        # print(self.population)
        self.scouts = alive_scouts
        self.employees = alive_employees

    #First update scouts. If scout has a source, gather food with employee bees. Finally update age of all bees.
    def update_bees(self, grid, population, currentDate):
        updated_scouts = []

        for scout in self.scouts:
            if scout.update(grid):
                updated_scouts += [scout]

        self.gather_food(updated_scouts, grid)
        self.update_bee_age(population, currentDate)
        self.gather_group_id = 0


    def update_growthscale(self):
        if self.population != 0:
            f = self.food_level/(food_per_bee*self.population)
            return min([f, 1])
        else:
            return 1


    #Update food levels, bee populations and perform bee actions
    def update(self, grid, currentDate):
        self.update_food_level()
        self.update_population(currentDate)
        self.update_bees(grid, self.population, currentDate)
        self.populationhistory.append(self.population)
        self.deathhistory.append(self.total_death)
        self.growthscale = self.update_growthscale()


    def incrementYear(self):
        pass

    def GetStatus(self):
        return [self.population, len(self.scouts), len(self.employees)]

    def Getpophistory(self):
        return self.populationhistory

    def Getdeathhistory(self):
        return self.deathhistory
