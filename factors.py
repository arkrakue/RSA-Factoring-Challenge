#!/usr/bin/python3

import sys
import math

def factorize(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i, n // i
        return n, 1

if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        for line in f:
            n = int(line.strip())
            p, q = factorize(n)
            print(f'{n}={p}*{q}')
