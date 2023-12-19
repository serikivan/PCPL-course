from get_random import gen_random

class Unique:
    def __init__(self, items, **kwargs):
        self.items = iter(items)
        self.ignore_case = kwargs.get('ignore_case', False)
        self.seen = set()

    def __next__(self):
        while True:
            item = next(self.items)
            key = item.lower() if self.ignore_case and isinstance(item, str) else item
            if key not in self.seen:
                self.seen.add(key)
                return item

    def __iter__(self):
        return self

if __name__ == '__main__':
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    unique_data = Unique(data)
    for item in unique_data:
        print(item, end=' ')
    print()

    data = gen_random(10, 1, 3)
    uniquesRow = Unique(data)
    for i in uniquesRow:
        print(i, end=' ')
    print()

    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    unique_data = Unique(data)
    for item in unique_data:
        print(item, end=' ')
    print()