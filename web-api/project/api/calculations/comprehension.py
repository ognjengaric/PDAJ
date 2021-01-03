def gen_matrix(n, m):
    return [(x, y) for x in range(n) for y in range(m)]


def parse_points(points):
    return [get_coords(x) for x in points]


def get_coords(string):
    split = string.split(",")
    return int(split[0]), int(split[1])


def get_distance(special, point):
    return abs(special[0] - point[0]) + abs(special[1] - point[1])


def get_nearest(specials, point):
    distances = [get_distance(s, point) for s in specials]
    return distances.index(min(distances))


def comprehension(n, m, specials):
    specials = parse_points(specials)
    matrix = gen_matrix(n, m)
    return [get_nearest(specials, point) for point in matrix]
