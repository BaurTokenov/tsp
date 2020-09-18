def readfile(filename):
    file = open('problems/' + filename, "r")
    lines = file.readlines()
    file.close()
    i = 0
    # find the start of the coordinates
    while lines[i] != 'NODE_COORD_SECTION\n':
        i += 1
    i += 1
    coordinates = []
    for j in range(i, len(lines) - 1):
        line = lines[j]
        coord = tuple(line.strip().split())
        coordinates.append(coord)
    return coordinates


print(readfile('a280.tsp'))
