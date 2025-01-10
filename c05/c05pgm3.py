#(C05) 3.Write a Python program to read each row from a given csv file and print a list of strings.


with open("student.csv",mode="r") as file:
  csvr=csv.reader(file)
  print("all rows")
  for row in csvr:
    print(row)
  print()

