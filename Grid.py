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
