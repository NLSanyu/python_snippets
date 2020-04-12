#!/bin/python3

import math

# Hackerrank RepeatedString problem
# Not yet complete
def repeatedString(s, n):
    if s == "a":
        return n
    else:
        rep = n // len(s) + 1
        new_s = s * rep
        final_s = new_s[0:n]
        print(final_s.count("a"))
        return final_s.count("a")

if __name__ == '__main__':
    s = input()
    n = int(input())
    result = repeatedString(s, n)