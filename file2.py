#CO5 1.Write a Python program to read a file line by line and store it into a list.
#DATE:26/11/24
file=open("text2.txt","r")
l=[i.split() for i in open("text2.txt")]
print(l)

