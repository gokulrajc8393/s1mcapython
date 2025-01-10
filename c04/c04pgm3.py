#(C04) 3.Create a class Rectangle with private attributes length and width.Overload'<’operator to compare the area of 2 rectangles.


class Rectangle:
  def __init__(self,length,width):
    self.length=length
    self.width=width
  def area(self):
    return self.length*self.width
  def __lt__(self,other): 
    return self.area() < other.area()
l1=int(input("enter length 1:"))
b1=int(input("enter width 1:"))
rectangle1=Rectangle(l1,b1)
l2=int(input("enter length 2:"))
b2=int(input("enter width 2:"))
rectangle2=Rectangle(l2,b2)
if rectangle1 < rectangle2:
  print("area of rectangle1 less than area of rectangle2")
elif rectangle1 > rectangle2:
  print("area of rectangle1 larger than area of rectangle2")
else:
  print("both rectangle have same area")