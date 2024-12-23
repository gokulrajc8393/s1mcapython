#CO5
#DATE:28/11/24
#3.write a program to read each row from the csv file and print a list of strings
import csv
with open("student.csv",mode="r") as file:
  csvr=csv.reader(file)
  print("all rows")
  for row in csvr:
    print(row)
  print()
  a=int(input("enter column:"))
  file.seek(0)
  print("particular column")
  for x in csvr:
    print(x[a])

