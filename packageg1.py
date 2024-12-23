"""
Create a package graphics with modules rectangle, circle and sub-package 3D-graphics with modules cuboid and sphere. Include methods to find area and perimeter of respective figures in each module. Write programs that finds area and perimeter of figures by different importing statements. (Include selective import of modules and import * statements)
"""
from graphics import rectangle,circle
from graphics.threeD import cuboid,sphere
length=int(input("enter length of rectangle: "))
width=int(input("enter width of rectangle: "))
#rectangle module
print("area of rectangle= ",rectangle.area(length,width))
print("perimeter of rectangle= ",rectangle.perimeter(length,width))
print()
radius=int(input("enter radius of circle: "))
#circle module
print("area of circle= ",circle.area(radius))
print("perimeter of circle= ",circle.perimeter(radius))
print()
clength=int(input("enter length of cuboid: "))
cwidth=int(input("enter width of cuboid: "))
cheight=int(input("enter height of cuboid: "))
#cuboid module
print("area of cuboid= ",cuboid.surfacearea(clength,cwidth,cheight))
print("volume of cuboid= ",cuboid.volume(clength,cwidth,cheight))
print()
sradius=int(input("enter radius of sphere: "))
#sphere module
print("area of sphere= ",sphere.surfacearea(sradius))
print("volume of sphere= ",sphere.volume(sradius))

