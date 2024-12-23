#Form a list of vowels selected from a given word
l=input("enter a word ")
l1=[x for x in l]
print(l1)
print("vowels")
l2=["a","e","i","o","u","A","E","I","O","U"]
l3=[x for x in l1 if x in l2]
print(l3)


