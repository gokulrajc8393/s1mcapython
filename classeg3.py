#CO1 DATE:3/12/24
# 1.Create Rectangle class with attributes length and breadth and methods to find area and perimeter. Compare two Rectangle #objects by their area
class Rectangle:
  def __init__(self,length,breadth):
    self.length=length
    self.breadth=breadth
  def area(self):
    return self.length*self.breadth
  def perimeter(self):
    return 2*(self.length+self.breadth)
l1=int(input("enter length 1:"))
b1=int(input("enter breadth 1:"))
r1=Rectangle(l1,b1)
print("area is:",r1.area())
print("perimeter is:",r1.perimeter())  
l2=int(input("enter length 2:"))
b2=int(input("enter breadth 2:"))
r2=Rectangle(l2,b2)
print("area is:",r2.area())
print("perimeter is:",r2.perimeter())  

if r1.area()>r2.area():
  print("rectangle 1 has bigger area")
elif r1.area()<r2.area():
  print("rectangle 2 has bigger area")
else:
  print("both rectangle have same area")
