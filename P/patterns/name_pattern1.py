'''
Structure
ex: omm
o/p-->
a
b
...
o
oa
ob
...
om
oma
omb
...
omm

'''
name1 = input('your name:')
name = name1.replace(' ', '').lower()
l = len(name)
s = 0
for i in range(l+1):
    print(" "*(l-i), name[:i])
