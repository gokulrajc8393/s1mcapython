#(C01) 15.Print out all colors from color-list1 not contained in color-list2.

list1=[i for i in input("enter the colors in list1: ").split()]
list2=[i for i in input("enter the colors in list2: ").split()]
result=[i for i in list1 if i not in list2]
print("colors in list1 not in list2 ",result)

