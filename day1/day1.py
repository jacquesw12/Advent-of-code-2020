#!/usr/bin/env python3

import itertools

def main():
    with open('input.txt', 'r') as file:
        list_entries = [int(x) for x in file.read().strip().split('\n')]

        # part 1
        for entry1, entry2 in itertools.product(list_entries, list_entries):
            if entry1 + entry2 == 2020:
                print(entry1, entry2)
                print(entry1 * entry2)
                break

        # part 2
        for entry1, entry2, entry3 in itertools.product(list_entries, list_entries, list_entries):
            if entry1 + entry2 + entry3 == 2020:
                print(entry1, entry2, entry3)
                print(entry1 * entry2 * entry3)
                break

if __name__ == '__main__':
    main()

"""
Solution suggested by a colleague

from itertools import product

def product_if_sum_is(value, *lists):
    for prod in (p for p in product(*lists) if sum(p) == value):
        return reduce(lambda a, b: a*b, prod)

with open("1a.txt") as f:
    numbers = [int(row) for row in f]
    print('1a: %s' % product_if_sum_is(2020, numbers, numbers))
    print('1b: %s' % product_if_sum_is(2020, numbers, numbers, numbers))

"""
