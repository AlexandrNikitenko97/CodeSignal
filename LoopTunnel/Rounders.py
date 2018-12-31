"""
We want to turn the given integer into a number that has only one non-zero digit using a tail rounding approach. 
This means that at each step we take the last non 0 digit of the number and round it to 0 or to 10. If it's less than 5 we 
round it to 0 if it's larger than or equal to 5 we round it to 10 (rounding to 10 means increasing the next significant
digit by 1). The process stops immediately once there is only one non-zero digit left.

Example

    For n = 15, the output should be
    rounders(n) = 20;

    For n = 1234, the output should be
    rounders(n) = 1000.

    1234 -> 1230 -> 1200 -> 1000.

    For n = 1445, the output should be
    rounders(n) = 2000.

    1445 -> 1450 -> 1500 -> 2000.
"""

def rounders(n):
    chars   = [i for i in str(n)[::-1]]
    rounded = []
    for i in range(len(chars)-1):
        if int(chars[i]) < 5:
            rounded.append('0')
        else:
            rounded.append('0')
            chars[i+1] = str(int(chars[i+1]) + 1)
        if i == len(chars)-2:
            rounded.append(chars[i+1])
    return int(''.join(rounded[::-1])) if len(str(n)) >= 2 else n
