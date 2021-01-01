#!/usr/bin/env python3

def check_password_part1(min_, max_, char, password):
    amount_char_in_pwd = 0
    for cur_char in password:
        if cur_char == char:
            amount_char_in_pwd += 1
    if amount_char_in_pwd >= min_ and amount_char_in_pwd <= max_:
        return True
    else:
        return False

def check_password_part2(pos1, pos2, char, password):
    char1 = password[pos1-1]
    char2 = password[pos2-1]
    if char1 == char and char2 == char:
        return False
    elif char1 == char or char2 == char:
        return True
    else:
        return False 

def main():
    valid_passwords_part1 = 0
    valid_passwords_part2 = 0
    with open('input.txt', 'r') as file:
        for line in file:
            amount, char, password = line.replace(':','').strip().split(' ')
            min_, max_ = amount.split('-')
            if check_password_part1(int(min_), int(max_), char, password):
                valid_passwords_part1 += 1
            if check_password_part2(int(min_), int(max_), char, password):
                valid_passwords_part2 += 1

    print(f'Valid passwords part 1 : {valid_passwords_part1}')
    print(f'Valid passwords part 2 : {valid_passwords_part2}')

if __name__ == '__main__':
    main()
