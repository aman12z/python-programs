marks ={'me':23,'live':1,'death':0}

print(marks)

s= sorted(marks.items(), key = lambda x : x[1])
print(s)          

# sort only the values
v=sorted(marks.values())
print(v)
