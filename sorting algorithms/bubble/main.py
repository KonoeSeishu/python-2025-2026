n = int(input("Give number of elements:"))
numbers = list(map(int, input("Give numbers to sort").split()))
print(numbers)

def bubble_sort(numbers, n):
    for i in range(n):
        for j in range(1, n-i):
            if numbers[j-1] > numbers[j]:
                numbers[j-1], numbers[j], = numbers[j], numbers[j-1]


bubble_sort(numbers, n)
print(numbers)
            
    