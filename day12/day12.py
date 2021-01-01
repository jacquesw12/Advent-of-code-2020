#!/usr/bin/env python3

import math

DEG2RAD = math.pi / 180

def main():
    with open('input.txt', 'r') as file:
        instructions = file.read().strip().split('\n')
        eastwest = 0
        nordsud = 0
        angle = 90 # starting east, north 0, south 180

        # part 1
        for inst in instructions:
            cat = inst[0]
            val = int(inst[1:])
            if cat == 'N':
                nordsud += val
            if cat == 'S':
                nordsud -= val
            if cat == 'E':
                eastwest += val
            if cat == 'W':
                eastwest -= val
            if cat == 'R':
                angle += val
            if cat == 'L':
                angle -= val
            if cat == 'F':
                if (angle % 360) == 0:
                    nordsud += val
                if (angle % 360) == 90:
                    eastwest += val
                if (angle % 360) == 180:
                    nordsud -= val
                if (angle % 360) == 270:
                    eastwest -= val
        print(f'Part 1 : {abs(eastwest) + abs(nordsud)}')

        # part 2
        nordsud_w = 1
        eastwest_w = 10
        nordsud_s = 0
        eastwest_s = 0

        for inst in instructions:
            cat = inst[0]
            val = int(inst[1:])
            if cat == 'N':
                nordsud_w += val
            if cat == 'S':
                nordsud_w -= val
            if cat == 'E':
                eastwest_w += val
            if cat == 'W':
                eastwest_w -= val
            if cat == 'R':
                cur_nord = nordsud_w
                cur_east = eastwest_w
                if val == 90:
                    nordsud_w = -cur_east
                    eastwest_w = cur_nord
                if val == 180:
                    nordsud_w = -cur_nord
                    eastwest_w = -cur_east
                if val == 270:
                    nordsud_w = cur_east
                    eastwest_w = -cur_nord
            if cat == 'L':
                cur_nord = nordsud_w
                cur_east = eastwest_w
                if val == 90:
                    nordsud_w = cur_east
                    eastwest_w = -cur_nord
                if val == 180:
                    nordsud_w = -cur_nord
                    eastwest_w = -cur_east
                if val == 270:
                    nordsud_w = -cur_east
                    eastwest_w = cur_nord
            if cat == 'F':
                nordsud_s += val * nordsud_w
                eastwest_s += val * eastwest_w
            print(f'Instruction {inst}')
            print(f'  Ship north {nordsud_s}, east {eastwest_s}')
            print(f'  Waypoint north {nordsud_w}, east {eastwest_w}')
        print(f'Part 2 : {abs(eastwest_s) + abs(nordsud_s)}')


if __name__ == '__main__':
    main()
