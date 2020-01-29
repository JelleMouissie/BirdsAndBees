import Environment as En
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
import random
import csv
import Analysis as ana

"""
Project Computational Science
Sander van Oostveen, Jelle Mouissie and Joos Akkerman

This file contains the code that runs our experiments.
"""

def find_peaks(population):
    """
    Find yearly peaks in the population
    """
    size = len(population) - 1
    result = []

    for i in range(1,5):
        largest = 0
        large_j = 0
        for j in range(i*200, i*200 + 200):
            if population[j] > largest:
                largest = population[j]
                large_j = j
        result.append((largest, large_j))
    return result

def randomize_2d(lst):
    """
    Randomize a 2d list
    """
    len1 = len(lst)
    len2 = len(lst[0])

    flat = [l for sub in lst for l in sub]
    np.random.shuffle(flat)

    return [[flat[i*len1 + j] for i in range(len2)] for j in range(len1)]


def get_monoculture(grid):
    """
    returns the diversity in the grid as a matrix
    """
    div_grid = []
    for row in grid:
        div_row = []
        for cell in row:
            diversity = 0
            for plant in cell.vegitation:
                if cell.vegitation[plant][0] != 0:
                    diversity += 1
            div_row.append(diversity)
        div_grid.append(div_row)
    return div_grid


def increase_mono(percentage, Env, monoCell):
    """
    Increase the percentage of monoculture in a grid
    """
    grid_size = len(Env.grid.cells)
    size = int(grid_size*grid_size * percentage /100)

    indices = [(x,y) for x in range(0,grid_size) for y in range(0,grid_size)]
    samples = random.sample(indices, size)

    for i,j in samples:
        Env.grid.cells[i][j] = monoCell


def get_maps(Env, percentage):
    """
    Get a Grid with a monoculture percentage
    """
    Env.monoculture_level = 1
    Env.reset()

    monoCell = Env.grid.cells[0][0]
    increase_mono(percentage, Env, monoCell)
    Env.grid.cells = randomize_2d(Env.grid.cells)

    return get_monoculture(Env.grid.cells)


def run_sim(Env, percentage):
    """
    Run a simulation
    """
    Env.monoculture_level = 1
    Env.reset()

    monoCell = Env.grid.cells[0][0]
    increase_mono(percentage, Env, monoCell)
    Env.grid.cells = randomize_2d(Env.grid.cells)
    i = 0

    div_grid1 = get_monoculture(Env.grid.cells)

    while i < 5:
        if Env.step():
            i += 1

    population = Env.hives[0].get_pop_history()
    peaks = find_peaks(population)
    print(peaks)

    pX = [peak[1] for peak in peaks]
    pY = [peak[0] for peak in peaks]

    if pY[0] is 0:
        return 0, False

    coef = 1
    b = 1

    # Plot stuff for individual runs
    plt.figure(1)

    plt.plot(range(len(population)), population)
    plt.xlabel("Day in Foraging Season")
    plt.ylabel("Bees in Population")

    plt.savefig('Figures/popGrowthStable.svg', transparent=True)

    fig, axs = plt.subplots(1,2, sharex=True, sharey=True)
    div_grid2 = get_monoculture(Env.grid.cells)
    axs[0].imshow(div_grid1)
    axs[0].set_title("Environment Year 0")
    axs[0].set(xlabel='Breadth', ylabel='Height',xticks=[0,2,4,6,8])
    im = axs[1].imshow(div_grid2)
    axs[1].set_title("Environment Year 5")
    axs[1].set(xlabel='Breadth', ylabel='Height',xticks=[0,2,4,6,8])
    plt.colorbar(im, ax=axs)
    plt.savefig('Figures/EnvironmentChange.svg', transparent=True)
    plt.show()

    return coef, True


def try_sim(Env, i):
    """
    Try simulations untill we get a satisfactory result
    """
    v = 0
    while(True):
        coef, again = run_sim(Env, i)
        v += 1
        if again or v > 5:
            break


def experiment(Env):
    results = []
    for j in range(10):
        print(f'Iteration: {j}')
        for i in range(0,100,10):
            print(f'Percentage: {i}')
            try_sim(Env, i)
            results.append([j+1,i+1] + Env.hives[0].get_pop_history())

    with open('Results/mono_test.csv','w') as result_file:
        wr = csv.writer(result_file, dialect='excel')
        wr.writerows(results)


def conclusion_experiment(Env):
    """
    Write the result of the final experiment to a csv file
    """
    results = []
    for j in range(10):
        print(f'Iteration: {j}')
        for i in range(30,70,2):
            print(f'Percentage: {i}')
            try_sim(Env, i)
            results.append([j+1,i+1] + Env.hives[0].get_pop_history())

    with open('Results/conclusion.csv','w') as result_file:
        wr = csv.writer(result_file, dialect='excel')
        wr.writerows(results)


def make_maps(Env):
    """
    Create Figures of the different maps
    """
    maps = []
    for i in [20,40,60,80]:
        maps.append(get_maps(Env, i))

    fig, axs = plt.subplots(2,2,sharex=True,sharey=True)
    im = None
    for i in range(2):
        for j in range(2):
            im = axs[i,j].imshow(maps[i*2 + j])
            axs[i,j].set_title(f'Biodiversity: {80 - (i*2+j) * 20}%')

    for ax in axs.flat:
        ax.set(xlabel='Breadth', ylabel='Height',xticks=[0,2,4,6,8])
        ax.label_outer()

    plt.colorbar(im, ax=[axs[0,0], axs[0,1], axs[1,0], axs[1,1]])
    plt.savefig('Figures/diffPercentage3.svg', transparent=True)


if __name__ == "__main__":
    Env = En.Environment()
    # experiment(Env)
    conclusion_experiment(Env)
    # make_maps(Env)
    ana.ttest()
