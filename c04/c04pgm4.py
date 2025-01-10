#(C04) 4.Create a class Time with private attributes hour, minute and second. Overload ‘+’ operator to find sum of 2 time.


class Time:
  def __init__(self,hour,minute,second):
    self.hour=hour
    self.minute=minute
    self.second=second
  def __add__(self,other):
    self.hour=self.hour+other.hour
    self.second=self.second+other.second
    if self.second >60:
      self.minute=self.minute+1
      self.second=self.second-60
    self.minute=self.minute+other.minute
    if self.minute >60:
      self.hour=self.hour+1
      self.minute=self.minute-60
    return self
  def display(self):
    print("Hour:",self.hour)
    print("Minute:",self.minute)
    print("Second:",self.second)
h1=int(input("enter hour 1:"))
m1=int(input("enter minute 1:"))
se1=int(input("enter second 1:"))
time1=Time(h1,m1,se1)
h2=int(input("enter hour 2:"))
m2=int(input("enter minute 2:"))
se2=int(input("enter second 2:"))
time2=Time(h2,m2,se2)
time3= Time(0,0,0)
time3=time1+time2
time3.display()