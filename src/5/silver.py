from shared import get_pages

rules, updates = get_pages()
count = 0
for update in updates:
    if rules.is_sorted(update):
        count += update[len(update) // 2]

print(count)
