def fitness(coordinates):
    totalDistance = 0.0
    for i in range(len(coordinates)):
        cur = coordinates[i]
        prev = coordinates[i-1]
        ind0, x0, y0 = cur
        ind1, x1, y1 = prev
        distance = ((x0 - x1) * (x0 - x1) + (y0 - y1) * (y0 - y1)) ** 0.5
        totalDistance += distance
    return totalDistance
