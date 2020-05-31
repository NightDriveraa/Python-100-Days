class Car():
    def __init__(self,make,year,model):  #初始化方法
        self.make = make
        self.year = year
        self.model = model
        self.odometer_reading = 0  #加入里程属性，默认值为0

    def get_descriptive_name(self):      #打印实例属性方法
        long_name = str(self.year) + ' ' + str(self.make) + ' ' + str(self.model)
        print(long_name)

    def read_odometer(self):    #打印实例里程方法
        print('odometer='+ str(self.odometer_reading))

    def update_odometer(self,mileage):    #修改实例里程属性方法
        if mileage < self.odometer_reading:   #防止里程数回调
            print('You can\'t roll back an odometer!' )
        else:
            self.odometer_reading = mileage

    def increment_odometer(self,miles):     #增加里程数方法
        if miles > 0:                       #防止增加数为复数/回调里程数
            self.odometer_reading += miles
        else:
            print('You can\'t roll back an odometer!')


my_car = Car('Audi',2016,'A4')  #创建实例
my_car.get_descriptive_name()   #打印实例属性

my_car.odometer_reading = 26    #访问实例直接修改属性
my_car.read_odometer()          #打印里程
my_car.update_odometer(20)      #通过方法修改里程数
my_car.read_odometer()
my_car.increment_odometer(-2)   #递增方法修改里程数
my_car.read_odometer()