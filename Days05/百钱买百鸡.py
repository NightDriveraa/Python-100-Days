for x in range(0,34):
    for y in range(0,21):
        z = 100-x-y
        if 3*x + 5*y + z/3 == 100:
            print('母鸡%d只，公鸡%d只，小鸡%d只'%(x,y,z))