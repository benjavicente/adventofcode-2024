data = list(map(int, input()))

gaps: list[tuple[int, int]] = []
placements: list[tuple[int, int]] = []
current_index = 0

# Crear gaps e posicines
for i, value in enumerate(data):
    if i % 2 == 0:
        placements.append((current_index, value))
    elif value != 0:
        gaps.append((current_index, value))
    current_index += value

# Ir desde atras hacia adelante tomando gaps
for i, (placement_index, placement_size) in reversed(list(enumerate(placements))):
    for j, (gap_index, gap_size) in enumerate(gaps):
        if gap_index >= placement_index:
            break # pasado
        if placement_size == gap_size:
            placements[i] = (gap_index, placement_size)
            gaps.pop(j)
            break # uso completo
        if placement_size < gap_size:
            placements[i] = (gap_index, placement_size)
            gaps[j] = (gap_index + placement_size, gap_size - placement_size)
            break # uso parcial


checksum = 0
for i, (placement_index, placement_size) in enumerate(placements):
    # secuencia triangular
    checksum += i * (placement_size * (placement_size + 2 * placement_index - 1) // 2)
print(checksum)
