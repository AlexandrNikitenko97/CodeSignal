"""
A little boy is studying arithmetics. He has just learned how to add two integers, written one below another, column by column. But he always forgets about the important part - carrying.

Given two integers, find the result which the little boy will get.

Note: the boy used this site as the source of knowledge, feel free to check it out too if you are not familiar with 
column addition.

Example

For param1 = 456 and param2 = 1734, the output should be
additionWithoutCarrying(param1, param2) = 1180.

   456
  1734
+ ____
  1180

The little boy goes from right to left:

    6 + 4 = 10 but the little boy forgets about 1 and just writes down 0 in the last column
    5 + 3 = 8
    4 + 7 = 11 but the little boy forgets about the leading 1 and just writes down 1 under 4 and 7.
    There is no digit in the first number corresponding to the leading digit of the second one, so the little boy 
    imagines that 0 is written before 456. Thus, he gets 0 + 1 = 1.
"""

def additionWithoutCarrying(param1, param2):
    resultNumber = []
    
    param1 = [i for i in str(param1)][::-1]
    param2 = [i for i in str(param2)][::-1]
    
    ln = len(param1) if len(param1) >= len(param2) else len(param2)
    
    for i in range(ln):
        try:
            p1 = int(param1[i])
        except IndexError:
            p1 = 0
        try:
            p2 = int(param2[i])
        except IndexError:
            p2 = 0

        adding = str(p1 + p2)
        if len(adding) == 2:
            resultNumber.append(adding[1])
        else:
            resultNumber.append(adding)
    return int(''.join(resultNumber[::-1]))
            
        
