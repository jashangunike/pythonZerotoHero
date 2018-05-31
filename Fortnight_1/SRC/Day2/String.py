"""
Author: Jashan
Date: 2018-May-31
Git: github.com/jashangunike
"""

Str1 = 'Hello World'
print('The Length of string is ' , len(Str1))       # The Length of string is  11
print('The initials of the word: ' , Str1.title())   #The initials of the word:  Hello World
print( ' strings are capitalized: ' , Str1.upper())  #strings are capitalized:  HELLO WORLD
print(' string is not uppercase: ' , Str1.isupper())  # string is not uppercase:  False

#The string is not starting with hello:  False
print('The string is not starting with hello: ' , Str1.startswith( ' hello ' ))

#The string is not ending with hello:  False
print('The string is not ending with hello: ' , Str1.endswith( ' hello ' ))

#The string is not starting with an exclamation point:  False
print ( 'The string is not starting with an exclamation point: ' , Str1.startswith( ' ! ' ))

#string is not an exclamation mark ending:  False
print ( ' string is not an exclamation mark ending: ' , Str1.endswith( ' ! ' ))

str2 =  ' - \ U9A86 \ u660a '
str3 = Str1.title() + '' + str2.lower() #Hello World - \ u9a86 \ u660a
print(str3)

