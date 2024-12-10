from shared import get_antenas_and_size, iter_antenas_combinations


antenas, height, width = get_antenas_and_size()
antinodes: set[tuple[int, int]] = set()
for (ax, ay), (bx, by) in iter_antenas_combinations(antenas):
    dx = bx - ax
    dy = by - ay
    antinodes.add((ax, ay)) # position 0
    for direction in (-1, 1):
        i = 1
        while 0 <= (px := ax + i * dx) < width and 0 <= (py := ay + i * dy) < height:
            antinodes.add((px, py))
            i += direction

print(len(antinodes))
