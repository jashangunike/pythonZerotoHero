
"""
Author: Jashan
Date: 2018-Jun-02
Git: github.com/jashangunike


"""

Num =  int ( input ( ' Please enter a positive integer: ' ))
Temp = Num
Num2 =  0
while Temp >  0 :
	Num2 *=  10             #Num2 = 10*Num2
	Num2 += Temp %  10      #Num2 = Temp/10 +Num2
	Temp //=  10            #Temp = Temp//10
if Num == Num2:
	print ( ' %d is the number of palindromes '  % Num)
else :
	print ( ' %d is not a palindrome '  % Num)