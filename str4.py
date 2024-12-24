#Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', #except the first char itself. 
str1=input("enter string ")
x=str1[0]
str1=str1.replace(x,"$")
str1=x+str1[1:]
print(str1)
