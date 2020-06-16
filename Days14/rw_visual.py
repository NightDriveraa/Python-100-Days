import matplotlib.pyplot as plt
from randow_walk import RandomWalk

while True:
    #创建漫步实例，且传入漫步值50000
    rw = RandomWalk(50000)
    #开始漫步
    rw.fill_walk()

    #调整图表窗口大小
    plt.figure(figsize=(10, 6))

    #将漫步的第一个点和最后一个点突出显示
    plt.scatter(0,0,c='green',s=150)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',s=150)

    #记录漫步顺序，并按漫步的先后，使漫步点颜色渐变显示
    point_numbers = range(rw.num_points)
    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,s=15)

    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    #询问是否进行下一次漫步
    keep_runing = input('Make another walk?(y/n): ')
    if keep_runing == 'n':
        break