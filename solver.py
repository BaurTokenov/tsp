import csv
from fileparser import readfile
from randomSolver import randomSolver
from gaSolver import gaSolver
from localSearch import localSearch


def main():
    coordinates = readfile('a280.tsp')
    best = localSearch(coordinates)
    with open('solution.csv', mode='w') as solutionFile:
        solutionWriter = csv.writer(solutionFile)
        for (city, x, y) in best[1]:
            solutionWriter.writerow([int(city)])
        pass


main()
