#a
def f_a(n):
    if n==1:
        return 1
    
    else:
        return f_a(n-1)*3
    
print(f_a(3))

#b
def f_b(n):
    if n==1:
        return 1
    
    else:
        return f_b(n+1)*(-2)
    
print(f_b(-2))

#c
def f_c(n):
    if n==1:
        return -1
    
    else:
        return f_c(n+1)*(-0.5)
    
print(f_c(-2))

#d
def f_d(n):
    if n==1:
        return 2
    
    else:
        return (f_d(n-1)*(3)*(3)-1)-1
    
print(f_d(2))

#e
def f_e(n):
    if n==1:
        return 3
    
    else:
        return f_e(n+2)*(-4)
    
print(f_e(-1))

#f
def f_f(n):
    if n==1:
        return -3
    
    else:
        return f_f(n+1)*(-2)
    
print(f_f(1))