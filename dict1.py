dict1={
"name":"gokul","age":21,"class":"mca"
}
print(dict1)
print(len(dict1))
print(dict1["class"])
x = dict1.get("age")
print(x)
y=dict1.keys()
print(y)
dict1["ug"]="bca"
print(dict1)
dict2=dict(name = "John", age = 36, country = "Norway")
print(dict2)
dict1.update({"age":22})
print(dict1)
