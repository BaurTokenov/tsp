import csv
import sys

from fileparser import readfile
from randomSolver import randomSolver
from gaSolver import gaSolver
from localSearch import localSearch


def main():
    coordinates = readfile(sys.argv[1])

    fitnessEvaluations = int(input(
        'Please input number of fitness evaluations:\n'
    ).strip())

    algoType = input(
        'Please enter algorithm type; 1 for Genetic Algorithm, 2 for Simulated Annealing:\n')

    best = None

    if int(algoType.strip()) == 1:
        populationSize = int(input("Please enter population size:\n"))
        best = gaSolver(coordinates, populationSize, fitnessEvaluations)
    else:
        best = localSearch(coordinates, fitnessEvaluations)

    print('Final answer:', best[0])

    with open('solution.csv', mode='w') as solutionFile:
        solutionWriter = csv.writer(solutionFile)
        for (city, x, y) in best[1]:
            solutionWriter.writerow([int(city)])
        pass


main()
