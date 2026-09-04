def are_equal(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    for num in range(len(lst1)):
        if lst1[num] != lst2[num]:
            return False
    return True
print(are_equal([1,2,3,7,4],[1,2,3,8,4]))
print(are_equal([1,2,3,4,5], [1,2,3,4,5]))