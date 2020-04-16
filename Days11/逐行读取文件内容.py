from time import sleep
def main():
    with open('致橡树.txt','r',encoding='utf-8') as f:
        for line in f:
            print(line,end=' ')
            sleep(0.5)
    print()

    #更加简约的代码，使用readlines方法
    with open('致橡树.txt','r',encoding='utf-8') as f:
        lines = f.readlines()    #readlines将把内容读取到一个列表容器
        print(lines)

if __name__ == '__main__':
    main()
