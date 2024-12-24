#Write a Python program to count the number of characters (character frequency) in a string. 
str1=input("enter string ")
dict1={}
for x in str1:
  keys=dict1.keys()
  if x in keys:
    dict1[x]=dict1[x]+1
  else:
    dict1[x]=1
print(dict1)

