import matplotlib.pyplot as plt
import csv
import ast
import numpy as np

"""
Project Computational Science
Sander van Oostveen, Jelle Mouissie and Joos Akkerman

This file visualizes tests performed on the model
"""
# levels of monoculture  visualized as heatmap
LEVELS = [0, 4, 9, 14]

def randomize_2d(lst):
    len1 = len(lst)
    len2 = len(lst[0])

    flat = [l for sub in lst for l in sub]
    np.random.shuffle(flat)

    return [[flat[i*len1 + j] for i in range(len2)] for j in range(len1)]

def grid_heatmap(levels, randomize):
    """
    visualizes grid as heatmap based on diversity of plants
    """
    fig, axs = plt.subplots(2, 2, sharex=True, sharey=True)
    # cbar_ax = fig.add_axes([.91,.3,.03,.4])

    fig.suptitle('Food diversity for different levels of monoculture')
    grids = []
    row_len = 0
    col_len = 0
    fractions = []
    for level in levels:
        grid = []
        with open(f"Grids/Monoculture/{level}.csv") as f:
            csv_reader = csv.reader(f, delimiter=',')
            for csv_row in csv_reader:
                row = []
                for csv_cell in csv_row:
                    cell = ast.literal_eval(csv_cell)
                    diversity = 0
                    for plant in cell:
                        if cell[plant][0] != 0:
                            diversity += 1
                    row += [diversity]
                grid += [row]
                row_len = len(row)
            col_len = len(grid)
            fraction = 100 - (((col_len - 2*level) * (row_len - 2*level))/(col_len * row_len)*100)
            fractions.append(fraction)
            if randomize:
                grid = randomize_2d(grid)
            grids += [grid]

    grids[0][0][0] = 1
    grid1 = np.array(grids[0])
    grid2 = np.array(grids[1])
    grid3 = np.array(grids[2])
    grid4 = np.array(grids[3])

    axs[0, 0].imshow(grid1)
    axs[0, 0].set_title(f'Mono level: {round(fractions[0],1)}%')
    im = axs[0, 1].imshow(grid2)
    axs[0, 1].set_title(f'Mono level: {round(fractions[1],1)}%')
    axs[1, 0].imshow(grid3)
    axs[1, 0].set_title(f'Mono level: {round(fractions[2],1)}%')
    axs[1, 1].imshow(grid4)
    axs[1, 1].set_title(f'Mono level: {round(fractions[3],1)}%')

    for ax in axs.flat:
        ax.set(xlabel='Breadth', ylabel='Height',xticks=[0,5,10,15,20,25])

    for ax in axs.flat:
        ax.label_outer()

    # TODO PUT COLORBAR IN
    col = plt.colorbar(im, ax = [axs[0,0],axs[0,1],axs[1,0], axs[1,1]])
    # col.set_ticks([0,5,10])

    plt.show()


def scatter_mono(iterations, avg_alpha, avg_beta):
    """
    Visualises scatter with relation between level of monoculture and average
    survival rate.
    """
    for iteration in iterations:
        data = iterations[iteration]
        for datapoint in data:
            plt.scatter(datapoint, data[datapoint], s=5, color='red')

    # plot regression line
    x = [0,90]
    y = [avg_alpha+avg_beta*i for i in x]
    plt.plot(x, y, color='blue', label='regression line')

    plt.title('Final population for differing levels of monoculture')
    plt.xlabel('Monoculture (%)')
    plt.ylabel('Surviving population')
    plt.legend(loc='upper right')
    plt.show()


if __name__ == '__main__':
    grid_heatmap(LEVELS, True)
