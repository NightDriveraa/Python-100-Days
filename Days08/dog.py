class dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title()+' is now sitting')
    def roll_over(self):
        print(self.name.title()+' rolled over')


def main():
    olddog = dog('david',16)   #实例惯用为小写
    olddog.sit()        #句点表示法访问属性
    print(str(olddog.name))
    olddog.roll_over()

if __name__ == '__main__':
    main()
