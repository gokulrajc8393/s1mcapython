#CO5
#DATE:28/11/24
#5.Write a Python program to write a Python dictionary to a csv file. After writing the CSV file
#read the CSV file and display the content.

import csv
dicteg=[{"roll no":101,"name":"gokul","branch":"bca","age":21},
      {"roll no":102,"name":"eldho","branch":"bca","age":21},
      {"roll no":103,"name":"basil","branch":"bca","age":21},
      {"roll no":104,"name":"jerin","branch":"bca","age":21},
      {"roll no":105,"name":"thomas","branch":"bca","age":21},
      {"roll no":106,"name":"vishnu","branch":"bca","age":21}]
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
  
