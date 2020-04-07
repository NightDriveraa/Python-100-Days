from  random import  randint
money = 1000
while money > 0:
    needs_go_on = False
    print('你的资产为：%d'%money)
    while True:
        debt = int(input('请下注：'))
        if 0<debt<=money:
            break
    first = randint(1,6)+randint(1,6)
    print('你摇出了%d点'%first)
    if first == 7 or first == 11:
        print('win!')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('lose!')
        money -= debt
    else:
        needs_go_on = True
    while needs_go_on:
        print('继续摇骰子')
        second = randint(1,6)+randint(1,6)
        print('你摇出了%d点'%second)
        if second == first:
            print('win!')
            money += debt
            needs_go_on = False
        elif second == 7:
            print('lose!')
            money -= debt
            needs_go_on = False
print('恭喜破产')