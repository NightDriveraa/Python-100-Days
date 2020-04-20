import re
def main():
    username = input('请输入用户名： ')
    qq = input('请输入QQ号： ')
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$',username)
    m2 = re.match(r'^[0-9]{4,11}$',qq)
    if not m1:
        print('请输入正确的用户名')
    if not m2:
        print('请输入正确的QQ号码')
    if m1 and m2:
        print('信息有效')

if __name__ == '__main__':
    main()
