"""
Author: Jashan
Date: 2018-May-31
Git: github.com/jashangunike

Imperial units and metric units cm interchangeable
"""

Value =  float ( input ( ' Please enter the length: ' ))    #4.5        #12
Unit =  input ( ' Please enter the unit: ' )                #in         #cm

if Unit == 'in' or Unit == 'inch' : # (:) required after condition
    print(' %f inch = %f cm ' %(Value,Value*2.54))               # 4.500000 inch = 11.430000 cm
elif Unit =='cm' or Unit == 'cm' :  # (:) required after condition
    print('%f centimeter = %f inch ' %(Value,Value /2.54))        #12.000000 centimeter = 4.724409 inch


else:
    print('Please enter valid unit')