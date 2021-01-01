#!/usr/bin/env python3

import copy

def answers_anyone(file):
    list_sets = []
    cur_set = set()
    for line in file:
        if line.strip():
            letters = [c for c in line.strip()]
            if len(letters) > 1:
                cur_set.update(letters)
            else:
                cur_set.add(letters[0])
        else:
            list_sets.append(cur_set)
            cur_set = set()
    list_sets.append(cur_set)
    return list_sets

def answers_everyone(file):
    list_sets = []
    res_set = set()
    next_entry = False
    
    for line in file:
        if line.strip() and not next_entry:
            next_entry = True
            letters = [c for c in line.strip()]
            if len(letters) > 1:
                res_set.update(letters)
            else:
                res_set.add(letters[0])
        elif line.strip():
            cur_set = set()
            letters = [c for c in line.strip()]
            if len(letters) > 1:
                cur_set.update(letters)
            else:
                cur_set.add(letters[0])
            res_set = res_set.intersection(cur_set)
        else:
            list_sets.append(res_set)
            res_set = set()
            next_entry = False
    list_sets.append(res_set)
    return list_sets
            
def main():
    with open('input.txt', 'r') as file:
        list_sets1 = answers_anyone(file)
        print(list_sets1)
        count1 = 0
        for aset in list_sets1:
            count1 += len(aset)
        print(count1)
        
        file.seek(0)
        list_sets2 = answers_everyone(file)
        print(list_sets2)
        count2 = 0
        for aset in list_sets2:
            count2 += len(aset)
        print(count2)




if __name__ == '__main__':
    main()
