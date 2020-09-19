from fileparser import readfile
from randomSolver import randomSolver
from gaSolver import gaSolver


def main():
    coordinates = readfile('a280.tsp')
    gaSolver(coordinates)


main()
