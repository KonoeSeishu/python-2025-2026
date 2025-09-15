def factorial(s):
    if s==0:
        return 1
    else:
        return s*factorial(s-1)
    
    
print(factorial(0))
print(factorial(5))
print(factorial(15))
print(factorial(996))

