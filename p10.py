
# Display future leap years from current year to a final year entered by user.


year1=int(input("enter starting year "))
year2=int(input("enter final year "))
for x in range(year1,year2):
  if (x%4==0 and x%100!=0 )or x%400==0:
    print("leap year ",x)

