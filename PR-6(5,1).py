x=[25, 17, -9, 6, -27, -9, 7, 3, -95, -27]
for i in range(len(x)-1):
    if x[i] < 0 and x[i+1] < 0:
        print(x[i], x[i+1])