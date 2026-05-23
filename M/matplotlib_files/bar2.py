import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

d1={'name':['omm','shakti','arya','satyakam'],'age':[13,14,14,15],'height':[170,172,168,174],'weight':[60,62,65,62]}
df1=pd.DataFrame(d1)

x = np.arange(len(df1['name']))
width = 0.3

# ensure output directory exists (inside the matplotlib_files folder)
script_dir = os.path.dirname(os.path.abspath(__file__))
graphs_dir = os.path.join(script_dir, 'graphs')
os.makedirs(graphs_dir, exist_ok=True)

plt.bar(x - width, df1['age'],  width=width, color='#e25625', label='age')
plt.bar(x,           df1['height'], width=width, color='#100900', label='height')
plt.bar(x + width, df1['weight'], width=width, color='#2596be', label='weight')

# show names at the numeric x positions
plt.xticks(x, df1['name'])

plt.xlabel('studentName')
plt.ylabel('studentData')
plt.legend(loc='upper right') #to show the color code in graph
plt.savefig(os.path.join(graphs_dir, 'fig_6.png'))
plt.show()
