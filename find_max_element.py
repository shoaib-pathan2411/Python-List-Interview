def max_num(lst):
    max1 = lst[0]
    for num in lst:
        if num > max1:
            max1 = num
    return max1
print(max_num([1,2,3,45,38]))