import random
from fitness import fitness


def randomSolver(coordinates):
    bestDistance = 999999.9

    readFile = open("randomBest.txt", "r")
    bestStr = readFile.readline()
    if bestStr:
        bestDistance = float(bestStr)

    bestAnswer = None
    fitnessEvalutations = 300000
    while fitnessEvalutations:
        print('fitnessEvaluationsCnt:', fitnessEvalutations)
        fitnessEvalutations -= 1
        curList = random.sample(coordinates, len(coordinates))
        curDistance = fitness(curList)
        print(curDistance)
        if curDistance < bestDistance:
            bestDistance = curDistance
            bestAnswer = curList
    print("RANDOM SOLVER")
    print('bestDistance', bestDistance)
    writeFile = open("randomBest.txt", "w")
    writeFile.write(str(bestDistance))
    readFile.close()
    writeFile.close()
    # print('bestAnswer', curList)
