import re
import os
import numpy as np
from numpy.core.fromnumeric import clip


def main():

    Part1()
    Part2()


def Part1():

    lineCount = sum(1 for line in open(os.path.join("..", "data", "5.txt"), "r"))
    
    data = np.zeros((lineCount, 4), dtype=int)

    with open(os.path.join("..", "data", "5.txt"), "r") as f:

        for i, line in enumerate(f):

            data[i, :] = np.array(re.sub(" -> ", ",",line).split(","))

    xLim = data[:, [0, 2]].max()
    yLim = data[:, [1, 3]].max()

    space = np.zeros((xLim + 1, yLim + 1), dtype=int)
    
    for i in range(data.shape[0]):
        
        # Vertical line
        if (data[i, 0] == data[i, 2]):            
            for j in range(min(data[i, 1], data[i, 3]), max(data[i, 1], data[i, 3]) + 1):
                space[data[i, 0], j] += 1

        # Horizontal line
        if (data[i, 1] == data[i, 3]):            
            for j in range(min(data[i, 0], data[i, 2]), max(data[i, 0], data[i, 2]) + 1):
                space[j, data[i, 1]] += 1

    print(np.sum(space >= 2))


def Part2():

    lineCount = sum(1 for line in open(os.path.join("..", "data", "5.txt"), "r"))
    
    data = np.zeros((lineCount, 4), dtype=int)

    with open(os.path.join("..", "data", "5.txt"), "r") as f:

        for i, line in enumerate(f):

            data[i, :] = np.array(re.sub(" -> ", ",",line).split(","))

    xLim = data[:, [0, 2]].max()
    yLim = data[:, [1, 3]].max()

    space = np.zeros((xLim + 1, yLim + 1), dtype=int)
    
    for i in range(data.shape[0]):
        
        # Vertical line
        if (data[i, 0] == data[i, 2]):            
            for j in range(min(data[i, 1], data[i, 3]), max(data[i, 1], data[i, 3]) + 1):
                space[data[i, 0], j] += 1

        # Horizontal line
        elif (data[i, 1] == data[i, 3]):            
            for j in range(min(data[i, 0], data[i, 2]), max(data[i, 0], data[i, 2]) + 1):
                space[j, data[i, 1]] += 1

        # Diagonal line
        else:

            deltaX = data[i, 2] - data[i, 0]
            deltaY = data[i, 3] - data[i, 1]

            if (deltaX > 0 and deltaY > 0):
                for j in range(abs(deltaX) + 1):
                    space[data[i, 0] + j, data[i, 1] + j] += 1            
            
            elif (deltaX < 0 and deltaY > 0):
                for j in range(abs(deltaX) + 1):
                    space[data[i, 0] - j, data[i, 1] + j] += 1

            elif (deltaX < 0 and deltaY < 0):
                for j in range(abs(deltaX) + 1):
                    space[data[i, 0] - j, data[i, 1] - j] += 1

            elif (deltaX > 0 and deltaY < 0):
                for j in range(abs(deltaX) + 1):
                    space[data[i, 0] + j, data[i, 1] - j] += 1
        

    print(np.sum(space >= 2))




if __name__ == "__main__":
    main()
