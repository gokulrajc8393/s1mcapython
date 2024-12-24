#Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters #of each string. 
str1=input("enter string 1 ")
str2=input("enter string 2 ")
str3=str2[0:2]+str1[2:]
str4=str1[0:2]+str2[2:]
print(str3," ",str4)


