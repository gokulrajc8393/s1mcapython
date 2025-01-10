#(c01) 11.program to find largest among 3 num 

a=int(input("enter num 1 "))
b=int(input("enter num 2 "))
c=int(input("enter num 3 "))
if a > b and a > c:
  print(a ,"is greater")
elif b > a and b > c:
  print(b ,"is greater")
elif c > a and c > b:
  print(c ,"is greater")
else:
  print("all are equal")

