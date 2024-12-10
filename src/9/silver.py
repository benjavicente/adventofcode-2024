
data = list(map(int, input()))
checksum = 0
current_index = 0

for i, value in enumerate(data):
    for _ in range(value):
        if i % 2 == 0:
            checksum += (i // 2) * current_index
        else:
            if data[-1] == 0:
                data.pop()
                data.pop()
            data[-1] -= 1
            checksum += (len(data) // 2) * current_index
        current_index += 1

print(checksum)
