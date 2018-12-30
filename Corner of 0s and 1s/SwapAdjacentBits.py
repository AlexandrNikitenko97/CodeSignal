"""
You're given an arbitrary 32-bit integer n. Take its binary representation, split bits into it in pairs 
(bit number 0 and 1, bit number 2 and 3, etc.) and swap bits in each pair. Then return the result as a decimal number.

Example

    For n = 13, the output should be
    swapAdjacentBits(n) = 14.

    13 (10) = 1101 (2) ~> {11}{01} (2) ~> 1110 (2) = 14 (10).

    For n = 74, the output should be
    swapAdjacentBits(n) = 133.

    74 (10) = 01001010 (2) ~> {01}{00}{10}{10} (2) ~> 10000101 (2)= 133 (10).
    Note the preceding zero written in front of the initial number: since both numbers are 32-bit integers, 
    they have 32 bits in their binary representation. The preceding zeros in other cases don't matter, so they are omitted. 
    Here, however, it does make a difference.
"""

def swapAdjacentBits(n):
    return ((n & 0xaaaaaaaa) >> 1 | ((n & 0X55555555) << 1) )
