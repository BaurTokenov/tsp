import random
import copy
import math
from fitness import fitness, calcDistance


def randomSolution(coordinates):
    curList = random.sample(coordinates, len(coordinates))
    return curList


def getNeighborSolution(solution):
    pos1 = random.randint(1, len(solution[1]) - 1)
    pos2 = random.randint(1, len(solution[1]) - 1)
    newSolution = copy.deepcopy(solution[1])
    newSolution[pos1], newSolution[pos2] = newSolution[pos2], newSolution[pos1]
    return (fitness(newSolution), newSolution)


def shouldAccept(newSolution, curSolution, temperature):
    if newSolution[0] < curSolution[0]:
        return 1.0
    return math.e ** ((curSolution[0] - newSolution[0])/temperature)


def cooling(timer):
    return 1005 / math.log(timer + 123)


def ls(coordinates):
    curSolution = randomSolution(coordinates)
    fit = fitness(curSolution)
    curSolution = (fit, curSolution)
    climb = True
    timer = 1
    temperature = cooling(timer)
    while climb:
        neighbors = []
        climb = False
        timer += 1
        for i in range(100):
            newSolution = getNeighborSolution(curSolution)
            if newSolution[0] < curSolution[0]:
                climb = True
                curSolution = newSolution
            print(shouldAccept(newSolution, curSolution,
                               temperature) > random.random())
            temperature = cooling(timer)
        print("CurSolution:", curSolution[0])

    return curSolution


def localSearch(coordinates):
    return ls(coordinates)
