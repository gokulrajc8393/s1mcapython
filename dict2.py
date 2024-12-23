#17.sort a dictionary by keys in ascending and descending order
d={"apple":10,"orange":20,"banana":5,"kiwi":2}
print("dictionary ",d)
aresult=dict(sorted(d.items()))
dresult=dict(sorted(d.items(),reverse=True))
print("dictionary in ascending order ",aresult)
print("dictionary in descending order ",dresult)
