import matplotlib.pyplot as plt
import numpy as np

cities=['delhi','mumbai','bangalore','cuttack']
population1=[2.5,3,4,1]
population2=[2,3.7,3,6]
population3=[1.4,2.8,2,1]
x=np.arange(len(cities))
plt.bar(x-0.3,population1,width=0.3)
plt.bar(cities,population2,width=0.3)
plt.bar(x+0.3,population3,width=0.3)
plt.xlabel('cities')
plt.xlabel('population')
plt.title('multiple bargraph')
plt.grid()
plt.show()
