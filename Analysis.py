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
TIME_PER_SEASON = 200
LEVELS = 5


def regress(pop_sizes, mono_levels):
    """
    Performs a regression analysis over survival rate and level of monoculture,
    return slope
    """
    regress_result = stats.linregress(mono_levels, pop_sizes)
    return regress_result


def get_max_run(run):
    """
    Gets the maximum population size in a run
    """
    max = 0
    max_i = 0
    for i in range(800, 900):
        if int(run[i]) > int(max):
            max = run[i]
            max_i = i
    return max, max_i



def ttest():
    """
    Performs student t-test to determine significance effect of monoculture on
    population size.
    """
    # open test results and perform regression analysis
    alphas = []
    betas = []
    iterations = {}
    with open(f"Results/conclusion2.csv") as f:
        csv_reader = csv.reader(f, delimiter=',')

        for run in csv_reader:
            max, max_i = get_max_run(run)
            if int(run[0]) not in iterations:
                iterations[int(run[0])] = {100 - int(run[1])-1: int(max)}
            else:
                iterations[int(run[0])][100 - int(run[1])-1] = int(max)

        for iteration in iterations:
            mono_levels = list(iterations[iteration].keys())
            pop_sizes = [iterations[iteration][i] for i in mono_levels]

            regress_result = regress(pop_sizes, mono_levels)
            alphas += [regress_result[1]]
            betas += [regress_result[0]]

    # plot scatter and regression line
    avg_alpha = sum(alphas)/len(alphas)
    avg_beta = sum(betas)/len(betas)
    stddev_beta = np.std(betas)
    vis.scatter_mono(iterations, avg_alpha, avg_beta)

    # perform t-test
    ttest_result = stats.ttest_ind(betas, [0 for i in betas], equal_var=True)
    t_stat = ttest_result[0]
    p_value = ttest_result[1]
    print(f'Results from t-test:')
    print(f'Avg beta: {avg_beta}, stddev beta: {stddev_beta}.')
    print(f't-stat: {t_stat}, p-value: {p_value}.')


if __name__ == '__main__':
    """
    Perform tests with different monocultures or a t-test
    """
    ttest()
