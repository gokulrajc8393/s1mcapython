#5.Prompt the user for a list of integers. For all values greater than 100, store ‘over’ instead.
u=input("enter list of integers seperated by spaces ")
numbers=u.split()
#numbers=[int(num) for num in u.split()]
result=[]
for num in numbers:
  numbers=int(num)
  if numbers > 100:
    result.append("over")
  else:
    result.append(numbers)
print("new list")
print(result)
