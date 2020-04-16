def main():
    try:
        with open('1.jpeg','rb') as fs1:
            data = fs1.read()
            print(type(data))
        with open('2.jpeg','wb') as fs2:
            fs2.write(data)
    except FileNotFoundError:
        print('找不到指定文件')
    except IOError as e:
        print('读写文件时出现错误')
    print('操作完成')

if __name__ == '__main__':
    main()