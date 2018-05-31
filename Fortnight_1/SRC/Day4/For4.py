"""
Author: Jashan
Date: 2018-May-31
Git: github.com/jashangunike

Enter a positive integer to determine if it is a prime number

"""
from math import sqrt

n = int(input('Enter Positive number'))
end = int(sqrt(n))
is_prime = True
for x in range(2, end + 1):
	if n % x == 0:
		is_prime = False
		break
if is_prime and n != 1:
	print ( ' %d is a prime '  % n  )
else:
	print ( ' %d is not a prime number '  % n )
