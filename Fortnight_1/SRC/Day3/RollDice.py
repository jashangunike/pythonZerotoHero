"""
Author: Jashan
Date: 2018-May-31
Git: github.com/jashangunike

Throwing a dice to decide what to do
"""
from random import randint  #Random is function and radiant is module

face =randint (1,6)
if face == 1:
    Result = 'Click Song'
elif face == 2 :
    Result = 'jump dance '
elif face == 3 :
    Result = 'Learn Dog'
elif face == 4:
	Result =  ' do push-ups '
elif face == 5:
	Result =  ' donation password '
else:
	Result =  ' speaking joke '
print(Result)