import re
import os
import numpy as np

def main():

    Part1()
    Part2()


def Part1():

    lineCount = sum(1 for line in open(os.path.join("..", "data", "3.txt"), "r"))
    with open(os.path.join("..", "data", "3.txt"), "r") as f:
        columnCount = len(f.readline().strip())

    with open(os.path.join("..", "data", "3.txt"), "r") as f:

        data = np.zeros((lineCount, columnCount))

        for i, line in enumerate(f):

            for j, bit in enumerate(re.sub('[^A-Za-z0-9]+', '', line)):

                if (bit == '1'):

                    data[i, j] = 1

        gammaRate = (np.sum(data, axis=0) > data.shape[0] / 2).astype(dtype=int)
        print("Part 1: Gamma")
        print(gammaRate)
        print(BinaryToDecimal(gammaRate))
        epsilonRate = (gammaRate != np.ones((columnCount,))).astype(dtype=int)
        print("Part 1: Epsilon")
        print(epsilonRate)
        print(BinaryToDecimal(epsilonRate))
        print("Part 1: Answer")
        print(BinaryToDecimal(gammaRate) * BinaryToDecimal(epsilonRate), "\n")



def Part2():

    lineCount = sum(1 for line in open(os.path.join("..", "data", "3.txt"), "r"))
    with open(os.path.join("..", "data", "3.txt"), "r") as f:
        columnCount = len(f.readline().strip())

    with open(os.path.join("..", "data", "3.txt"), "r") as f:

        data = np.zeros((lineCount, columnCount))

        for i, line in enumerate(f):

            for j, bit in enumerate(re.sub('[^A-Za-z0-9]+', '', line)):

                if (bit == '1'):

                    data[i, j] = 1

    oxygenRating = FindRating(data.copy(), columnCount, True)
    CO2Rating = FindRating(data.copy(), columnCount, False)
    print("Part 2: Oxygen")
    print(oxygenRating)
    print("Part 2: CO2")
    print(CO2Rating)
    print("Part 2: Answer")
    print(oxygenRating * CO2Rating)

    



def FindRating(data, columnCount, mostCommon = True):

    for i in range(columnCount):

        data = Reduce(data, i, mostCommon)

        if data.shape[0] == 1:

            return BinaryToDecimal(data[0])


        

        
def Reduce(data, index, mostCommon = True):

    if (mostCommon):

        mask = ((np.sum(data[:, index], axis=0) >= data.shape[0] / 2)) == data[:, index]

    else:

        mask = ((np.sum(data[:, index], axis=0) < data.shape[0] / 2)) == data[:, index]

    return data[mask, :]





def BinaryToDecimal(array):

    return array.dot(2**(np.arange(array.size)[::-1]))

        


if __name__ == "__main__":
    main()