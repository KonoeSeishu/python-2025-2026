list1 = [30, 12, 5, 11, 1]
def sort(list1):
    for i in range(len(list1)):
        if list1[j] < list1[minimum]:
            minimum = j
    if i != minimum:
        po = list1[i]
        list1[i] = list1[minimum]
        list1[minimum] = po
        
sort(list1)
print(list1)