# Remove All Occurrences of Element
def remove_element(lst, x):
    result = []
    for num in lst:
        if num != x:
            result.append(num)

    return result

print(remove_element([1,2,3,4,3,5,6,3], 3))

def remove_element(lst, x):
    for num in lst:
        if num == x:
            lst.remove(num)

    return lst

print(remove_element([1,2,3,4,3,5,6,3], 3))