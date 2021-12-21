import re
import os
import numpy as np
from time import time


def main():

    Part1()
    Part2()
    CompareApproaches()

def Part1():

    with open(os.path.join("..", "data", "6.txt"), "r") as f:
        inputData = [int(i) for i in f.readline().split(",")]

    s = School(inputData)

    for i in range(80):
        s.update()

    print(len(s.schoolFish))

def Part2():

    with open(os.path.join("..", "data", "6.txt"), "r") as f:
        inputData = [int(i) for i in f.readline().split(",")]    

    eS = efficientSchool(inputData)

    for i in range(256):
        eS.update()

    print(eS.currentSchool.sum())

def CompareApproaches():    

    with open(os.path.join("..", "data", "6.txt"), "r") as f:
        inputData = [int(i) for i in f.readline().split(",")]    

    N = 10

    # Simple object orientated
    tA1 = time()
    for k in range(N):
        s = School(inputData)
        for i in range(80):
            s.update()
    tA2 = time()
    print(len(s.schoolFish), "TIME: ", tA2 - tA1)

    # numpy
    tB1 = time()
    for k in range(N):
        data = np.array(inputData, dtype=int)
        for i in range(80):
            data = Update(data)
    tB2 = time()
    print(data.shape[0], "TIME: ", tB2 - tB1)

    # efficientSchool
    tC1 = time()
    for k in range(N):
        eS = efficientSchool(inputData)
        for i in range(80):
            eS.update()
    tC2 = time()
    print(eS.currentSchool.sum(), "TIME: ", tC2 - tC1)
    




class School:    

    def __init__(self, inputData):
        self.schoolFish = []
        
        for timerCount in inputData:
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



class efficientSchool:

    def __init__(self, inputData):
        self.currentSchool = np.zeros((9), dtype=np.dtype(np.int64))
        for timerCount in inputData:
            self.currentSchool[timerCount] += 1

    def update(self):
        zeroFish = self.currentSchool[0]
        for i in range(self.currentSchool.shape[0]-1):
            self.currentSchool[i] = self.currentSchool[i+1]
        self.currentSchool[6] += zeroFish
        self.currentSchool[8] = zeroFish
            

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