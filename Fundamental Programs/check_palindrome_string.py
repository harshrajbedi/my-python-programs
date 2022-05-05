# To check whether the string is palindrome or not

def palin(string):
	strpal = string[::-1]
	return strpal

string = input("Enter the String: ")
result = palin(string)
strpal = 0
if result == string:
	print("True")
else:
	print("False")