#accept an integer n and compute n+nn+nnn ,value of n should be less than 10
n=int(input("enter value of n "))
if n < 10:
  print("n+nn+nnn= ",n+(n*n)+(n*n*n))
else:
  print("n must be less than 10")
  
