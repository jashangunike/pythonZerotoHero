"""
Author: Jashan
Date: 2018-Jun-02
Git: github.com/jashangunike

The definition and use of functions - Calculate the number of combinations C(7,3)


"""

# Encapsulating factorial functions into a function
def  factorial ( n ):
	Result =  1
	for num in  range ( 1 , n +  1 ):
		Result *= num
	return Result


print (factorial( 7 ) // factorial( 3 ) // factorial( 4 ))