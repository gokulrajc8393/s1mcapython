#(C02) 9. Construct following pattern using nested loop
"""
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""


for i in range(5):
    for j in range(i + 1):
        print("*", end=" ")
    print()

for i in range(5):
    for j in range(5-i-1):
        print("*", end=" ")
    print()