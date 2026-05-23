n=int(input('enter number of layers:'))#horizontal layer

# first n vertical layers
for i in range(n):
    print((n-i)*' ',(2*i+1)*'*')

# next n-1 vertical layers
for i in range(n-2,-1,-1):
    print((n-i)*' ',(2*i+1)*'*')