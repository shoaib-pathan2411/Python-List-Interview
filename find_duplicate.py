def find_duplicate(lst):
    seen = []
    dulicates = []
    for num in lst:
        if num in seen:
            if num not in dulicates:
                dulicates.append(num)
        seen.append(num)
    return dulicates
print(find_duplicate([1,2,4,5,3,4,2,4,53]))