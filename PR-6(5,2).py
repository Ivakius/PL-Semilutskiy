x=[11, 25, 50, 67, 25, 11, 70, 46, 67, 87]
y=[]
for a in x:
    if a not in y:
        y.append(a)
print(y)