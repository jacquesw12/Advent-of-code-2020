#!/usr/bin/env python3

import copy
from itertools import combinations

def check_next_nb(preamble, next_nb):
    for elt in combinations(preamble, 2):
        comb_sum = sum(list(map(int, list(elt))))
        if comb_sum == next_nb:
            return True
    return False

def main():
    with open('input.txt', 'r') as file:
        numbers = [line.strip() for line in file.readlines()]
        preamble_lgh = 25

        nb_part1 = 0
        ix_nb = 0
        # part 1
        for i in range(preamble_lgh, len(numbers)):
            preamble = numbers[i-preamble_lgh:i]
            if not check_next_nb(preamble, int(numbers[i])):
                ix_nb = i
                nb_part1 = int(numbers[i])
                break
        print(nb_part1)

        # part 2
        res_list = []
        for i in range(ix_nb):
            cur_sum = 0
            cur_list = []
            j = i
            while cur_sum <= nb_part1:
                if cur_sum == nb_part1:
                    print(cur_sum)
                    print(cur_list)
                    res_list = copy.deepcopy(cur_list)
                    break
                cur_sum += int(numbers[j])
                cur_list.append(int(numbers[j]))
                j += 1
        res_list.sort()
        print(res_list[0] + res_list[-1])

if __name__ == '__main__':
    main()

"""
Another solution suggested by a colleague

from collections import deque
from itertools import islice

def xmas(num_gen, sz=25):
    dq = deque(islice(num_gen, sz), sz)
    for cur_val in num_gen:
        if not [t for t in dq if cur_val-t in dq]:
            return cur_val
        dq += [cur_val]

print(xmas((int(n) for n in open("input_9"))))
"""
