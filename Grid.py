from Cell import Cell

class Grid:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def initializeCells(self, diversity):
        self.cells = []
        for y in range(self.y):
            row = []
            for x in range(self.x):
                row += [Cell(diversity)]
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
                cell.incrementYear()
