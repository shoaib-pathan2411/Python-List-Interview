# def find_missing(list1):
#     n = len(list1) + 1
#     total = n * (n + 1) // 2
#     actual = 0

#     for num in list1:
#         actual += num

#     return total - actual
# print(find_missing([1,2,3,4,7,6,9]))

def find_missing_number(lst1):
    n = len(lst1) + 1
    for i in range(1, n + 1):
        if i not in lst1:
            return i

print(find_missing_number([1,2,3,4,7,7,6,9,8]))

def find_missing_number1(lst1):
    smallest = lst1[0]
    largest = lst1[0]
    for num in lst1:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    for i in range(smallest, largest + 1):
        if i not in lst1:
            print(i)

print(find_missing_number1([1,2,4,7,7,6,9,8]))