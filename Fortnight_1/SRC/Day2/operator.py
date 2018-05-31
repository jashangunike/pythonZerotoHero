"""
Author: Jashan
Date: 2018-May-30
Git: github.com/jashangunike
"""

a = 5
b = 10
c = 3
d = 4
e = 5
a += b      #a+b 15
a -= c      #a-c 15-3=12
a *= d      #a*d 12*4=48
a /=e       #a/e 48/5=9.6
print("a = ", a)

flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag1
print("flag1 = ", flag1)        #True
print("flag2 = ", flag2)        #False
print("flag3 = ", flag3)        #False (Because here both condition become true)
print("flag4 = ", flag4)        #True
print("flag5 = ", flag5)        #False ( Here real answer is true )
print(flag1 is True)            #True
print(flag2 is not False)       #False