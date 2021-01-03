def gen_matrix(n, m):
    values = []
    for x in range(n):
        for y in range(m):
            values.append((x, y))
    return values


def parse_points(points):
    coords = []
    for x in points:
        split = x.split(",")
        coords.append((int(split[0]), int(split[1])))
    return coords


def get_distance(special, point):
    return abs(special[0] - point[0]) + abs(special[1] - point[1])


def get_nearest(specials, point):
    distances = []
    for s in specials:
        distances.append(get_distance(s, point))
    print(distances)
    return distances.index(min(distances))


def sequential(n, m, specials):
    specials = parse_points(specials)
    matrix = gen_matrix(n, m)
    result = []
    for point in matrix:
        result.append(get_nearest(specials, point))

    return result
