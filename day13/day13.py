#!/usr/bin/env python3

# Brute force solution takes way too long here ...
# But works with examples
def check_schedule_for_timestamp(i, schedule):
    for offset, bus_id in enumerate(schedule):
        if bus_id == 'x':
            continue
        if not (i + ix) % int(bus_id) == 0:
            return False
    return True
            
def main():
    with open('input_ex.txt', 'r') as file:
        
        inp = file.readlines()
        timestamp = int(inp[0].strip())
        schedule_2 = inp[1].strip().split(',')
        schedule_1 = [int(i) for i in schedule_2 if i != 'x']
        schedule_1.sort()

        # part 1
        bus_id = 0
        for i in range(timestamp, timestamp + schedule_1[0]):
            for bus in schedule_1:
                if i % bus == 0:
                    bus_id = bus
                    break
            if bus_id:
                break
        print(f'Solution part 1: {bus_id* (i-timestamp)}')

        # part 2
        print(schedule_2)

        result = 1
        mode = 1
        # Got some help from https://www.reddit.com/r/adventofcode/comments/kc60ri/2020_day_13_can_anyone_give_me_a_hint_for_part_2/
        for offset, bus_id in enumerate(schedule_2):
            if bus_id == 'x':
                continue
            while (result + offset) % int(bus_id) != 0:
                result += mode
            mode *= int(bus_id)
        print(f'Solution part 2: {result}')

        """
        Brute force solution
        ok = True
        i = 0 
        while ok:
            if check_schedule_for_timestamp(i, schedule_2):
                print(f'Solution part 2: {i}')
                break
            i += 1
        """

if __name__ == '__main__':
    main()

