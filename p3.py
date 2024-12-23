#write a pgm to input two integer numbers and find largest among the two
a=int(input("enter num 1 "))
b=int(input("enter num 2 "))
print(a)
print(b)
if a > b:
  print(a, "is greater")
elif a == b:
  print("both are equal")
else:
  print(b, "is greater")


