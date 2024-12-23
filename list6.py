"""
7.Enter 2 lists of integers.Check 
        (a) Whether list are of same length 
        (b) whether list sums to same value 
        (c) whether any value occur in both
"""
l=input("enter list1 of integers seperated by spaces ")
l1=[int(num) for num in l.split()]
m=input("enter list2 of integers seperated by spaces ")
l2=[int(num) for num in m.split()]
print(l1)
print(l2)
a=len(l1)
b=len(l2)
if a==b:
  print("list are of same length")
else:
  print("list are not of same length")
c=sum(l1)
d=sum(l2)
if c==d:
  print("sum of list elements same")
else:
  print("sum of list elements not same")
l3=[x for x in l1 if x in l2]
print("value common in both list ",l3)
