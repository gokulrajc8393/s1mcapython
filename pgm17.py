#create two list of colors list1 with colors red,blue,green,yellow,purple and list2 with colors blue,yellow,pink
#use a set to find colors in list1 that are not in list2

list1=["red","blue","green","yellow","purple"]
list2=["blue","yellow","pink"]
result=set(list1)-set(list2)
print("colors in list1 that are not in list2 ",list(result))
