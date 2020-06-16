#choice()函数，传入一个列表，将返回列表中的随机一项
from random import choice

#创建随机漫步类
class RandomWalk():
    #初始化，传入属性num_points以调整漫步次数，默认漫步5000次
    def __init__(self,num_points=5000):
        self.num_points = num_points
        #创建属性x_values/y_values，储存随机漫步值，且默认都为从(0,0)开始漫步
        self.x_values=[0]
        self.y_values=[0]
    #创建方法以随机选择漫步方向以及步长
    def fill_walk(self):
        #检索属性x_values的长度，当漫步次数小于设定的总漫步次数，开始选择方向/步长
        while len(self.x_values) < self.num_points:
            #随机选择x轴上的漫步方向，1为向右，-1为向左
            x_direction = choice([1,-1])
            #随机选择x轴上的漫步步长，0即为允许沿y轴的直线漫步
            x_distance = choice([0,1,2,3,4])
            #最后x轴上的漫步即为方向*步长
            x_step = x_direction * x_distance

            #开始y轴上的方向/步长选择
            y_direction = choice([1,-1])
            y_distance  = choice([0,1,2,3,4])
            y_step = y_direction * y_distance

            #拒绝原地漫步
            if x_step == 0 and y_step == 0:
                continue

            #记录下一个漫步点，即为当前最后一个漫步点+下一次漫步的方向*步长
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            #将下一个漫步点存入漫步值属性
            self.x_values.append(next_x)
            self.y_values.append(next_y)
