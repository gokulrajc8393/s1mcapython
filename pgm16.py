#c01 15 print all color from color list1 not contained in color list2.
#create color list given as user input,use list comprehension

list1=[i for i in input("enter the colors in list1: ").split()]
list2=[i for i in input("enter the colors in list2: ").split()]
result=[i for i in list1 if i not in list2]
print("colors in list1 not in list2 ",result)

