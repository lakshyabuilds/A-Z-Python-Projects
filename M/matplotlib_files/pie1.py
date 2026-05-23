import matplotlib.pyplot as plt

popl = [1325, 338, 8]
contri = ['India', 'USA', 'Sweden']
clr = ['gold', 'pink', 'black']
xpld = [0.3, 0.3, 0.3]
plt.pie(popl, colors=clr, labels=contri,
        shadow=True, explode=xpld, autopct='%4.1f%%')
plt.title('population in millions')

plt.show()
