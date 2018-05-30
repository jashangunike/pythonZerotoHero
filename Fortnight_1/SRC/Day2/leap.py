"""
Author: Jashan
Date: 2018-May-30
Git: github.com/jashangunike
"""

Year = int(input("Please Enter Year"))

is_leap = (Year %4 ==0 and Year &100 !=0 or Year%400 ==0)
print(is_leap)



