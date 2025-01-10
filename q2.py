#Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between #them.

fname=input("enter first name: ")
lname=input("enter last name: ")
l1=[x for x in fname]
l2=[y for y in lname]
n=len(l1)
for i in range(n,0,-1):
  print(l1[i],end="")


