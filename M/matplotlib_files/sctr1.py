import matplotlib.pyplot as plt
import numpy as np

x=np.random.randint(0,100,size=(100,))
y=np.random.randint(0,100,size=(100,))
size=range(0,100)
clr=['r','c','k','g']*25  #no of colors must be same as the size
plt.scatter(x,y,s=size,c=clr)
plt.show()
