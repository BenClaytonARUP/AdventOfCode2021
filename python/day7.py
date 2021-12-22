import re
import os
import numpy as np
from time import time


def main():

    Part1()
    Part2()
    
def Part1():

    with open(os.path.join("..", "data", "7.txt"), "r") as f:
        inputData = [int(i) for i in f.readline().split(",")]

    minFuel = max(inputData) * len(inputData)
    position = -1
    for possiblePosition in range(max(inputData)):
        fuel = 0
        for crab in inputData:
            fuel += abs(crab - possiblePosition)
        if fuel < minFuel:
            minFuel = fuel
            position = possiblePosition

    print(minFuel)
    print(position)
    
def Part2():

    with open(os.path.join("..", "data", "7.txt"), "r") as f:
        inputData = [int(i) for i in f.readline().split(",")]

    minFuel = 0.5 * max(inputData) * (max(inputData) + 1) * len(inputData)
    position = -1
    for possiblePosition in range(max(inputData)):
        fuel = 0
        for crab in inputData:
            distance = abs(crab - possiblePosition)
            # Standard formulae for summation of N
            fuel += distance * (distance + 1) / 2
        if fuel < minFuel:
            minFuel = fuel
            position = possiblePosition

    print(minFuel)
    print(position)


if __name__ == "__main__":
    main()