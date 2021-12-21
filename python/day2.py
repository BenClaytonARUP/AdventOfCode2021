import re
import os

def main():

    Part1()
    Part2()


def Part1():

    with open(os.path.join("..", "data", "2.txt"), "r") as f:

        horizontal = 0
        depth = 0

        for line in f:

            if (line[0] == "u"):
                depth -= int(re.sub("[^0-9]", "", line))

            elif (line[0] == "d"):
                depth += int(re.sub("[^0-9]", "", line))

            else:
                horizontal += int(re.sub("[^0-9]", "", line))

        print(depth * horizontal)

    


def Part2():

    with open(os.path.join("..", "data", "2.txt"), "r") as f:

        horizontal = 0
        depth = 0
        aim = 0

        for line in f:

            if (line[0] == "u"):
                aim -= int(re.sub("[^0-9]", "", line))

            elif (line[0] == "d"):
                aim += int(re.sub("[^0-9]", "", line))

            else:
                horizontal += int(re.sub("[^0-9]", "", line))
                depth += aim * int(re.sub("[^0-9]", "", line))

        print(depth * horizontal)


if __name__ == "__main__":
    main()
