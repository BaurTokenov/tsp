import random
import copy
import math
from fitness import fitness, calcDistance

fitnessEvaluations = 0


def randomSolution(coordinates):
    curList = random.sample(coordinates, len(coordinates))
    return curList


def getNeighborSolution(solution):
    global fitnessEvaluations
    pos1 = random.randint(1, len(solution[1]) - 1)
    pos2 = random.randint(1, len(solution[1]) - 1)
    newSolution = copy.deepcopy(solution[1])
    newSolution[pos1], newSolution[pos2] = newSolution[pos2], newSolution[pos1]
    fitnessEvaluations -= 1
    return (fitness(newSolution), newSolution)


def shouldAccept(newSolution, curSolution, temperature):
    if newSolution[0] < curSolution[0]:
        return 1.0
    return math.e ** ((curSolution[0] - newSolution[0])/temperature)


def cooling(timer):
    return 105 / math.log(100*timer + 123)


def ls(coordinates):
    global fitnessEvaluations
    curSolution = randomSolution(coordinates)
    fit = fitness(curSolution)
    fitnessEvaluations -= 1
    curSolution = (fit, curSolution)
    timer = 1
    temperature = cooling(timer)

    while fitnessEvaluations >= 0:
        neighbors = []
        timer += 10000

        for i in range(200):
            newSolution = getNeighborSolution(curSolution)
            # flag is necessary for the first ascent approach
            flag = False
            if (fitnessEvaluations <= 0):
                return curSolution
            if shouldAccept(newSolution, curSolution,
                            temperature) > random.random():
                curSolution = newSolution
                flag = True
            temperature = cooling(timer)
            if flag:
                break
        print("Current solution:", curSolution[0])

    return curSolution


def localSearch(coordinates, fitnessEvaluationsArg):
    global fitnessEvaluations
    fitnessEvaluations = fitnessEvaluationsArg
    return ls(coordinates)
