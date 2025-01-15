#(C01) 14.accept an integer n and compute n+nn+nnn ,value of n should be less than 10

x=int(input("Enter an Integer : ")) 
n1 = int(f"{x}")  
n2 = int(f"{x}{x}")  
n3 = int(f"{x}{x}{x}")  
print(n1,"+",n2,"+",n3," = ",n1+n2+n3)