def remove_duplicates(lst):
    result = []

    for num in lst:
        if num not in result:
            result.append(num)
    return result
print(remove_duplicates([1,2,4,5,24,343,3,23,2,3,]))