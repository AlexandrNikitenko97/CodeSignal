"""
Find the number of ways to express n as sum of some (at least two) consecutive positive integers.

Example

    For n = 9, the output should be
    isSumOfConsecutive2(n) = 2.

    There are two ways to represent n = 9: 2 + 3 + 4 = 9 and 4 + 5 = 9.

    For n = 8, the output should be
    isSumOfConsecutive2(n) = 0.

    There are no ways to represent n = 8.
"""

from math import ceil

def isSumOfConsecutive2(n):
    ways = 0
    for i in range(ceil(n/2), 1, -1):
        summa = i
        for j in range(i-1, 0, -1):
            print('j == ', j)
            summa += j
            print(summa)
            if summa > n: break
            if summa < n: continue
            if summa == n: 
                ways += 1
                break
    return ways
