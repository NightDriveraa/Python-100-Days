from  math import  sqrt
for num in range(2,101):
    flag = True
    for _ in range(2,int(sqrt(num))+1):
        if num%_ == 0:
            flag = False
            break
    if flag:
        print('%d' % num, end=' ')


