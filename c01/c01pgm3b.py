#(C01) 3.(b).Square of N numbers.

l=input("enter list of integers seperated by spaces ")
l1=[int(num) for num in l.split()]
print(l1)
print("square of numbers")
l2=[(num*num) for num in l1]
print(l2)
