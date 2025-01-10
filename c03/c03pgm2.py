#(C03)  2.Create a package graphics with modules rectangle, circle and sub-package 3D-graphics with modules cuboid and sphere. Include methods to find area and perimeter of respective figures in each module. Write programs that finds area and perimeter of figures by different importing statements. (Include selective import of modules and import * statements)

from graphics import rectangle,circle
from graphics.threeD import cuboid,sphere
length=5
width=3
radius=10
height=6
#rectangle module
print("area of rectangle= ",rectangle.area(length,width))
print("perimeter of rectangle= ",rectangle.perimeter(length,width))
#circle module
print("area of circle= ",circle.area(radius))
print("perimeter of circle= ",circle.perimeter(radius))
#cuboid module
print("area of cuboid= ",cuboid.surfacearea(length,width,height))
print("volume of cuboid= ",cuboid.volume(length,width,height))
#sphere module
print("area of sphere= ",sphere.surfacearea(radius))
print("volume of sphere= ",sphere.volume(radius))
