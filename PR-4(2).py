n=int(input('Введите натуральное число '))
sum_f=0
f=1
for i in range (1, n+1):
    f*=i
    sum_f+=f
print(sum_f)