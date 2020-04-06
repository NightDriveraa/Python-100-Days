x = int(input('第一个数字: '))
y = int(input('第二个数字: '))
if x > y:
    x,y = y,x
for factor in range(x,0,-1):
    if x%factor == 0 and y%factor == 0:
        print('%d和%d的最大公约数是%d'%(x,y,factor))
        print('%d和%d的最小公倍数是%d'%(x,y,x*y//factor))