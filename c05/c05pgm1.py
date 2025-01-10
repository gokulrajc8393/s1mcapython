#(C05) 1.Write a Python program to read a file line by line and store it into a list.

file=open("text2.txt","r")
l=[i.split() for i in open("text2.txt")]
print(l)



