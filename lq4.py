#4.create dictionary of 5 countries and their capitals.write a fnct to take country and return its capital

dict1={"Russia":"Moscow","United Kingdom":"London","Germany":"Berlin","Spain":"Madrid","Ukraine":"Kiev"}
print(dict1.keys())
c=input("Enter a country from the given dictionary:")
if c in dict1:
  cap= dict1[c]
  print(cap)
else:
  print("not found")



