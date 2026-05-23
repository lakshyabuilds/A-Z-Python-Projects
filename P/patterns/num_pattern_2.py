'''
1
1 2
1 2 3
1 2 3 4
'''

for i in range(5):
    num = 1
    for j in range(i+1):
        print(num, end=' ')
        num += 1
    print()  # for new line
