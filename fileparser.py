import fitness


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
        if "EOF" in line or not line:
            continue
        coord = [float(item) for item in line.strip().split()]
        coordinates.append(coord)
    return coordinates
