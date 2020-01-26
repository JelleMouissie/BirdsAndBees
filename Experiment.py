import Environment as En
import matplotlib.pyplot as plt
import numpy as np
import random

def find_peaks(population):
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

    # for i, x in enumerate(population):
    #     if i > 0 and i < size:
    #         if x > old and x > population[i+1]:
    #             result.append((x,i))
    #     old = x
    return result

def randomize_2d(lst):
    len1 = len(lst)
    len2 = len(lst[0])

    flat = [l for sub in lst for l in sub]
    np.random.shuffle(flat)

    return [[flat[i*len1 + j] for i in range(len2)] for j in range(len1)]

def get_monoculture(grid):
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
    grid_size = len(Env.grid.cells)
    size = int(grid_size*grid_size * percentage /100)

    indices = [(x,y) for x in range(0,grid_size) for y in range(0,grid_size)]
    samples = random.sample(indices, size)

    for i,j in samples:
        Env.grid.cells[i][j] = monoCell




def run_sim(Env, percentage):
    Env.monoculture_level = 1
    Env.reset()

    monoCell = Env.grid.cells[0][0]
    increase_mono(percentage, Env, monoCell)
    # Env.grid.cells = randomize_2d(Env.grid.cells)
    i = 0

    div_grid1 = get_monoculture(Env.grid.cells)

    while i < 5:
        if Env.step():
            i += 1

    population = Env.hives[0].Getpophistory()
    peaks = find_peaks(population)
    print(peaks)

    pX = [peak[1] for peak in peaks]
    pY = [peak[0] for peak in peaks]

    coef, b = np.polyfit(pX,pY,1)
    print("Coeff is:" + str(coef))
    xX = range(pX[0], pX[-1])
    xY = [coef * x + b for x in xX]

    # Plot stuff for individual runs

    # plt.figure(1)
    #
    # plt.plot(range(len(population)), population, xX, xY)
    # plt.figure(2)
    #
    # div_grid2 = get_monoculture(Env.grid.cells)
    # plt.imshow(div_grid1)
    # plt.colorbar()
    #
    # plt.figure(3)
    # plt.imshow(div_grid2)
    # plt.colorbar()
    # plt.show()
    # print(peaks)

    return coef

if __name__ == "__main__":
    Env = En.Environment()
    results = []
    # run_sim(Env, 94)

    for i in range(90,100):
        temp_results = []
        for j in range(5):
            temp_results.append(run_sim(Env, i))
        results.append(np.mean(temp_results))

    plt.plot(range(90,100), results)
    plt.show()
