def all_unique_elements(lst):
    return len(lst) == len(set(lst))

print(all_unique_elements([1,2,3,4]))
print(all_unique_elements([1,2,3,4,5,1]))

def all_uniqe_elements_from_list(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return False
        seen.add(item)
    return True

print(all_uniqe_elements_from_list([1,2,3,4]))
print(all_uniqe_elements_from_list([1,2,3,4,5,1]))