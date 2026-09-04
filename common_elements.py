def common_elements(lst1, lst2):
    result = []
    for num in lst1:
        if num in lst2 and num not in result:
            result.append(num)
    return result

print(common_elements([1,2,3,6],[2,3,4,5]))