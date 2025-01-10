#(C02) 5.Display the given pyramid with step number accepted from user. Eg: N=4
"""
1
2 4
3 6 9
4 8 12 16
"""

for i in range(1,5):
  for j in range(1,i+1):
   print(i*j,end=" ")
  print(" ")
