from Cell import Cell
from PlantSpecies import generate_plant_species
import csv
import ast

"""
Project Computational Science
Sander van Oostveen, Jelle Mouissie and Joos Akkerman

This file defines the class Grid,
Which defines the behaviour of Grid which contains all cells.
"""

class Grid:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.plant_species = []


    def initialize_cells(self, diversity, monoculture_level):
        """
        Initializes cells by reading csv with requested monoculture level
        """
        self.cells = []

        for x in range(diversity):
            self.plant_species += [generate_plant_species(x)]

        with open(f"Grids/10by10/{monoculture_level}.csv") as f:            #TODO HIER MOET NOG IETS MEE
            csv_reader = csv.reader(f, delimiter=',')

            for csv_row in csv_reader:
                row = []
                for cell in csv_row:
                    prop_cell = ast.literal_eval(cell)
                    row.append(Cell(diversity, prop_cell, self.plant_species))
                self.cells += [row]


    def get(self, x, y):
        """
        Get the cell at the given coordinates
        """
        return self.cells[x][y]


    def get_limits(self):
        """
        Get the limits of the grid.
        """
        return self.x, self.y


    def get_food_matrix(self):
        """
        Get the current state of all food for visualisation perposes.
        """
        matrix = []
        for row in self.cells:
            foodrow = []
            for cell in row:
                foodrow += [cell.get_food_left()]
            matrix += [foodrow]
        return matrix


    def increment_year(self):
        """
        Increment every cell with one year
        triggering the updates done in the winter
        """
        for row in self.cells:
            for cell in row:
                cell.increment_year()


    def get_percentage_monoculture(self):
        """
        Return the percentage of the cells that qualify as a monoculture
        """
        monocultures = 0
        for row in self.cells:
            for cell in row:
                if cell.is_mono_culture():
                    monocultures += 1
        return monocultures / self.x * self.y
