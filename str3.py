#Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is #less than 2, return the empty string instead. 
str1=input("enter string ")
if len(str1)<2:
  print("empty")
else:
  str2=str1[0:2]+str1[-2:]
  print(str2)
