def feobi(n):
    if n==1 or n==2:
        return 1
    else:
        return (feobi(n-1))+(feobi(n-2))
    
    
print(feobi(3))    
print(feobi(5))
print(feobi(6))
print(feobi(7))
print(feobi(30))
