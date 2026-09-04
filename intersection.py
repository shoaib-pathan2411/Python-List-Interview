# The syntax def intersection(lst1, lst2): is a standard Python function definition used 
# to find the intersection of two lists—meaning it identifies the elements that are common 
# to both lst1 and lst2.
def intersection(lst1,lst2):
    result = []
    for num in lst1:
        if num in lst2 and num not in result:
            result.append(num)

    return result

print(intersection([1,2,3,4], [3,4,5,6]))