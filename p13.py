#write a program to display the first n numbers of the Fibonacci series
n=int(input("enter limit "))
a=0
b=1
while a <= n:
  print(a)
  c=a+b
  a=b
  b=c
