#6.create two dictionary .write pgm that replace values in first dictioanry with values from second dictioanry

dict1={"name":"gokul","age":21,"course":"mca"}
dict2={"name":"basil","age":21,"course":"bca"}
dict1['name']=dict2['name']
dict1['age']=dict2['age']
dict1['course']=dict2['course']
print(dict1)
