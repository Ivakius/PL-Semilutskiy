#Дана действительная матрица размером n х m, все элементы которой различны. В каждой строке выбирается элемент с наименьшим значением. Если число четное, то заменяется нулем, нечетное - единицей. Вывести на экран новую матрицу.
matrix=[]
new_matrix=[]
matrix = [
    [3.2, 1.5, 4.0, 2.8],
    [8.1, 6, 7.6, 6.2],
    [9.0, 0.9, 3.3, 1.1]
]
for row in matrix:
    min_value = min(row)
    if min_value%2==0:  
        min_value=0
    else:  
        min_value=1
    new_row=[min_value if value == min(row) else value for value in row]
    new_matrix.append(new_row)
for row in new_matrix:
    print(row)