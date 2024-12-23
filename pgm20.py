#20.from a list of integers create a list removing even numbers

ol=[int(i) for i in input("enter the integers ").split()]
print("list before ",ol)
newlist=[i for i in ol if i%2!=0]
print("list after removing even numbers ",newlist)

