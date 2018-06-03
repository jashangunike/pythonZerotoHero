"""
Author: Jashan
Date: 2018-May-31
Git: github.com/jashangunike

Print a variety of triangular patterns
*
**
***
****
*****


    *
   **
  ***
 ****
*****


    *
   ***
  *****
 *******
*********
"""

row =  int ( input ( ' Please enter the number of rows: ' ))

for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()





