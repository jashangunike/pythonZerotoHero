"""
Author: Jashan
Date: 2018-May-31
Git: github.com/jashangunike

Using a for loop to achieve even sums between 1 and 100

"""

sum = 0
for x in range(2, 101, 2):  #Range between 2 to 100 and taken Even value
	sum += x

print(sum)
