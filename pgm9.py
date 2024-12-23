#write lambda functions to find the sum of three numbers,product of three numbers
s1=lambda a,b,c :a+b+c
p1=lambda a,b,c :a*b*c
a=int(input("enter num 1 "))
b=int(input("enter num 2 "))
c=int(input("enter num 3 "))
print("sum of three numbers= ",s1(a,b,c))
print("product of three numbers= ",p1(a,b,c))
