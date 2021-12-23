import re
import os
import numpy as np

def main():    
    
    cavesSet = set()
    with open(os.path.join("..", "data", "12.txt"), "r") as f:
        for line in f:
            for cave in line.strip().split('-'):
                cavesSet.add(cave)
    
    connections = dict()
    for cave in cavesSet:
        connections[cave] = []

    with open(os.path.join("..", "data", "12.txt"), "r") as f:
        for line in f:
            connections[line.strip().split('-')[0]].append(line.strip().split('-')[1])
            connections[line.strip().split('-')[1]].append(line.strip().split('-')[0])

    
    part_1(connections)
    part_2(connections)

def part_1(connections):

    
    paths = set()
    path = 'start' 
    smallCaves = set(['start'])
    current = 'start'
    recursive_cave_check(current, path, smallCaves, paths, connections)

    print(len(paths))


def part_2(connections):

    
    paths = set()
    path = 'start' 
    smallCaves = set(['start'])
    current = 'start'
    recursive_cave_check(current, path, smallCaves, paths, connections, False)

    print(len(paths))


def recursive_cave_check(current, path, smallCaves, paths, connections, smallCave2 = True):

    if current == 'end':
        paths.add(path)
        return

    for option in connections[current]:

        if option == 'start':
            continue

        if option not in smallCaves or smallCave2 == False:

            smallCavesCopy = smallCaves.copy()
            pathCopy = path + ',' + option
            smallCave2Copy = smallCave2

            if len(re.findall("[a-z]", option)) > 0:
                if option in smallCavesCopy:
                    smallCave2Copy = True
                else:                    
                    smallCavesCopy.add(option)

            recursive_cave_check(option, pathCopy, smallCavesCopy, paths, connections, smallCave2Copy)



    


if __name__ == "__main__":
    main()