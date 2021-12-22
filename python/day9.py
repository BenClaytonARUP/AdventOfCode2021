import re
import os
import numpy as np

def main():    

    
    with open(os.path.join("..", "data", "9.txt"), "r") as f:
        rowCount = sum(1 for line in f)
    
    with open(os.path.join("..", "data", "9.txt"), "r") as f:
        columnCount = sum(1 for c in f.readline().strip())
    
    data = np.empty((rowCount, columnCount), dtype=int)
    with open(os.path.join("..", "data", "9.txt"), "r") as f:
        
        for i, line in enumerate(f):
            data[i, :] = np.array([int(c) for c in line.strip()])

    part_1(data)
    part_2(data)

def part_1(data):

    riskLevelSum = 0

    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if data[i, j] < min(adjacent(i, j, data, Explorer())):
                riskLevelSum += data[i, j] + 1

    print(riskLevelSum)


def part_2(data):

    lowPoints = []

    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if data[i, j] < min(adjacent(i, j, data, Explorer())):
                lowPoints.append((i, j))

    basin = set(lowPoints)
    basinSizes = []
    for point in lowPoints:
        basinSizes.append(recursiveCheck(point[0], point[1], data, basin))

    basinSizes.sort(reverse=True)
    print(basinSizes[0] * basinSizes[1] * basinSizes[2])

def recursiveCheck(i, j, data, basin):

    basin.add((i, j))

    e = Explorer()
    adjacent(i, j, data, e)
    if (i-1, j) in basin:
        e.up = True
    if (i+1, j) in basin:
        e.down = True
    if (i, j-1) in basin:
        e.left = True
    if (i, j+1) in basin:
        e.right = True

    if e.explored():
        return 1

    sum = 0
    if e.up == False and (i-1, j) not in basin:
        sum += recursiveCheck(i-1, j, data, basin)
    if e.down == False and (i+1, j) not in basin:
        sum += recursiveCheck(i+1, j, data, basin)
    if e.left == False and (i, j - 1) not in basin:
        sum += recursiveCheck(i, j-1, data, basin)
    if e.right == False and (i, j + 1) not in basin:
        sum += recursiveCheck(i, j+1, data, basin)

    return sum + 1

    

    


def adjacent(i, j, data, e):

    adjacentNumbers = []

    if i == 0:
        adjacentNumbers.append(data[i + 1, j])
    elif i == data.shape[0] - 1:
        adjacentNumbers.append(data[i - 1, j])
    else:
        adjacentNumbers.append(data[i + 1, j])
        adjacentNumbers.append(data[i - 1, j])

    if i == 0:
        e.up = True
    else:
        if data[i - 1, j] == 9:
            e.up = True
    if i == data.shape[0] - 1:
        e.down = True
    else:
        if data[i + 1, j] == 9:
            e.down = True

    if j == 0:
        adjacentNumbers.append(data[i, j + 1])
    elif j == data.shape[1] - 1:
        adjacentNumbers.append(data[i, j - 1])
    else:
        adjacentNumbers.append(data[i, j + 1])
        adjacentNumbers.append(data[i, j - 1])

    if j == 0:
        e.left = True
    else:
        if data[i, j - 1] == 9:
            e.left = True
    if j == data.shape[1] - 1:
        e.right = True
    else:
        if data[i, j + 1] == 9:
            e.right = True

    return adjacentNumbers

class Explorer:

    def __init__(self):
        self.up = False
        self.right = False
        self.down = False
        self.left = False

    def explored(self):
        if self.up == True and self.right == True and self.down == True and self.left == True:
            return True
        else:
            return False



if __name__ == "__main__":
    main()