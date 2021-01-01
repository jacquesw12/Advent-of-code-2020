#!/usr/bin/env python3

from math import pow

def calc_row_or_col(in_str): 
    out = 0
    for ix, cur_letter in enumerate(in_str):
        if cur_letter == 'B' or cur_letter == 'R':
            out += pow(2,len(in_str) - 1 -ix)
    return out

def main():
    with open('input.txt', 'r') as file:
        boarding_passes = [(x[:7],x[7:]) for x in file.read().strip().split('\n')]
        
        # part 1
        max_id = 0
        seat_ids = []
        for bp in boarding_passes:
            seat_id = 8 * calc_row_or_col(bp[0]) + calc_row_or_col(bp[1])
            seat_ids.append(seat_id)
            max_id = max(max_id, seat_id)
        print(f'Part 1 : The max seat id is {max_id}.')
        
        # part 2
        seat_ids.sort()
        for i in range(len(seat_ids)-1):
            if seat_ids[i+1] - seat_ids[i] > 1:
                print(f'Part 2 : The missing seat id is {seat_ids[i+1] - 1}.')
                break

if __name__ == '__main__':
    main()
