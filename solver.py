from randomSolver import randomSolver
from fileparser import readfile


def main():
    coordinates = readfile('a280.tsp')
    randomSolver(coordinates)


main()
