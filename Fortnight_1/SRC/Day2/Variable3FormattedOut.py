"""
Author: Jashan
Date: 2018-May-31
Git: github.com/jashangunike

Formatted output
"""

a = int(input('a = '))    #8
b = int(input('b = '))    #8
print('%d + %d = %d' % (a, b, a + b))        #8 + 8 = 16
print('%d - %d = %d' % (a, b, a - b))        #8 - 8 = 0
print('%d * %d = %d' % (a, b, a * b))       #8 * 8 = 64
print('%d / %d = %f' % (a, b, a / b))       #8 / 8 = 1.000000      3 // 9 = 0(if a=3,b=9)
print('%d // %d = %d' % (a, b, a // b))     #8 // 8 = 1
print('%d %% %d = %d' % (a, b, a % b))      #8 % 8 = 0
print('%d ** %d = %d' % (a, b, a ** b))     #8 ** 8 = 16777216
