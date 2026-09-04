def first_duplicate_index(lst):
    seen = []
    for i in range(len(lst)):
        if lst[i] in seen:
            return seen.index(lst[i])
        else:
            seen.append(lst[i])

print(first_duplicate_index([1,5,3,4,7,6,7,8]))