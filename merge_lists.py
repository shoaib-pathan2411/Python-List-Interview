def merge_lists(lst1, lst2):
    # result = lst1 + lst2
    # return result
    lst1.extend(lst2)
    return lst1
print(merge_lists([1,2,3], [4,5,6]))

def merge_lists(lst1, lst2):
    for i in lst2:
        # if i not in lst1:
            lst1.append(i)
    return lst1
print(merge_lists([1,2,3], [3,4,5,6]))