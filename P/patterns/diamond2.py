n=int(input('enter no layers:'))#horizontal layer
for i in range(n+1):
    print((2*(n-i)+1)*' ',i*'*   ')
for i in range(n-1,-1,-1):
    print((2*(n-i)+1)*' ',i*'*   ')
