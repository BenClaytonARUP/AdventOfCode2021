import re
import os
import numpy as np

def main():    

    with open(os.path.join("..", "data", "10.txt"), "r") as f:        
        data = []
        for line in f:
            data.append([c for c in line.strip()])

    part_1(data)
    part_2(data)

def part_1(data):

    score = 0
    
    for line in data:

        stack = []

        for item in line:
            if item in ['(', '[', '{', '<']:
                stack.append(item)
            else:
                if stack[len(stack) - 1] == '(' and item == ')':
                    del stack[-1]
                elif stack[len(stack) - 1] == '[' and item == ']':
                    del stack[-1]
                elif stack[len(stack) - 1] == '{' and item == '}':
                    del stack[-1]
                elif stack[len(stack) - 1] == '<' and item == '>':
                    del stack[-1]
                else:
                    score += calc_score(item)
                    break
            

    print (score)

def part_2(data):
    
    scores = []
    
    for i, line in enumerate(data):

        stack = []
        corrupt = False

        for item in line:
            if item in ['(', '[', '{', '<']:
                stack.append(item)
            else:
                if stack[len(stack) - 1] == '(' and item == ')':
                    del stack[-1]
                elif stack[len(stack) - 1] == '[' and item == ']':
                    del stack[-1]
                elif stack[len(stack) - 1] == '{' and item == '}':
                    del stack[-1]
                elif stack[len(stack) - 1] == '<' and item == '>':
                    del stack[-1]
                else:
                    corrupt = True
                    break
        
        if (not corrupt):     
            if len(stack) > 0:
                scores.append(calc_score_part2(stack))
                
    scores.sort()
    print(scores[int(0.5 * (len(scores) - 1))])

    
    

def calc_score_part2(stack):
    score = 0
    for b in reversed(stack):
        score *= 5        
        if b == '(':
            score += 1
        elif b == '[':
            score += 2
        elif b == '{':
            score += 3
        elif b == '<':
            score += 4

    return score
                

def calc_score(item):
    if item == ')':
        return 3
    if item == ']':
        return 57   
    if item == '}':
        return 1197    
    if item == '>':
        return 25137     




if __name__ == "__main__":
    main()