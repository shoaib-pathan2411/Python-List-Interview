def find_min(lst):
    min1 = lst[0]
    for num in lst:
        if num < min1:
            min1 = num

    return min1
print(find_min([1,2,3,4,5]))