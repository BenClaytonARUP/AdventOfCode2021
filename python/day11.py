import re
import os
import numpy as np

def main():    

    

    with open(os.path.join("..", "data", "11.txt"), "r") as f:
        rowCount = sum(1 for line in f)

    with open(os.path.join("..", "data", "11.txt"), "r") as f:
        columnCount = sum(1 for n in f.readline().strip())

    data = np.empty((rowCount, columnCount), dtype=int)
    with open(os.path.join("..", "data", "11.txt"), "r") as f:        
        
        for i, line in enumerate(f):
            data[i, :] = np.array([int(c) for c in line.strip()])

    part_1(data.copy())
    part_2(data.copy())

def part_1(data):

    # Wrap data in negative values that won't flash
    dataWrapped = np.zeros((data.shape[0] + 2, data.shape[1] + 2), dtype=int)
    dataWrapped[1:-1, 1:-1] = data
    flashCount = 0


    for step in range(100):

        # Reset wrap
        reset_wrap(dataWrapped)

        # Increase energy level
        dataWrapped += 1

        # Check for flashes
        flashing = True
        while flashing:
            flashing = False
            for i in range(dataWrapped.shape[0]):
                for j in range(dataWrapped.shape[1]):
                    if dataWrapped[i, j] > 9:
                        flash(dataWrapped, i, j)
                        flashCount += 1
                        flashing = True

        # Reset flashed octopus to zero
        dataWrapped[dataWrapped < 0] = 0

    print(flashCount)

def part_2(data):

    # Wrap data in negative values that won't flash
    dataWrapped = np.zeros((data.shape[0] + 2, data.shape[1] + 2), dtype=int)
    dataWrapped[1:-1, 1:-1] = data


    for step in range(10000):

        flashCount = 0

        # Reset wrap
        reset_wrap(dataWrapped)

        # Increase energy level
        dataWrapped += 1

        # Check for flashes
        flashing = True
        while flashing:
            flashing = False
            for i in range(dataWrapped.shape[0]):
                for j in range(dataWrapped.shape[1]):
                    if dataWrapped[i, j] > 9:
                        flash(dataWrapped, i, j)
                        flashCount += 1
                        flashing = True

        # Reset flashed octopus to zero
        dataWrapped[dataWrapped < 0] = 0

        if flashCount == 100:
            print(step + 1)
            break


def flash(dataWrapped, i, j):

    # Set current octopus to negative value such that it won't flash again on this turn
    dataWrapped[i, j] = -(dataWrapped.shape[0] * dataWrapped.shape[1] + 10)

    # Increase adjacent energies
    for n in range(-1, 2):
        for m in range(-1, 2):
            dataWrapped[i + n, j + m] += 1

def reset_wrap(dataWrapped):

    dataWrapped[0, :] = -(dataWrapped.shape[0] * dataWrapped.shape[1] + 10)
    dataWrapped[:, 0] = -(dataWrapped.shape[0] * dataWrapped.shape[1] + 10)
    dataWrapped[dataWrapped.shape[0] - 1, :] = -(dataWrapped.shape[0] * dataWrapped.shape[1] + 10)
    dataWrapped[:, dataWrapped.shape[1] - 1] = -(dataWrapped.shape[0] * dataWrapped.shape[1] + 10)


if __name__ == "__main__":
    main()