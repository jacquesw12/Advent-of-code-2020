#!/usr/bin/env python3

import numpy as np
import itertools
import copy

def create_matrix(file, mat):
  # 0 floor
  # 1 empty
  # 2 occupied
  file.seek(0)
  for ix_line,line in enumerate(file):
    for ix_col,char in enumerate(line):
      if char == '.':
        mat[ix_line, ix_col] = 0
      if char == 'L':
        mat[ix_line, ix_col] = 1

def init_matrix(file):
  nb_lines = 0
  nb_columns = 0
  for line in file:
    nb_lines += 1
  file.seek(0)
  for line in file.readlines():
    line = line.strip()
    for char in line:
      nb_columns += 1
    break
  return np.empty((nb_lines, nb_columns,)), nb_lines, nb_columns

def is_on_board(neighbour, nb_lines, nb_columns):
    x = neighbour[0]
    y = neighbour[1]
    #print(f'x {x} y {y}')
    if x < 0 or x > nb_lines - 1:
        return False
    if y < 0 or y > nb_columns - 1:
        return False
    return True

def amount_occupied_neighbours(x, y, mat, nb_lines, nb_columns):
    neighbours = [(x+1, y+1), (x+1, y), (x+1, y-1), (x, y+1), (x, y-1), (x-1, y+1), (x-1, y), (x-1, y-1)]
    count_occ = 0
    for neighbour in neighbours:
        if not is_on_board(neighbour, nb_lines, nb_columns):
            continue
        else:
            if mat[neighbour[0]][neighbour[1]] == 2:
                count_occ += 1
    return count_occ

def is_occupied_in_dir(x, y, direction, mat, nb_lines, nb_columns):
    if not is_on_board((x,y), nb_lines, nb_columns):
        return False 
 
    if mat[x][y] == 0:
        return is_occupied_in_dir(x+direction[0], y+direction[1], direction, mat, nb_lines, nb_columns)
    elif mat[x][y] == 1:
        return False
    else:
        return True


def amount_occupied_dir(x, y, mat, nb_lines, nb_columns):
    directions = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
    count_occ = 0
    for direction in directions:
        if is_occupied_in_dir(x+direction[0], y+direction[1], direction, mat, nb_lines, nb_columns):
            count_occ += 1

    return count_occ

def main():
    with open('input.txt', 'r') as file:
        mat, nb_lines, nb_columns = init_matrix(file)
        create_matrix(file, mat)
        ok = True
        while ok:
            mat_bef = copy.deepcopy(mat)
            for x, y in itertools.product(range(nb_lines), range(nb_columns)):
                occ_neighbours = amount_occupied_neighbours(x, y, mat_bef, nb_lines, nb_columns)
                if mat_bef[x][y] == 1 and occ_neighbours == 0:
                    mat[x][y] = 2
                if mat_bef[x][y] == 2 and occ_neighbours >= 4:
                    mat[x][y] = 1
            if np.array_equal(mat, mat_bef):
                ok = False
            # print(mat)
            # print('\n')
        print(f'Result part 1 : {np.count_nonzero(mat == 2)}')

        # part 2
        file.seek(0)
        mat2, nb_lines, nb_columns = init_matrix(file)
        create_matrix(file, mat2)
        # print(mat2)
        ok = True
        while ok:
            mat_bef = copy.deepcopy(mat2)
            for x, y in itertools.product(range(nb_lines), range(nb_columns)):
                occ_neighbours = amount_occupied_dir(x, y, mat_bef, nb_lines, nb_columns)
                if mat_bef[x][y] == 1 and occ_neighbours == 0:
                    mat2[x][y] = 2
                if mat_bef[x][y] == 2 and occ_neighbours >= 5:
                    mat2[x][y] = 1
            if np.array_equal(mat2, mat_bef):
                ok = False
            # print(mat2)
            # print('\n')
        print(f'Result part 2 : {np.count_nonzero(mat2 == 2)}')


if __name__ == '__main__':
    main()
