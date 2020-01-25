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
LEVELS = [0, 6, 9, 14]

def grid_heatmap(levels):
    """
    visualizes grid as heatmap based on diversity of plants
    """
    fig, axs = plt.subplots(2, 2)
    fig.suptitle('Food diversity for different levels of monoculture')
    grids = []
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
            grids += [grid]

    grid1 = np.array(grids[0])
    grid2 = np.array(grids[1])
    grid3 = np.array(grids[2])
    grid4 = np.array(grids[3])

    axs[0, 0].imshow(grid1)
    axs[0, 0].set_title(f'Mono level: {levels[0]}')
    axs[0, 1].imshow(grid2)
    axs[0, 1].set_title(f'Mono level: {levels[1]}')
    axs[1, 0].imshow(grid3)
    axs[1, 0].set_title(f'Mono level: {levels[2]}')
    axs[1, 1].imshow(grid4)
    axs[1, 1].set_title(f'Mono level: {levels[3]}')

    for ax in axs.flat:
        ax.set(xlabel='Breadth', ylabel='Height')

    for ax in axs.flat:
        ax.label_outer()

    # TODO PUT COLORBAR IN

    plt.show()


if __name__ == '__main__':
    grid_heatmap(LEVELS)
