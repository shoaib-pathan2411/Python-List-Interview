def merge_lists(lst1, lst2):
    # result = lst1 + lst2
    # return result
    lst1.extend(lst2)
    return lst1
print(merge_lists([1,2,3], [4,5,6]))