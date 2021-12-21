import re
import os
import numpy as np


def main():

    Part1()
    Part2()

def Part1():

    with open(os.path.join("..", "data", "6.txt"), "r") as f:
        inputData = [int(i) for i in f.readline().split(",")]

    s = School(inputData)

    for i in range(80):
        s.update()

    print(len(s.schoolFish))

class School:    

    def __init__(self, inputData):
        
        for timerCount in inputData:
            self.schoolFish = []
            self.schoolFish.append(Fish(timerCount))

    def update(self):
        newFish = []
        for fish in self.schoolFish:
            if fish.update():
                newFish.append(Fish(8))
        self.schoolFish += newFish


class Fish:
    
    def __init__(self, timerCount):
        self.timerCount = timerCount

    def update(self):
        if self.timerCount == 0:
            self.timerCount = 6
            return True
        self.timerCount -= 1

def Part2():

    with open(os.path.join("..", "data", "6.txt"), "r") as f:
        inputData = [int(i) for i in f.readline().split(",")]

    data = np.array(inputData)

    for i in range(256):
        print("Day", i+1)
        data = Update(data)

    print(len(data))

    print("HERE")
    quit()

    s2 = School(inputData)

    for i in range(256):
        print("Day", i+1)
        s2.update()

    print(len(s2.schoolFish))


def Update(data):

    zeroFishMask = data == 0
    data[~zeroFishMask] -= 1
    if (zeroFishMask.sum() > 0):
        newFish = np.full((zeroFishMask.sum()), 8)
        data[zeroFishMask] = 6
        data = np.concatenate((data, newFish))

    return data
    



if __name__ == "__main__":
    main()