from shared import get_map, get_guard_position, direction_deltas

# TODO: esta malita esta solución
#
gamemap = get_map()

current_direction = 0
x, y = get_guard_position(gamemap)

width, height = len(gamemap[0]), len(gamemap)
posible_wall_placements: set[tuple[int, int]] = set()
while True:
    dx, dy = direction_deltas[current_direction]
    if not (0 <= x + dx < width and 0 <= y + dy < height):
        break

    if gamemap[y + dy][x + dx] == "#":
        current_direction = (current_direction + 1) % 4
        continue

    posible_wall_placements.add((x + dx, y + dy))
    x += dx
    y += dy

# print(posible_wall_placements)
count = 0
for wx, wy in posible_wall_placements:
    current_direction = 0
    x, y = get_guard_position(gamemap)
    visited: set[tuple[int, int, int]] = set()

    gamemap[wy][wx] = "#"
    looped = False
    while True:
        if (x, y, current_direction) in visited:
            looped = True
            break
        visited.add((x, y, current_direction))

        dx, dy = direction_deltas[current_direction]
        if not (0 <= x + dx < width and 0 <= y + dy < height):
            break

        if gamemap[y + dy][x + dx] == "#":
            current_direction = (current_direction + 1) % 4
            continue

        x += dx
        y += dy

    if looped:
        # print(wx, wy)
        count += 1
    gamemap[wy][wx] = "."


print(count)
#
