#(C01) 3.(a).Generate positive list of numbers from a given list of integers.

l=input("enter list of integers seperated by spaces ")
l1=[int(num) for num in l.split()]
pl=[num for num in l1 if num>0]
print("list of positive numbers are ",pl)
