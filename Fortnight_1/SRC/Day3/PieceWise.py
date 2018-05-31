"""
Author: Jashan
Date: 2018-May-31
Git: github.com/jashangunike

Piecewise function evaluation
		3x - 5	(x > 1)
f(x) =	x + 2	(-1 <= x <= 1)
		5x + 3	(x < -1)
"""

x = float(input('x = '))
if x>1 :
    y = 3*x - 5
elif x >= -1 :
    y = x + 2
else:
    y = 5 * x + 3
print('You Enter ( % .2f ) = % .2f '%( x, y) )