import random
from fitness import fitness, calcDistance


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


def ga(populationSize, generations, coordinates):
    population = []
    for i in range(populationSize):
        randSol = randomSolution(coordinates)
        fit = fitness(randSol)
        population.append((fit, randSol))

    curGen = 0
    best = (9999999, [])
    for g in range(generations):
        children = []
        while len(children) < populationSize:
            parent1 = selection(population, 10)
            parent2 = selection(population, 10)
            offspring1 = crossover(parent1, parent2)
            offspring1 = mutate(offspring1, 0.1)
            offspring1 = (fitness(offspring1[1]), offspring1[1])
            children.append(offspring1)

            offspring2 = crossover(parent2, parent1)
            offspring2 = mutate(offspring2, 0.1)
            offspring2 = (fitness(offspring2[1]), offspring2[1])
            children.append(offspring2)

        pool = population
        pool.extend(children)
        pool = sorted(pool, key=lambda x: x[0])
        population = pool[:populationSize]
        # population = children
        # population = sorted(population, key=lambda x: x[0])
        # for solution in population:
        #     if solution[0] < best[0]:
        #         best = solution
        if pool[0][0] < best[0]:
            best = pool[0]

        print("Best in generation:", g, best[0], population[0][0])
    print('Final Generation:', best[0])


def gaSolver(coordinates):
    ga(5000, 500, coordinates)