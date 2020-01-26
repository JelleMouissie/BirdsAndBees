import numpy as np
import matplotlib.pyplot as plt
import Visualize as vis


"""
Project Computational Science
Sander van Oostveen, Jelle Mouissie and Joos Akkerman

This file contains the statistical analysis of data produced by the model
"""

ITERATIONS = 10
PERIODS = 6
LEVELS = 15

def test_mono():
    """
    Tests survival of bee colony for different levels of monoculture,
    saves results to csv and plots results
    """

    # perform test for given amount of iterations
    for iter in range(ITERATIONS):
        results = []

        # TODO: USE GenGrid TO OVERWRITE GRIDS (Jelle)

        # perform test on grid for different levels
        for level in range(LEVELS + 1):
            pass
            # TODO: RUN MODEL FOR GIVEN LEVEL (Jelle)
            # TODO: COLLECT AVG POPULATION SIZE OF HIVE IN LAST PERIOD (Jelle)
            # TODO: SAVE POPULATION SIZE IN ORDER OF MON LEVELS (Jelle)

        # TODO WRITE RESULTS AS ROW TO CSV (Jelle)
        # open file to write results to
        # with open(f'Results/monoculture.csv', 'a', newline='') as file:
        #     wr = csv.writer(file, quoting=csv.QUOTE_ALL)
        #     for row in cells:
        #         wr.writerow(row)


    # TODO: IMPLEMENT VIS FUNCTION THAT PLOTS AVG POP ON Y-AXIS AND MONO LEVEL
    # ON X-AXIS
    vis.scatter_mono()


def regress():
    """
    Performs a regression analysis over survival rate and level of monoculture
    """
    # TODO: PERFORM REGRESSION ANALYSIS
    pass


def ttests():
    """
    Performs student t-tests to determine significance effect of monoculture on
    population size.
    """
    # TODO: PERFORM T-TESTS
    pass




if __name__ == '__main__':
    test_mono()
    regress()
    ttests()
