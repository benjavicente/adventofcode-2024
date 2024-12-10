from shared import get_lists

left, right = map(sorted, get_lists())
distance = sum(abs(l - r) for l, r in zip(left, right))
print(distance)
