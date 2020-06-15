import matplotlib.pyplot as plt
x_value = [1,2,3,4,5]
y_value = [1,4,9,16,25]
plt.scatter(x_value,y_value,c='red',edgecolors='black',s = 200)
plt.title('Square Numbers',fontsize=24)
plt.xlabel('Value',fontsize=24)
plt.ylabel('Squares of Value',fontsize=24)
plt.tick_params(axis='both',which='major',labelsize=14)
plt.show()


x_value = list(range(1,1001))
y_value = [x**2 for x in x_value]
plt.scatter(x_value,y_value,c=y_value,cmap=plt.cm.Blues,s=40)
plt.title('Square Numbers',fontsize=24)
plt.xlabel('Value',fontsize=24)
plt.ylabel('Squares of Value',fontsize=24)
plt.axis([0,1100,0,1100000])
plt.show()