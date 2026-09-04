def find_squares(lst):
    result = []
    for num in lst:
        num = num*num
        result.append(num)

    return result
        # return num

print(find_squares([1,2,3,4,5,6,7,8]))