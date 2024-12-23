"""
create a list with values 3,56,12,98,43,23 
1.write a program to find the largest number in the given list of numbers
2.find the sum of all elements in the list
3.find all even numbers from the given list
4.for all values greater than 50 store over instead
5.find the smallest element in the list
6.reverse the list
7.add the element 500 to the list
8.sort the list
"""
l1=[3,56,12,98,43,23]
print(l1)
print("largest number in list is ",max(l1))
print("sum of elements in list is ",sum(l1))
l2=[x for x in l1 if x%2==0]
print("even numbers are ",l2)
l3=[]
for x in l1:
  if x > 50:
    l3.append("over")
  else:
    l3.append(x)
print("new list")
print(l3)
print("smallest element in list is ",min(l1))
l1.reverse()
print("reversed list is ",l1)
l1.append(500)
print("list after append ",l1)
l1.sort()
print("sorted list ",l1)


