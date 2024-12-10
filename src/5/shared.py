from functools import cmp_to_key

class Rules:
    def __init__(self):
        self.orders: dict[tuple[int, int], bool] = {}

        def _sort_key(a, b):
            return self.sort_order(a, b)
        self.sort_key = cmp_to_key(_sort_key)

    def add_rule(self, a: int, b: int):
        self.orders[(b, a) if a >= b else (a, b)] = a >= b

    def sort_order(self, a: int, b: int):
        # todo: creo que esto está malo
        key = (b, a) if a >= b else (a, b)
        if key not in self.orders:
            return 0
        return 1 if self.orders[key] == (a >= b) else -1

    def is_sorted(self, update: list[int]):
        for i, value in enumerate(update):
            for left_value in update[:i]:
                if self.sort_order(left_value, value) == -1:
                    return False
            for right_value in update[i+1:]:
                if self.sort_order(value, right_value) == -1:
                    return False
        return True

def get_pages():
    rules = Rules()
    updates = []
    is_reading_rules = True
    while True:
        try:
            entry = input().strip()
            if entry == "":
                is_reading_rules = False
            elif is_reading_rules:
                a, b = entry.split("|")
                rules.add_rule(int(a), int(b))
            else:
                updates.append(list(map(int, entry.split(","))))
        except EOFError:
            break
    return rules, updates
