#CO5 2.Python program to copy odd lines of one file to other
#DATE:26/11/24
f = open("text2.txt", "r")
print(f.read())
f.close()
f = open("text2.txt", "r")
g = open("text3.txt", "w")
h = open("text5.txt", "w")
i=1
for x in f:
  if i % 2!=0:
    g.write(x)
  else:
    h.write(x)
  i=i+1
g.close()
h.close()
f.close()
print("odd lines")
g = open("text3.txt", "r")
print(g.read()) 
g.close()
print("even lines")
h = open("text5.txt", "r")
print(h.read()) 
h.close()

