#(C05) 5.Write a Python program to write a Python dictionary to a csv file. After writing the CSV file
# read the CSV file and display the content.


dicteg=[{"roll no":11,"name":"gokul","branch":"mca","age":21},
        {"roll no":12,"name":"abhijith","branch":"mca","age":22},
        {"roll no":13,"name":"adwaith","branch":"mca","age":22},
        {"roll no":14,"name":"vishnu","branch":"mca","age":22},
        {"roll no":15,"name":"thomas","branch":"mca","age":22},
        {"roll no":16,"name":"joyal","branch":"mca","age":21}]
field=["roll no","name","branch","age"]
filename="dictegfile.csv"
with open(filename,mode="w") as file:
  writer=csv.DictWriter(file,fieldnames=field)
  writer.writeheader()
  writer.writerows(dicteg)

with open(filename,mode="r") as file:
  csvr=csv.reader(file)
  for x in csvr:
    print(x)





