"""
Author: Jashan
Date: 2018-May-31
Git: github.com/jashangunike

Use a for loop to achieve 1~100 summation

"""

sum = 0
for x in range(1, 101) :
    if x% 2 == 0 : # in range between 1 to 100 which equal to zero
        sum += x   # Sum+x 
print(sum)