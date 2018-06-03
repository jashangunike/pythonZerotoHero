"""
Author: Jashan
Date: 2018-Jun-02
Git: github.com/jashangunike

Outputs prime numbers between 2 and 99

"""
import math

for num in range(2,100) :
    Is_prime = True
    for factor in range (2, int(math.sqrt(num))+1) :
        if num % 2 ==0 :
            Is_prime = False
            break
if Is_prime :
    print(num,end=' ')
