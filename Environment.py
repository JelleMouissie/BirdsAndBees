import matplotlib
import matplotlib.pyplot as plt
import sys
import pandas as pd
from Model import Model
from GUI import GUI
from Grid import Grid
from Hive import Hive


"""
Project Computational Science
Sander van Oostveen, Jelle Mouissie and Joos Akkerman

This file contains the basic Environment in which the bee simulation is done. 
"""


class Environment(Model):
    def __init__(self):
        Model.__init__(self)
        self.make_param('x', 10)
        self.make_param('y', 10)
        self.make_param('diversity', 10)
        self.make_param('monoculture_level', 0)
        self.make_param('predators', 0.0000)
        self.hives =  self.makeHives()


    def reset(self):
        """
        Reset the current model.
        """
        self.current_date = [0, 0]
        self.grid = Grid(self.x, self.y)
        self.grid.initialize_cells(self.diversity, self.monoculture_level)
        self.hives =  self.makeHives()


    def makeHives(self):
        """
        Create a list of all hives.
        """
        return [Hive(5, 5, 10000, 10000, 1, 1, self.predators)]


    def draw(self):
        """
        Draw the current status and date and plot either the grid or the population
        """
        print(self.hives[0].GetStatus())
        print(self.current_date)
        # self.plotgrid()
        self.plotpop()


    def step(self):
        """
        Take one step in the Environment
        """
        year = self.increment_date()
        for hive in self.hives:
            hive.update(self.grid, self.current_date)
        return year


    def increment_date(self):
        """
        Increment the date by one
        """
        if self.current_date[0] < 200:
            self.current_date[0] += 1
            return False
        else:
            self.current_date[0] = 0
            self.current_date[1] += 1
            self.increment_year()
            return True


    def increment_year(self):
        """
        Increment The year by one and process winter in the grid and hives
        """
        for hive in self.hives:
            hive.increment_year()
        self.grid.increment_year()


    def get_date_as_string(self):
        """
        Return the current date as a string for the GUI
        """
        return "day: " + str(self.current_date[0]) + "year: " + str(self.current_date[1])


    def plotgrid(self):
        """
        Plot the food of the current Grid
        """
        plt.cla()
        df = pd.DataFrame(self.grid.get_food_matrix())
        plt.table(cellText=df.values, loc='center')
        plt.show()


    def plotpop(self):
        """
        Plot the population history of every hive.
        """
        plt.cla()
        for hive in self.hives:
            pophistory = hive.Getpophistory()
            plt.plot(range(len(pophistory)), pophistory)
        plt.show()


    def override_values(self, x, y, diversity, monoculture_level):
        """
        Override some basic values to acces the model without using the GUI
        """
        self.x = x
        self.y = y
        self.diversity = diversity
        self.monoculture_level = monoculture_level


    def get_results(self):
        """
        Return the population history of the Hive
        """
        return self.hives[0].Getpophistory()


    def get_percentage_monoculture(self):
        """
        Return the percentage of the grid that is a monoculture
        """
        return self.grid.get_percentage_monoculture()


if __name__ == "__main__":
    Env = Environment()
    cx = GUI(Env)
    cx.start()
