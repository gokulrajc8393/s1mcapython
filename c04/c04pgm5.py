#(C04) 5.Create a class Publisher (name). Derive class Book from Publisher with attributes title and author. Derive class Python from #Book with attributes price and no_of_pages. Write a program that displays information about a Python book. Use base class #constructor invocation and method overriding. 


class Publisher:
  def __init__(self,name):
    self.name=name
  def display():
    pass
class Book(Publisher):
  def __init__(self,name,title,author):
    super().__init__(name) #invoking base class constructor here
    self.title=title
    self.author=author
  def display():
    pass
class Python(Book):
  def __init__(self,name,title,author,price,npage):
    super().__init__(name,title,author)  
    self.price=price
    self.npage=npage
  def display(self):
    print("book details")
    print("Title: ",self.title)
    print("Publisher Name: ",self.name)
    print("Author: ",self.author)
    print("Price: ",self.price)
    print("No Of Pages: ",self.npage)

title=input("enter book title: ")
name=input("enter publisher name: ")
author=input("enter author name: ")
price=int(input("enter book price: "))
npage=int(input("enter no of pages: "))

b=Python(title,name,author,price,npage)
b.display()   