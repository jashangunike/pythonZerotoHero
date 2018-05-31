"""
Author: Jashan
Date: 2018-May-31
Git: github.com/jashangunike

Percentile grades to graded grades
90 points or more --> A
80 minutes to 89 minutes --> B
70 minutes to 79 minutes --> C
60 minutes to 69 minutes --> D
60 points or less --> E

"""

Score =  float ( input ( ' Please enter grade: ' ))
if Score > 90 :         # :) required after condition
    grade = 'A'
elif Score >= 80:       #Elseif
	grade = 'B'
elif Score >= 70:
	grade = 'C'
elif Score >= 60:
	grade = 'D'
else:                   #Else
	grade = 'E'
print ( 'The corresponding level is: ', grade)