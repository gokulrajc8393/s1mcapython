#write a pgm to find factorial of a number
n=int(input("enter number "))
fact=1
i=1
while i <= n:
  fact=fact*i
  i=i+1
print("factorial of ",n,"is ",fact)

