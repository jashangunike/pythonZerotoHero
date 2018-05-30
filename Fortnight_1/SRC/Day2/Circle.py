"""
Calculate the perimeter and area of ​​the circle by entering the radius

Author: Jashan
Date: 2018-May-30
Git: github.com/jashangunike
"""

import math                                                         #Pre defined lib

Radius = float(input("Please the enter the radius of circle "))     #user able to enter the value
perimeter = 2 * math.pi * Radius
area = math.pi * Radius * Radius
print('Length : %.2f '% perimeter)                                  #only 2 digit comes after point
print('Area : %.3f ' % area)                                        #only 3 digit comes after point
