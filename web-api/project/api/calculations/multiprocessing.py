from multiprocessing import Pool

def gen_matrix(n, m):
    return ((x, y) for x in range(n) for y in range(m))


def parse_points(points):
    # return (get_coords(x) for x in points)
    return [get_coords(x) for x in points]


def get_coords(string):
    split = string.split(",")
    return int(split[0]), int(split[1])


def get_distance(special, point, index):
    return abs(special[0] - point[0]) + abs(special[1] - point[1]), index


def get_nearest(specials, point):
    distances = (get_distance(s, point, ind) for ind, s in enumerate(specials))
    return min(distances)[1]


def multiprocessing(n, m, specials):
    specials = parse_points(specials)
    with Pool() as pool:
        yield from pool.imap(get_nearest, gen_matrix(n, m))
