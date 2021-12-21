import os
import re

def main():

    Part1()
    Part2()


def Part1():

    with open(os.path.join("..", "data", "1.txt"), "r") as f:

        previousValue = -1
        countIncrease = -1

        for line in f:
            currentValue = int(re.sub('[^A-Za-z0-9]+', '', line))
            if (currentValue > previousValue):
                countIncrease += 1
            previousValue = currentValue

        print(countIncrease)

def Part2():

    with open(os.path.join("..", "data", "1.txt"), "r") as f:

        lines = f.readlines()

        countIncrease = -1
        
        valueM1 = int(re.sub('[^A-Za-z0-9]+', '', lines[0]))
        valueM2 = int(re.sub('[^A-Za-z0-9]+', '', lines[1]))

        sum3 = -1

        for line in lines[2:]:

            currentValue = int(re.sub('[^A-Za-z0-9]+', '', line))

            if (currentValue + valueM1 + valueM2 > sum3):
                countIncrease += 1
            
            sum3 = currentValue + valueM1 + valueM2

            valueM2 = valueM1
            valueM1 = currentValue


        print(countIncrease)


if __name__ == "__main__":
    main()