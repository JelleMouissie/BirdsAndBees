import matplotlib
import matplotlib.pyplot as plt
import sys
import pandas as pd
from Model import Model
from GUI import GUI
from Grid import Grid
from Hive import Hive


class Environment(Model):
    def __init__(self):
        Model.__init__(self)
        self.make_param('x', 10)
        self.make_param('y', 10)
        self.make_param('diversity', 2)

        self.hives =  self.makeHives()

    def reset(self):
        self.currentDate = [0, 0]
        self.grid = Grid(self.x, self.y)
        self.grid.initializeCells(self.diversity)


    def makeHives(self):
        return [Hive(5, 5, 10000, 10000, 1, 1)]

    def draw(self):
        print(self.hives[0].GetStatus())
        # pophistory = self.hives[0].Getpophistory()
        # deathhistory = self.hives[0].Getdeathhistory()
        # plt.plot(range(len(pophistory)), pophistory)
        # plt.plot(range(len(deathhistory)), deathhistory)
        print(self.currentDate)
        self.plotgrid()
        self.plotpop()
        pass
        # plt.cla()

    def step(self):
        self.incrementDate()
        for hive in self.hives:
            hive.update(self.grid, self.currentDate)      #TODO: Pass Grid object to retrieve plant information from Scout Bee location in Scout.update(Grid)


    def incrementDate(self):
        if self.currentDate[0] < 200:
            self.currentDate[0] += 1
        else:
            self.currentDate[0] = 0
            self.currentDate[1] += 1
            self.incrementYear()

    def incrementYear(self):
        self.draw()
        for hive in self.hives:
            hive.incrementYear()
        input("new year new me")

    def getDateAsString(self):
        return "day: " + str(self.currentDate[0]) + "year: " + str(self.currentDate[1])

    def plotgrid(self):
        plt.ion()
        plt.cla()
        df = pd.DataFrame(self.grid.GetFoodMatrix())
        plt.table(cellText=df.values, loc='center')
        plt.show()

    def plotpop(self):
        plt.cla()
        pophistory = self.hives[0].Getpophistory()
        deathhistory = self.hives[0].Getdeathhistory()
        plt.plot(range(len(deathhistory)), deathhistory)
        plt.plot(range(len(pophistory)), pophistory)
        plt.show()


if __name__ == "__main__":
    Env = Environment()
    cx = GUI(Env)
    cx.start()
