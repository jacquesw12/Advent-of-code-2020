#!/usr/bin/env python3

def cant_be_removed(ix, adaptators):
    if (adaptators[ix + 1] - adaptators[ix]) == 3 or (adaptators[ix] - adaptators[ix - 1]) == 3 :
        return True
    return False

def count_combinations(invarients):
    nb_combinations = 1
    for i in range(len(invarients)-1):
        if invarients[i+1] - invarients[i] == 4:
            nb_combinations *= 7
        elif invarients[i+1] - invarients[i] == 3:
            nb_combinations *= 4
        elif invarients[i+1] - invarients[i] == 2:
            nb_combinations *= 2
        else:
            nb_combinations *= 1
    return nb_combinations
    

def main():
    with open('input.txt', 'r') as file:
        adaptators = [int(x) for x in file.read().strip().split('\n')]
        adaptators.sort()
        adaptators.insert(0,0)
        adaptators.append(adaptators[-1] + 3)
        print(adaptators)

        # part 1
        count_1_diff = 0
        count_3_diff = 0
        for ix in range(len(adaptators) - 1):
            if (adaptators[ix + 1] - adaptators[ix]) == 1:
                count_1_diff += 1
            if (adaptators[ix + 1] - adaptators[ix]) == 3:
                count_3_diff += 1
            
        print(count_1_diff)
        print(count_3_diff)
        print(count_1_diff * count_3_diff)

        # part 2
        # for ex 2, result = 7 * 7 * 4 * 2 * 7 * 7
        # for 3 consecutive: 7 possibilities
        # for 2, 4
        # for 1, 2

        list_invarients = [0]
        for i in range(1, len(adaptators) - 1):
            if (cant_be_removed(i, adaptators)):
                list_invarients.append(i)
        list_invarients.append(len(adaptators)-1)
        nb_comb = count_combinations(list_invarients)
        print(nb_comb)

if __name__ == '__main__':
    main()
