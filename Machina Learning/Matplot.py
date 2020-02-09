import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import matplotlib as mpl
# Multi figures
x = np.arange(-3,3,0.01)
#plt.plot(x,norm.pdf(x))
#plt.plot(x,norm.pdf(x,1.0,0.7))

#save ut to a file [keep this line before the plt.show()]
plt.savefig('D:\Python\Pycharm\Machina Learning\myplot.png',format='png')
# adjust the axes

plt.xlim((-5,5))
plt.ylim((0,1.0))
plt.xticks((-5,-4,-3,-2,-1,0,1,2,3,4,5))
# add a grid
plt.grid()
#change line type and colour
plt.plot(x,norm.pdf(x),'b-')
plt.plot(x,norm.pdf(x,1.0,0.7),'r:')
#labeling axes and adding a legend
plt.xlabel('Greeables')
plt.ylabel('Probability')
plt.legend(['Sheetchees','Gacks'],loc=1)
#plt.show()
# Pie chart
values = [12,55,4,35,14]
colors = ['r','g','b','c','m']
explode = [0,0,0,0.2,0]
labels = ['India','united kingdom','united states','China','europe']
plt.pie(values,colors=colors,labels=labels,explode=explode)
plt.title('Student locations')
#plt.show()
#bar chart
plt.bar(range(0,5),values,color=colors)
#plt.show()
#scatter plot
x = np.random.randn(200)
y = np.random.randn(200)
plt.scatter(x,y)
#plt.show()
#Histogram
incomes = np.random.normal(27000,15000,10000)
plt.hist(incomes,100)
#plt.show()
#box & whisker plot
uniformskewed = np.random.rand(100)*100-40
high_outliers = np.random.rand(10)*50+10
low_outliers = np.random.rand(10)*-50-10
data = np.concatenate((uniformskewed, high_outliers, low_outliers))
plt.boxplot(data)
plt.show()