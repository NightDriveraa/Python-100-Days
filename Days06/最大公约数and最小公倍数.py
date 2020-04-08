def gcd(x,y):
    if y>x:
        x,y = y,x
    for factor in range(y,0,-1):
        if y%factor==0 and x%factor==0:
            return factor

def lcm(x,y):
    return  x*y//gcd(x,y)

x = int(input('x '))
y = int(input('y '))
print(gcd(x,y))