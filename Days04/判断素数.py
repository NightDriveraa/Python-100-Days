from math import sqrt
while 1:
    num = int(input('输入数字: '))
    if num == 1:
        continue
    end = int(sqrt(num))   #sqrt函数，用以求数字的平方根
    flag = True
    for x in range(2,end+1):   #对一个数因数分解，得到的两个数P1/P2必定是P1<=sqrt/P2>=sqrt,只要其中一侧不存在，则为素数
        if num%x == 0:
            flag = False
            break
    if flag == False:
        print('合数')
    else:
        print('素数')
