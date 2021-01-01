#!/usr/bin/env python3

import copy

def go_through(inp_list):
    acc = 0
    ok = True
    cur_ix = 0
    ix_visited = [cur_ix]

    while ok and cur_ix < len(inp_list):
        next_ix = cur_ix
        if inp_list[cur_ix][0] == 'nop':
            next_ix += 1 
        elif inp_list[cur_ix][0] == 'acc':
            next_ix += 1 
            acc += inp_list[cur_ix][1]
        else:
            next_ix += inp_list[cur_ix][1]

        if next_ix in ix_visited:
            ok = False
            return False
        else: 
            ix_visited.append(next_ix)

        cur_ix = next_ix

    print (acc)
    return True

def main():
    with open('input.txt', 'r') as file:
        inp_list = []
        for line in file:
            operation, argument = line.strip().split(' ')
            inp_list.append((operation, int(argument)))
        
        # Parsing can also be done in one python line 
        # although I think that this is less readable
        file.seek(0)
        alt_list = [[line.strip().split(' ')[0], int(line.strip().split(' ')[1])] for line in file]

        # Another parsing suggestion from a colleague
        alt_list2 = [[opcode, int(argv)] for opcode, argv in [line.split() for line in open('input.txt', 'r').readlines()]]

        # part 1
        ok = True
        cur_ix = 0
        acc = 0
        ix_visited = [cur_ix]

        while ok:
            next_ix = cur_ix
            if inp_list[cur_ix][0] == 'nop':
                next_ix += 1 
            elif inp_list[cur_ix][0] == 'acc':
                next_ix += 1 
                acc += inp_list[cur_ix][1]
            else:
                next_ix += inp_list[cur_ix][1]

            if next_ix in ix_visited:
                ok = False
            else: 
                ix_visited.append(next_ix)

            cur_ix = next_ix
        print(acc)

        # part 2
        ix_nop = []
        ix_jmp = []

        for ix, elt in enumerate(alt_list):
            if elt[0] == 'nop':
                ix_nop.append(ix)
        for ix, elt in enumerate(alt_list):
            if elt[0] == 'jmp':
                ix_jmp.append(ix)

        for ix in ix_nop:
            inp_list_cp = copy.deepcopy(alt_list)
            inp_list_cp[ix][0] = 'jmp'
            go_through(inp_list_cp)
        for ix in ix_jmp:
            inp_list_cp = copy.deepcopy(alt_list)
            inp_list_cp[ix][0] = 'nop'
            go_through(inp_list_cp)


if __name__ == '__main__':
    main()
