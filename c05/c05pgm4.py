#(C05) 4.Write a Python program to read specific columns of a given CSV file and print the content of the columns.


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





