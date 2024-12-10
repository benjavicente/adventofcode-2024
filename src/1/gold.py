from shared import get_lists
from collections import Counter

left, right = get_lists()
counter = Counter(right)
similarity = sum(l * counter[l] for l in left)
print(similarity)
