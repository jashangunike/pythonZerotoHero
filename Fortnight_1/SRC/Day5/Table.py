"""
Author: Jashan
Date: 2018-Jun-02
Git: github.com/jashangunike

Output Multiplication Table (99 Table)

"""

for i in range(1 , 10) :                            #here row i=1,2,3,4,5,6,7,8,9,10
    for j in range(1, i+1) :                        #here j= 1 to i+1
        print('%d * %d =%d' %(i,j,i*j), end= ' \t')   #logic
        print()                                         #print
