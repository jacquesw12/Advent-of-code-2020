#!/usr/bin/env python3

import numpy as np

def create_matrix(file, mat):
  file.seek(0)
  for ix_line,line in enumerate(file):
    for ix_col,char in enumerate(line):
      if char == '.':
        mat[ix_line, ix_col] = 0
      if char == '#':
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
  return np.empty((nb_lines, nb_columns,))

def count_trees(mat, slope_x, slope_y):
    cur_line = 0
    count_trees = 0
    while cur_line <  mat.shape[0]:
        if mat[cur_line][(int(slope_y / slope_x * cur_line)) % mat.shape[1]] == 1:
            count_trees += 1
        cur_line += slope_x
    return count_trees

def main():
    with open('input.txt', 'r') as file:
        mat = init_matrix(file)
        print(mat.shape)
        create_matrix(file, mat)

        # part 1
        amount_trees = count_trees(mat, 1, 3)
        print(f'Amount trees part 1 : {amount_trees}')

        # part 2
        answer_part2 = 1
        slopes = [(1,1), (1,3), (1,5), (1,7), (2,1)]
        for slope in slopes:
            print(f'Tackling case x {slope[0]} y {slope[1]}')
            print(f'  Res : {count_trees(mat, slope[0], slope[1])}')
            answer_part2 *= count_trees(mat, slope[0], slope[1])
        print(f'Answer part 2 : {answer_part2}')

if __name__ == '__main__':
    main()
