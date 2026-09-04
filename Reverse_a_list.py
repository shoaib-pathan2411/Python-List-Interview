def reverse_list(lst):
    result = []
    for num in range(len(lst)-1,-1,-1):
        result.append(lst[num])

    return result

print(reverse_list([1,2,3,4,5]))

def rev_list(lst):
    return lst[::-1]

print(rev_list([1,2,3,4,5]))

def reverse_list_in_place(lst):
    lst.reverse()
    return lst
print(reverse_list_in_place([1,2,3,4,5]))

def reversed_list(lst):
    return list(reversed(lst))
print(reversed_list([1,2,3,4,5]))