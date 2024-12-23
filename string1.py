"""
#declare a string welcome to python programming
1.print the string
2.print the length of string
3.declare another string hello concatenate the two string to get output hello welcome to python programming
4.extract the word python from the string
5.replace the first character of the string with $ symbol
6.from the end of string hello display till e
7.display the string python programming from the initial string
8.convert the string to uppercase
9.check whether all the characters in the string are lowercase
10.split the string

"""
s="welcome to python programming"
print(s)
print("length of string ",s,"is ",len(s))
k="hello"
l=k+ " " +s
print(l)
print(s[11:17])
print(s.replace("w", "$"))
print(k[-1:-5:-1])
print(s[11:29])
print(s.upper())
print(s.islower())
print(s.split())
