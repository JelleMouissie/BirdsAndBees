from Cell import Cell
from PlantSpecies import GeneratePlantSpecies
import csv
import ast

class Grid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.plantSpecies = []

    # def initializeCells(self, diversity):
    #     self.cells = []
    #
    #     for y in range(self.y):
    #         row = []
    #         for x in range(self.x):
    #             row += [Cell(diversity)]
    #         self.cells += [row]

    def initializeCells(self, diversity, monoculture_level):
        """
        Initializes cells by reading csv with requested monoculture level
        """


        self.cells = []

        # VERPLAATST VANAF CELL OMDAT ZE MAAR EEN KEER GEGENEREERD HOEVEN TE WORDEN
        for x in range(diversity):
            self.plantSpecies += [GeneratePlantSpecies(x)]

        with open(f"Grids/Monoculture/{monoculture_level}.csv") as f:
            csv_reader = csv.reader(f, delimiter=',')
            # cells = [line.split() for line in f]
            # for row in cells:
            #     print(row)
            # cells = []
            for csv_row in csv_reader:
                row = []
                for cell in csv_row:
                    prop_cell = ast.literal_eval(cell)
                    # print(cell)
                    # print(prop_cell, len(self.plantSpecies))
                    row.append(Cell(diversity, prop_cell, self.plantSpecies))
                self.cells += [row]


    def Get(self, x, y):
        return self.cells[x][y]

    def Getlimits(self):
        return self.x, self.y

    def GetFoodMatrix(self):
        matrix = []
        for row in self.cells:
            foodrow = []
            for cell in row:
                foodrow += [cell.getFoodLeft()]
            matrix += [foodrow]
        return matrix

    def incrementYear(self):
        for row in self.cells:
            for cell in row:
                pass
                cell.incrementYear()

    def drought(self):
        for row in self.cells:
            for cell in row:
                pass
                cell.drought()

    def ForestFire(self, x, y):
        self.cells[x][y].burn()
