import re
import os
import numpy as np

def main():    

    with open(os.path.join("..", "data", "8.txt"), "r") as f:

        data = []

        for i, line in enumerate(f):
            lineData = [k.strip() for k in line.split('|')]
            data.append(dict())
            data[i]['input'] = [set(k) for k in lineData[0].split(' ')]
            data[i]['output'] = [set(k) for k in lineData[1].split(' ')]

    Part1(data)
    Part2(data)
    
def Part1(data):

    counter = 0

    for i in range(len(data)):
        for digit in data[i]['output']:
            if (len(digit) in [2, 4, 3, 7]):
                counter += 1

    print(counter)

def Part2(data):

    sumDigits = 0

    for line in data:

        digits = [set() for i in range(10)]
        digitsOut = []

        # Get the easy digits 
        for input in line['input']:

            # 1
            if len(input) == 2:
                digits[1] = set([c for c in input])

            # 4
            elif len(input) == 4:
                digits[4] = set([c for c in input])

            # 7
            elif len(input) == 3:
                digits[7] = set([c for c in input])

            # 8
            elif len(input) == 7:
                digits[8] = set([c for c in input])

        # Infer the hard digits
        for input in line['input']:
        
            # 0, 6, 9
            if len(input) == 6:

                s = set([c for c in input])

                # 9
                if (len(s.intersection(digits[4])) == 4):
                    digits[9] = s

                # 6
                elif (len(s.intersection(digits[7])) == 2):
                    digits[6] = s

                # 0
                elif (len(s.intersection(digits[7])) == 3):
                    digits[0] = s

            
            # 2, 3, 5
            if len(input) == 5:

                s = set([c for c in input])

                # 3
                if (len(s.intersection(digits[1])) == 2):
                    digits[3] = s

                # 2
                elif (len(s.intersection(digits[4])) == 2):
                    digits[2] = s

                # 5
                elif (len(s.intersection(digits[4])) == 3):
                    digits[5] = s

        for output in line['output']:

            for i in range(len(digits)):

                if output == digits[i]:
                    digitsOut.append(str(i))

        sumDigits += int(''.join(digitsOut))

    print(sumDigits)


if __name__ == "__main__":
    main()