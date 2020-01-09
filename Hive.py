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

    self.foragers = int(FORAGERS_TO_POPULATION * population)
    self.scouts = int(SCOUTS_TO_EMPLOYEES * self.foragers)
    self.employees = self.foragers - self.scouts
