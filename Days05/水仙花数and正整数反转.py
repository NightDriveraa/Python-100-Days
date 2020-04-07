for num in range(100,1000):
    a = num//100
    b = (num%100)//10
    c = num%10
    if a**3+b**3+c**3 == num:
        print(num,end = '\t')

num = int(input('输入一个正整数： '))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num*10 + num%10
    num //= 10
print(reversed_num)