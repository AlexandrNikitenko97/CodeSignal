"""
Determine if the given number is a power of some non-negative integer.

Example

    For n = 125, the output should be
    isPower(n) = true;
    For n = 72, the output should be
    isPower(n) = false.
"""

from math import sqrt

def isPower(n):
   for i in range(1, int(sqrt(n))+1):
      for j in range(1, int(sqrt(n))+1):
         if pow(i,j) == n:
            return True
   return False
