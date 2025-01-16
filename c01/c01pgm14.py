#(C01) 14.accept an integer n and compute n+nn+nnn ,value of n should be less than 10

x = int(input("Enter an Integer: "))

# Check if the input is less than 10
if x < 10:
    n1 = int(f"{x}")  # Represents n
    n2 = int(f"{x}{x}")  # Represents nn
    n3 = int(f"{x}{x}{x}")  # Represents nnn
    print(f"{n1} + {n2} + {n3} = {n1 + n2 + n3}")
else:
    print("The integer should be less than 10.")
