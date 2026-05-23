import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(1,20,300) # takes 300 values betwn 1-20
plt.hist(x,bins=20)
plt.show()