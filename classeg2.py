#create  a class student with attribute number,name,age.create an object student1 of student class.print rollno,name,age
class Student:
  def __init__(self,rollno,name,age):
    self.rollno=rollno
    self.name=name
    self.age=age
rollno=input("enter roll:")
name=input("enter name:")
age=input("enter age:")
student1=Student(rollno,name,age)
print("student details")
print("roll no:",student1.rollno) 
print("name:",student1.name)
print("age:",student1.age)
