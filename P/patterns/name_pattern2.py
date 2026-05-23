name = input("enter name: ")
l = len(name)

for i in range(l):
    print(' '*(l-i)**2, name[i])
for i in range(l-1,-1,-1):
    print(' '*(l-i)**2, name[i])
