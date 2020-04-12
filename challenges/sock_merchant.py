#!/bin/python3

import math
import random

# Hackerrank SockMerchant problem
def sockMerchant(n, ar):
    counted = []
    pairs = 0
    for i in ar:
        if i not in counted:
            c = ar.count(i)
            pairs += c // 2
            counted.append(i)
    return pairs

if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    print(result)
