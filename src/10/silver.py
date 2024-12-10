from collections import defaultdict
from shared import get_topographic_map

topographic_map = get_topographic_map()
cells_positions: dict[int, set[tuple[int, int]]] = defaultdict(set)

# Obtener la posición por número
for y in range(len(topographic_map)):
    for x in range(len(topographic_map[y])):
        cells_positions[topographic_map[y][x]].add((x, y))

# Obtener los números 9
cells_end_trails: dict[tuple[int, int], set[tuple[int, int]]] = defaultdict(set)
for top_cell in cells_positions[9]:
    cells_end_trails[top_cell].add(top_cell)

# Expandir hacia 0
for i in reversed(range(0, 9)):
    new_cells_end_trails: dict[tuple[int, int], set[tuple[int, int]]] = defaultdict(set)
    for cell in cells_positions[i]:
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if (cx := cell[0] + dx, cy  := cell[1] + dy) in cells_end_trails:
                new_cells_end_trails[cell].update(cells_end_trails[(cx, cy)])
    cells_end_trails = new_cells_end_trails

print(sum(len(trails) for trails in cells_end_trails.values()))
