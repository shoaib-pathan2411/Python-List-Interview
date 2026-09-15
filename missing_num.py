def find_missing(list1):
    n = len(list1) +1
    total = n * (n + 1) // 2
    actual = 0

    for num in list1:
        actual += num

    return total - actual


print(find_missing([1,2,3,4,7,6,9,8]))