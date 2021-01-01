#!/usr/bin/env python3

def contains_shiny(rules, bag):
    if rules[bag][0] == '':
        return False
    if 'shiny gold' in rules[bag]:
        return True
    else:
        res = False
        for elt in rules[bag]:
            res = res or contains_shiny(rules, elt)
        return res

def bag_contains(rules, bag):
    counter = 1 
    if not rules[bag]:
        return counter
    else:
        print(rules[bag])
        for key, value in rules[bag].items():
            counter += value * bag_contains(rules, key)
            print(counter)
        return counter

def line_to_dict_part1(line, rules):
    line = line.replace('.','').replace('bags','').replace('bag','').split('contain')
    containing_bag = line[0].rstrip()
    list_contained_bags = [elt.strip() for elt in line[1].replace('no other', '').split(',')]
    # remove amount
    list_contained = [elt[2:] for elt in list_contained_bags]
    rules[containing_bag] = list_contained
    
def line_to_dict_part2(line, rules):
    line = line.replace('.','').replace('bags','').replace('bag','').split('contain')
    containing_bag = line[0].rstrip()
    list_contained_bags = [elt.strip() for elt in line[1].replace('no other', '').split(',')]

    dict_contained = {elt[2:]: int(elt[0]) for elt in list_contained_bags if elt}
    rules[containing_bag] = dict_contained

def main():
    with open('input.txt', 'r') as file:
        counter = 0
        counter2 = 0
        rules = {}
        rules2 = {}
        for line in file.read().strip().split('\n'):
            line_to_dict_part1(line, rules)
            line_to_dict_part2(line, rules2)

        for bag in list(rules.keys()):
            if contains_shiny(rules, bag):
                counter += 1

        counter2 = bag_contains(rules2,'shiny gold')
        # -1 because the way the function is written, the bag counts itself ...
        print(counter2 - 1)

if __name__ == '__main__':
    main()
