# BirdsAndBees

Project Computational Science
Sander van Oostveen (10997989), Jelle Mouissie (11348410) and Joos Akkerman (11304723)

This repository contains the code used to run a bee population dynamics model, build for the UvA course Project Computational Science. This model simulates the decrease in bee population size under increased monoculture, which decreases the food supply. 

To run the model, run the file `Environment.py`. This file opens a GUI which allows for the change of initial parameters and shows the resulting graphs of the run, and prints the resulting values.

To execute the conducted experiment, run the file `Experiment.py`. This will yield the graphs for the run experiments, update the data and perform a t-test. This t-test shows the results for the following hypotheses:

* H0: There is no effect of a decrease biodiversity on the studied bee population size.
* H1: There is a significant effect of a decrease in biodiversity on the studied bee population size.

If the experiment has been executed and the data is available, it is also possible to solely run the regression analysis and t-test. This is done by running the file `Analysis.py`.

The resulting graphs are saved in the map `Figures`, data is saved in `Results` and the biodiversity grids are saved in `Grids`.
