def find_even(lst):
    result = []
    for num in lst:
        if num % 2 == 0:
        # if num % 2 != 0:
            result.append(num)

    return result

print(find_even([1,2,3,4,5,6,7,8]))