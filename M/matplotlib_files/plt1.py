import matplotlib.pyplot as plt
import numpy as np

cities=['delhi','mumbai','bangalore','cuttack']
population=[2.5,3,4,1]
plt.bar(cities,population,width=0.3,color=['r','silver','gold','brown'])
plt.plot(cities,population,'ro',linestyle='dashed')
plt.xlabel('cities')
plt.xlabel('population')
plt.show()
