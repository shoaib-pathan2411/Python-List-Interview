def all_unique_elements(lst):
    return len(lst) == len(set(lst))

print(all_unique_elements([1,2,3,4]))
print(all_unique_elements([1,2,3,4,5,1]))