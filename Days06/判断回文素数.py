from 判断素数 import is_prime
from 判断回文数 import is_palindrom
num = int(input('num: '))
if is_prime(num) and is_palindrom(num):
    print('Yes')
else:
    print('NO')