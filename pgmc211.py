# c02 11.Write lambda functions to find area of square, rectangle and triangle.
area1=lambda a :a*a
area2=lambda l,b :l*b
area3=lambda b,h :0.5*b*h
s=int(input("enter side of square "))
print("area of square= ",area1(s))
l=int(input("enter length of rectangle "))
b=int(input("enter breadth of rectangle "))
print("area of rectangle= ",area2(l,b))
p=int(input("enter base of triangle "))
h=int(input("enter height of triangle "))
print("area of triangle= ",area3(p,h))
