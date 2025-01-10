#2.write a python program to concatenate dictioanry to create a new one
#dictnry1 ={"name","age"}
#dictnry2={"city","gender"}

dict1={"name":"gokul","age":21}
dict2={"city":"ernakulam","gender":"male"}
print(dict1)
print(dict2)
dict1.update(dict2)
print(dict1)
