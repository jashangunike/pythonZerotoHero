"""
Author: Jashan
Date: 2018-May-31
Git: github.com/jashangunike

Enter a non-negative integer n to calculate n!

"""

n = int(input('n = '))          # Enter the Positive value
result = 1
for x in range(1, n + 1):
	result *= x             #result*x = result
print('%d! = %d' % (n, result))
