def union(lst1, lst2):
    result = []
    for num in lst1 + lst2:
        if num not in result:
            result.append(num)
    return result
print(union([1,2,3], [3,4,5]))