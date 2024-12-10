from shared import get_antenas_and_size, iter_antenas_combinations

antenas, height, width = get_antenas_and_size()
antinodes: set[tuple[int, int]] = set()

for (ax, ay), (bx, by) in iter_antenas_combinations(antenas):
    for x, y in ((2 * ax - bx, 2 * ay - by), (2 * bx - ax, 2 * by - ay)):
        if 0 <= x < width and 0 <= y < height:
            antinodes.add((x, y))

print(len(antinodes))
