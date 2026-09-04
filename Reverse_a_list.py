def reverse_list(lst):
    result = []
    for num in range(len(lst)-1,-1,-1):
        result.append(lst[num])

    return result

print(reverse_list([1,2,3,4,5]))