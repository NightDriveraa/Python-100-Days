"""一个可用于表示汽车的类"""

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



class Battery():
    def __init__(self,battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print('This car has a '+str(self.battery_size)+'-KWh battery')

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range) + ' miles on a full charge'
        print(message)

    def update_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85

class ElectricCar(Car):
    def __init__(self,make,year,model):
        super().__init__(make,year,model)
        self.battery = Battery()


my_tesla = ElectricCar('tesla',2016,'Model s')
my_tesla.get_descriptive_name()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.update_battery()
my_tesla.battery.get_range()