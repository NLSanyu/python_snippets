#!/bin/python3

import math

# Hackerrank JumpingOnClouds problem
def jumpingOnClouds(c):
    i = 0
    jumps = 0
    while i < (len(c) - 1):
        if c[i+1] == 1:
            i += 2
            jumps += 1
        else:
            if (i+2 < len(c)) and (c[i+2] == 0):
                i += 2
                jumps += 1
            else:
                i += 1
                jumps += 1
    return jumps

if __name__ == '__main__':
    n = int(input())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
    print(result)
