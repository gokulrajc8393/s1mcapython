#(C02) 10.Generate all factors of a number.

def factors(a):
	for i in range(1,a+1):
		if a%i == 0:
			print(i)
	
	
a=int(input("Enter a number :"))
factors(a)