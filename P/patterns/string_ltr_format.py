# program to write a string in v shape
while True:
    x = input('enter text:')
    n = x.replace(' ', '')
    l = len(n)
    s = 0
    
    if len(x) == 1:
        print(0*' ',x)
        
    else:    
        for i in range(l):
            print(i*' ', n[i], (l-2-2*i)*' ', n[l-i-1])
            s += 1
    
            # to stop it from continuing after meeting point
            if l-2-2*i == 0 or l-2-2*i == 1:
                break

        if l % 2 != 0:  # for words with odd no of letters
            print((i+2)*' ', n[l//2])

    while True:
        rep = input('Try once more?(y/n):')
        if rep == 'y':
            break
        if rep == 'n':
            break
        if rep != 'y' or 'n':
            print('invalid entry')
            
    if rep == 'y':
        continue
    if rep == 'n':
        print('thank you')
        break
