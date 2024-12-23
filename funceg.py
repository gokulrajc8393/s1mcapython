#write a program to find the factorial of a number using function
def factorial(n):
  result=1
  for i in range(1,n+1):
    result=result*i
  return result
n=int(input("enter a number "))
result=factorial(n)
print("factorial is ",result)
