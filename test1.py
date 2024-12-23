class Time:
	def __init__(s,h,m,se):
		s.h=h
		s.m=m
		s.se=se
	def __add__(s,o):
		s.h=s.h+o.h
		s.se=s.se+o.se
		if(s.se > 60):
			s.m=s.m+1
			s.se=s.se-60
		s.m=s.m+o.m
		if(s.m > 60):
			s.h=s.h+1
			s.m=s.m-60
		return s
	def display(s):
		print("Hour is",s.h)
		print("Minute is",s.m)
		print("Second is",s.se)
h=int(input("enter hour : "))
m=int(input("enter minute : "))
se=int(input("enter second : "))
time1= Time(h,m,se)
h=int(input("enter hour : "))
m=int(input("enter minute : "))
se=int(input("enter second : "))
time2= Time(h,m,se)
time3= Time(0,0,0)
time3=time1+time2
time3.display()

