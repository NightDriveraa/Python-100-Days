x = 0
y = 1
for _ in range(6):
    z = x+y
    print('%d'%z)
    x = y+z
    print('%d'%x)
    y = z+x
    print('%d'%y)


a = 0
b = 1
for _ in range(20):
    a,b = b,a+b
    print(a,end=' ')