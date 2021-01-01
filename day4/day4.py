#!/usr/bin/env python3

import re

def read_entries(file):
    list_entries = []
    cur_map = {}
    for line in file:
        if line.strip():
            entries = line.strip().split(' ')
            for entry in entries:
                key, value = entry.split(':')
                cur_map[key] = value
        else:
            list_entries.append(cur_map)
            cur_map = {}
    list_entries.append(cur_map)
    return list_entries

def count_valid_passports(passports):
    count = 0
    for passport in passports:
        if has_required_keys(passport):
            count += 1
    return count

def has_required_keys(passport):
    entry_keys = set(passport.keys())
    mandatory_fields = set(['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'])
    if mandatory_fields.issubset(entry_keys):
        return True
    else:
        return False

# In regex, \d and [0-9] are equivalent
def is_height_valid(hgt):
    if not (re.match(r'\d{3}cm', hgt) or re.match(r'\d{2}in', hgt)):
        return False
    if re.match(r'[0-9]{3}cm', hgt):
        hgtcm = int(hgt[0:3])
        if hgtcm < 150 or hgtcm > 193:
            return False
    if re.match(r'\d{2}in', hgt):
        hgtin = int(hgt[0:2])
        if hgtin < 59 or hgtin > 76:
            return False
    return True

def are_keys_valid(passport):
    byr = int(passport['byr'])
    if byr < 1920 or byr > 2002:
        return False
    iyr = int(passport['iyr'])
    if iyr < 2010 or iyr > 2020:
        return False
    eyr = int(passport['eyr'])
    if eyr < 2020 or eyr > 2030:
        return False
    hgt = passport['hgt']
    if not is_height_valid(hgt):
        return False
    hcl = passport['hcl']
    if not re.match(r'#[\da-f]{6}', hcl):
        return False
    ecl = passport['ecl']
    if not ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    pid = passport['pid']
    if len(pid) != 9 or not pid.isnumeric():
        return False
    return True 

def count_passports_valid_keys(passports):
    count = 0
    for passport in passports:
        if not has_required_keys(passport):
            continue
        if are_keys_valid(passport):
            count += 1
    return count
    
def main():
    with open('input.txt', 'r') as file:
        list_entries = read_entries(file)
        # part 1
        count1 = count_valid_passports(list_entries)
        print(f'Part 1 : {count1} passports are valid.')
        # part 2
        count2 = count_passports_valid_keys(list_entries)
        print(f'Part 2 : {count2} passports are valid.')

if __name__ == '__main__':
    main()
