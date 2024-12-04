#Упорядочить по возрастанию элементы каждой строки матрицы размером n х m.
n=3
m=4
A=[]
for i in range(n):
    B=[]
    for j in range(m):
        B.append(int(input()))
    A.append(B)
for row in A:
    row.sort()
    print(row)