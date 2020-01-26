import numpy as np
import matplotlib.pyplot as plt
import Visualize as vis
from Environment import Environment
from GenGrid import gen_grid
import csv
import scipy.stats as stats



"""
Project Computational Science
Sander van Oostveen, Jelle Mouissie and Joos Akkerman

This file contains the statistical analysis of data produced by the model
"""

ITERATIONS = 1
PERIODS = 5
TIME_PER_SEASON = 2
# LEVELS = 15
LEVELS = 5

def test_mono():
    """
    Tests survival of bee colony for different levels of monoculture,
    saves results to csv and plots results
    """

    # perform test for given amount of iterations
    for iter in range(ITERATIONS):
        results = []

        for level in range(LEVELS+1):
            with open(f"Grids/Monoculture/{level}.csv", 'w'): pass

        gen_grid()
        # TODO: USE GenGrid TO OVERWRITE GRIDS (Jelle)

        # perform test on grid for different levels
        for level in range(LEVELS + 1):
            Env = Environment()
            Env.OverrideValues(10, 10, 10, level)
            Env.reset()

            for i in range(TIME_PER_SEASON*PERIODS-1):
                Env.step()

            result = [iter, level, Env.GetPercentageMonoculture()]
            for val in Env.GetResults():
                result += [val]
            # print(len(result))
            # print(result)
            # results += [iter, level, result]
            results += [result]
            # print(results)


        # TODO WRITE RESULTS AS ROW TO CSV (Jelle)
        # open file to write results to
        print()
        with open(f'Results/monoculture.csv', 'a', newline='') as file:
            wr = csv.writer(file, quoting=csv.QUOTE_ALL)
            for row in results:
                wr.writerow(row)


    # TODO: IMPLEMENT VIS FUNCTION THAT PLOTS AVG POP ON Y-AXIS AND MONO LEVEL
    # ON X-AXIS
    vis.scatter_mono()


def regress(pop_sizes, mono_levels):
    """
    Performs a regression analysis over survival rate and level of monoculture,
    return slope
    """
    regress_result = stats.linregress(mono_levels, pop_sizes)
    return regress_result[0]


def ttest():
    """
    Performs student t-test to determine significance effect of monoculture on
    population size.
    """

    # open test results and perform regression analysis
    betas = []
    with open(f"Results/monoculture.csv") as f:
        csv_reader = csv.reader(f, delimiter=',')

        iterations = {}
        for run in csv_reader:
            if int(run[0]) not in iterations:
                iterations[int(run[0])] = {int(run[1]): int(run[-1])}
            else:
                iterations[int(run[0])][int(run[1])] = int(run[-1])

        print(iterations)
        for iteration in iterations:
            mono_levels = list(iterations[iteration].keys())
            pop_sizes = [iterations[iteration][i] for i in mono_levels]
            # mono_levels = [int(i) for i in mono_levels]
            # pop_sizes = [int(i) for i in pop_sizes]
            # all_pop_sizes += [pop_sizes]

            beta = regress(pop_sizes, mono_levels)
            betas += [beta]

        print(betas)
        vis.scatter_mono(iterations)

    # perform t-test
    ttest_result = stats.ttest_ind(betas, 0, equal_var=True)
    avg_beta = sum(betas)/len(betas)
    stddev_beta = np.std(betas)
    t_stat = ttest_result[0]
    p_value = ttest_result[1]
    print(f'Results from t-test:')
    print(f'Avg beta: {avg_beta}, stddev beta: {stddev_beta}.')
    print(f't-stat: {t_stat}, p-value: {p_value}.')


if __name__ == '__main__':
    test_mono()
    # ttest()
