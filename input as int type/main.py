sum1 = 0
number = int(input())

if number > 0:
    sum1+= number % 10
    print(sum1)
    sum1+= number // 10
    print(sum1)
    
