from math import sqrt
def is_prime(num):
    flag = 1
    for factor in range(2,int(sqrt(num)+1)):
        if num % factor == 0:
            flag = 0
            break
    if flag == 1:
        return True
    else:
        return False

if __name__ == '__main__':
    num = int(input('num'))
    is_prime(num)