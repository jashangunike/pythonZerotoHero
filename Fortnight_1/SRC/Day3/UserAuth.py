"""
Author: Jashan
Date: 2018-May-31
Git: github.com/jashangunike

User authentication

"""

Username =  input ( ' Please enter username: ' )
Password =  input ( ' Please enter the password: ' )

if Username == 'admin' and Password == '123456':
	print ( ' Authentication succeeded! ' )
else:
	print ( ' Authentication failed! ' )