#Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already #ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged. 
str1=input("enter string ")
if len(str1)<3:
  print(str1)
elif str1[-3:]=="ing":
  str1=str1+"ly"
  print(str1)
else:
  str1=str1+"ing"
  print(str1)
  
