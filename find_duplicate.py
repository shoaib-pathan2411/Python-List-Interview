def find_duplicate(lst):
    seen = []
    duplicates = []
    for num in lst:
        if num in seen:
            if num not in duplicates:
                duplicates.append(num)
        seen.append(num)
    return duplicates

print(find_duplicate([1, 2, 4, 5, 3, 4, 2, 4, 53]))

def find_duplicate_element(list1):
    dup = []
    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
            if list1[i] == list1[j] and list1[i] not in dup:
                dup.append(list1[i])
    return dup
print(find_duplicate_element([1,2,4,5,3,4,2,4,53]))