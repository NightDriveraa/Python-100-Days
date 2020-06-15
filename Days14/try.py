import matplotlib.pyplot as plt
x_value = [1,2,3,4,5]
y_value = [x**3 for x in x_value]
plt.plot(x_value,y_value,linewidth=5)
plt.title('Cube Numebers',fontsize = 24)
plt.xlabel('Value',fontsize=24)
plt.ylabel('CUbe of Value',fontsize=24)
plt.tick_params(axis='both',labelsize=14)
plt.savefig('Cube_Numbers.png',bbox_inches='tight')

x_value = list(range(1,5001))
y_value = [x**3 for x in x_value]
plt.scatter(x_value,y_value,c=y_value,cmap=plt.cm.Reds,s=40)
plt.title('Cube Numebers',fontsize = 24)
plt.xlabel('Value',fontsize=24)
plt.ylabel('CUbe of Value',fontsize=24)
plt.axis([0,6000,0,135000000000])
plt.savefig('Cube_Numbers(5000).png',bbox_inches='tight')