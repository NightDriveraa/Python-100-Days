def main():
    f = None
    try:
        f = open('致橡树.txt','r',encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('找不到指定文件')
    except LookupError:
        print('未知编码')
    except UnicodeDecodeError:
        print('读取文件时解码错误')

    finally:
        if f:
            f.close()

def main2():     #with as 方式
    try:
        with open('致橡树.txt','r',encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
            print('找不到指定文件')
    except LookupError:
        print('未知编码')
    except UnicodeDecodeError:
        print('读取文件时解码错误')


if __name__ == '__main__':
    main2()