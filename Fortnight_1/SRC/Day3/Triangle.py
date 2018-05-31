"""
Author: Jashan
Date: 2018-May-31
Git: github.com/jashangunike

Judging whether the input side length can form a triangle
If possible, calculate the perimeter and area of ​​the triangle
"""
import math

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a + b > c and a + c > b and b + c > a:
	print ( ' Perimeter: %f '  % (a + b + c))
	p = (a + b + c) / 2
	area = math.sqrt(p * (p - a) * (p - b) * (p - c))
	print ( ' area: %f '  % (area))
else:
	print ( ' cannot form a triangle ' )