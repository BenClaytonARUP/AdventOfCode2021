import re
import os
import numpy as np
from numpy.core.fromnumeric import clip


def main():

    Part1()
    Part2()


def Part1():

    with open(os.path.join("..", "data", "4.txt"), "r") as f:

        # Extract input info

        cards = []
        card = np.zeros((5, 5), dtype=int)

        for i, line in enumerate(f):

            if (i == 0):
                chosenNumbers = [int(j) for j in line.strip().split(",")]
                continue

            if (i == 1):
                continue

            if ((i + 5) % 6 == 0):
                cards.append(card.copy())
                card = np.zeros((5, 5), dtype=int)
                continue

            card[(i-2) % 6, :] = np.array(line.split()).astype(dtype=int)

        cards.append(card.copy())

        # Keep track of numbers crossed off

        track = [np.zeros((5, 5)) for i in range(len(cards))]

    for number in chosenNumbers:
        Turn(track, cards, number)
        (cards, track, score) = CheckWinner(track, cards, number)
        if (score != -1):
            print(score)
            return


def Part2():

    with open(os.path.join("..", "data", "4.txt"), "r") as f:

        # Extract input info

        cards = []
        card = np.zeros((5, 5), dtype=int)

        for i, line in enumerate(f):

            if (i == 0):
                chosenNumbers = [int(j) for j in line.strip().split(",")]
                continue

            if (i == 1):
                continue

            if ((i + 5) % 6 == 0):
                cards.append(card.copy())
                card = np.zeros((5, 5), dtype=int)
                continue

            card[(i-2) % 6, :] = np.array(line.split()).astype(dtype=int)

        cards.append(card.copy())

        # Keep track of numbers crossed off

        track = [np.zeros((5, 5)) for i in range(len(cards))]

   
    for number in chosenNumbers:
        Turn(track, cards, number)
        (cards, track, score) = CheckWinner(track, cards, number)

        if (len(cards) == 0):
            print(score)
            return


def Turn(track, cards, number):

    for i, card in enumerate(cards):

        track[i] += (card == number).astype(dtype=int)


def CheckWinner(track, cards, number):

    score = -1
    i_remove = []

    for i in range(len(track)):

        vertSum = track[i].sum(axis=0)
        if (vertSum.max() == 5):
            score = Score(i, number, track, cards)
            i_remove.append(i)

        horSum = track[i].sum(axis=1)
        if (horSum.max() == 5):
            score = Score(i, number, track, cards)
            i_remove.append(i)

    newCards = []
    newTrack = []
    for i in range(len(cards)):
        if i in i_remove:
            aaa = 1
        if i not in i_remove:
            newCards.append(cards[i])
            newTrack.append(track[i])

    cards = newCards
    track = newTrack

    return (cards, track, score)


def Score(i, number, track, cards):

    cards[i][track[i] == 1] = 0
    score = np.sum(cards[i]) * number

    return score


if __name__ == "__main__":
    main()
