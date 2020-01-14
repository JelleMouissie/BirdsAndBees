import matplotlib.pyplot as plt
import sys
import matplotlib
from Model import Model
from GUI import GUI
from Grid import Grid


class Environment(Model):
    def __init__(self):
        Model.__init__(self)
        self.make_param('Wepsen', 0)
        self.make_param('x', 10)
        self.make_param('y', 10)
        self.make_param('diversity', 2)

    def reset(self):
        self.currentDate = [0, 0]
        self.grid = Grid(self.x, self.y)
        self.grid.initializeCells(self.diversity)




    def draw(self):
        pass
        # plt.cla()

    def step(self):
        self.incrementDate()

        pass

    def incrementDate(self):
        if self.currentDate[0] < 180:
            self.currentDate[0] += 1
        else:
            self.currentDate[0] = 0
            self.currentDate[1] += 1

    def getDateAsString(self):
        return "day: " + str(self.currentDate[0]) + "year: " + str(self.currentDate[1])


if __name__ == "__main__":
    Env = Environment()
    cx = GUI(Env)
    cx.start()
