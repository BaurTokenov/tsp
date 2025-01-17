import random
from fitness import fitness, calcDistance

fitnessEvaluations = 0


def randomSolution(coordinates):
    curList = random.sample(coordinates, len(coordinates))
    return curList


def selection(miniPopulation, k):
    tournament_pool = random.sample(miniPopulation, k)
    result = sorted(tournament_pool, key=lambda x: x[0])
    return result[0]


def crossover(p1, p2):
    cut = random.randint(1, len(p1[1]) - 1)
    offspring = p1[1][:cut]
    usedCities = set()
    for i in range(cut):
        curCity = p1[1][i][0]
        usedCities.add(curCity)
    for cityTuple in p2[1]:
        if not cityTuple[0] in usedCities:
            offspring.append(cityTuple)
        if len(offspring) == len(p1[1]):
            break
    return (0, offspring)


def mutate(solution, rate):
    if random.random() < rate:
        pos1 = random.randint(1, len(solution[1]) - 1)
        pos2 = random.randint(1, len(solution[1]) - 1)
        solution[1][pos1], solution[1][pos2] = solution[1][pos2], solution[1][pos1]

    return solution


def replacement(population, children, replacementType):
    # sort the parents + children and keep the best
    if replacementType == 1:
        pool = population + children
        pool = sorted(pool, key=lambda x: x[0])
        return pool[:len(population)]
    # children fully replace parents
    if replacementType == 2:
        return children
    # replace worst parents with better children
    if replacementType == 3:
        keepers = len(population) // 2
        parents = sorted(population, key=lambda x: x[0])[:keepers]
        children = sorted(children, key=lambda x: x[0], reverse=True)[keepers:]
        population = parents + children
        return population


def ga(populationSize, generations, coordinates):
    population = []
    global fitnessEvaluations

    # initialize population
    for i in range(populationSize):
        randSol = randomSolution(coordinates)
        fit = fitness(randSol)
        fitnessEvaluations -= 1
        population.append((fit, randSol))

    best = (99999999999, [])
    mutationRate = 0.5

    for g in range(generations):
        children = []
        while len(children) < populationSize:
            tournamentPoolSize = 5
            parent1 = selection(population, tournamentPoolSize)
            parent2 = selection(population, tournamentPoolSize)

            offspring1 = crossover(parent1, parent2)
            offspring1 = mutate(offspring1, mutationRate)
            offspring1 = (fitness(offspring1[1]), offspring1[1])
            children.append(offspring1)
            fitnessEvaluations -= 1

            offspring2 = crossover(parent2, parent1)
            offspring2 = mutate(offspring2, mutationRate)
            offspring2 = (fitness(offspring2[1]), offspring2[1])
            children.append(offspring2)
            fitnessEvaluations -= 1

        population = replacement(population, children, 3)
        for solution in population:
            if solution[0] < best[0]:
                best = solution
        if fitnessEvaluations <= 0:
            return best
        print("Best in generation", g, ':', best[0])
    return best


def gaSolver(coordinates, populationSize, fitnessEvaluationsArg):
    global fitnessEvaluations
    fitnessEvaluations = fitnessEvaluationsArg
    return ga(populationSize, 20000, coordinates)
