#3.write a python pgm to check whether a given key already exist in dictionary
#dictnry={"name","age"}


dict1={"name":"gokul","age":21}
key=input("enter key to check: ")
if key in dict1:
  print("key exist in dictionary")
else:
  print("key not present")
