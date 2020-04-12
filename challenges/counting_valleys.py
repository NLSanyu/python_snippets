#!/bin/python3

import math

# Hackerrank CountingValleys problem
def countingValleys(n, s):
    i = 0 
    valleys = 0
    level = 0
    for i in s:
        if i == "D":
            level -= 1
        else:
            level += 1
            if level == 0:
                valleys += 1
    return valleys

if __name__ == '__main__':
    n = int(input())
    s = input()
    result = countingValleys(n, s)
    print(result)

