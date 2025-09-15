def d(n):
    if n==1:
        return 1
    elif n==2:
        return 5
    
    return d(n-1)-d(n-2)
        
print(d(3))
print(d(4))
