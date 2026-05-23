import matplotlib.pyplot as plt
import numpy as np

x=[1,2,3,4,5]
y=[1,2,3,4,5]
plt.plot(x,y,'r*',linestyle='dotted',markersize=20,mec='k',mfc='g') #mec=markeredgecolor, mfc=markerfacecolor
plt.xlabel('students')
plt.ylabel('marks')
plt.show()
