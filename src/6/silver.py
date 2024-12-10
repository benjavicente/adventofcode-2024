from shared import get_map, get_guard_position, direction_deltas

gamemap = get_map()

current_direction = 0

x, y = get_guard_position(gamemap)
width, height = len(gamemap[0]), len(gamemap)
count = 1
gamemap[y][x] = "!"

while True:
    dx, dy = direction_deltas[current_direction]
    if not (0 <= x + dx < width and 0 <= y + dy < height):
        break

    if gamemap[y + dy][x + dx] == "#":
        current_direction = (current_direction + 1) % 4
        continue

    x += dx
    y += dy

    if gamemap[y][x] != "!":
        gamemap[y][x] = "!"
        count += 1

for row in gamemap:
    print("".join(row))

print(count)
