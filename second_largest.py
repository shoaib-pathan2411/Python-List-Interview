def second_largest(lst):
    first = float('-inf')
    second = float('-inf')
    for num in lst:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second

print(second_largest([1,2,4,52,5,66,4,3,4,3,4,45,56,24]))