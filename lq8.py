#8.create a dictionary by extracting keys from given dictioanry
#dictnry={name,age,salary,city}
#keys name,salary

dict1={"name":"gokul","age":21,"salary":45000,"city":"ernakulam"}
dict2={}
dict2['name']=dict1['name']
dict2['salary']=dict1['salary']
dict2['city']=dict1['city']
print(dict2)

