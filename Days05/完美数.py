for nums in range(1,10001):
    i = 0
    for num in range(nums-1,0,-1):
        if nums%num == 0:
            i += num
    if i == nums:
        print('%d'%nums)


import math

for num in range(1, 10000):
    result = 0
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            result += factor
            if factor > 1 and num // factor != factor:
                result += num // factor
    if result == num:
        print(num)