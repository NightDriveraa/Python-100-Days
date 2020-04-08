def is_palindrom(num):
    total = 0
    temp = num
    while temp>0:
        total = total*10 + temp%10
        temp //= 10
    if total == num:
        return True
    else:
        return False

if __name__ == '__main__':
    num = int(input('num '))
    is_palindrom(num)
