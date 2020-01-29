import numpy as np
from PlantSpecies import generate_plant_species
from random import random
import csv

"""
Project Computational Science
Sander van Oostveen, Jelle Mouissie and Joos Akkerman

This file creates grids for different levels of monoculture
"""

NUTRITION_PER_PLANT = 500
ALL_PLANTS = {0: [NUTRITION_PER_PLANT, 2, 1, [1, 60]],
                1: [NUTRITION_PER_PLANT, 2, 1, [10, 70]],
                2: [NUTRITION_PER_PLANT, 2, 1, [30, 100]],
                3: [NUTRITION_PER_PLANT, 2, 1, [50, 110]],
                4: [NUTRITION_PER_PLANT, 2, 1, [70, 120]],
                5: [NUTRITION_PER_PLANT, 2, 1, [90, 140]],
                6: [NUTRITION_PER_PLANT, 2, 1, [110, 160]],
                7: [NUTRITION_PER_PLANT, 2, 1, [130, 170]],
                8: [NUTRITION_PER_PLANT, 2, 1, [160, 190]],
                9: [NUTRITION_PER_PLANT, 2, 1, [180, 200]]}
MONO_PLANT = 5

# generations only function properly in square grid with even breadt and width
HEIGHT = BREADTH = 10
DIVERSITY = 9

def gen_grid():
    """
    Generates grid with increasing degree of monoculture
    """
    # create initial grid:
    plantSpecies = []
    for plant_number in range(DIVERSITY):
        plantSpecies += [ALL_PLANTS[plant_number]]

    cells = []
    for y in range(HEIGHT):
        row = []
        for x in range(BREADTH):
            row += [gen_cell(DIVERSITY)]
        cells += [row]

    # writerow initial grid to csv
    with open('Grids/10by10/0.csv', 'w', newline='') as file:
        wr = csv.writer(file, quoting=csv.QUOTE_ALL)
        for row in cells:
            wr.writerow(row)

    # change initial grid with increasing monoculture
    for level in range(int(BREADTH/2)):
        level_cells = []

        # change rows and columns based on level and print to csv
        for row in cells:
            if cells.index(row) <= level or cells.index(row) >= HEIGHT-1-level:
                for cell in row:
                    row[row.index(cell)] = gen_cell_mono(MONO_PLANT)
            for i in range(level):
                row[i] = gen_cell_mono(MONO_PLANT)
                row[BREADTH-1-i] = gen_cell_mono(MONO_PLANT)

            level_cells.append(row)

            # print grids to csv
            with open(f'Grids/10by10/{level+1}.csv', 'w', newline='') as file:
                wr = csv.writer(file, quoting=csv.QUOTE_ALL)
                for row in level_cells:
                    wr.writerow(row)

def gen_cell(diversity):
    """
    Generates cell based on diversity level
    """
    vegitation = {}

    # spread plant species over cell
    randomindexes = []
    for y in range(diversity-2):
        randomindexes += [int(random()*100)]
    randomindexes.sort()
    randomindexes += [100]
    currentindex = 0

    for i in range(len(randomindexes)):
        amount = randomindexes[i] - currentindex
        currentindex = randomindexes[i]
        vegitation[i] = [amount, amount * ALL_PLANTS[i][0]]

    return vegitation


def gen_cell_mono(mono_plant):
    """
    Generates cell with only one plant species
    """
    vegitation = {}

    for plant in ALL_PLANTS:
        if plant == mono_plant:
            plant_prop = ALL_PLANTS[plant]
            vegitation[plant] = [10*plant_prop[0], plant_prop[1], plant_prop[2],
                                    plant_prop[3]]
        else:
            vegitation[plant] = [0,0]

    return vegitation


if __name__ == '__main__':
    gen_grid()
