from collections import defaultdict
from itertools import combinations

def get_antenas_and_size():
    grid = []
    while True:
        try:
            grid.append(list(input()))
        except EOFError:
            break

    antenas: dict[str, set[tuple[int, int]]] = defaultdict(set)
    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            if value != ".":
                antenas[value].add((x, y))
    return antenas, len(grid), len(grid[0])


def iter_antenas_combinations(antenas: dict[str, set[tuple[int, int]]]):
    for char, positions in antenas.items():
        for permutation in combinations(positions, 2):
            yield permutation
