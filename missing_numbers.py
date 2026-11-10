# def missing_numbers(lst, n):
#     result = []
#     for num in range(1, n+1):
#         if num not in result:
#             result.append(num)
#             # print(num)
#     return result

# print(missing_numbers([1,3,5,6,8],8))

# def missing_numbers1(lst):
#     result = []
#     for num in range(1, len(lst)+1):
#         if num not in result:
#             result.append(num)
#     return result
# print(missing_numbers1([1,3,5,6,8]))

import pdb
def missing_numbers2(lst):
    result = []
    smallest = lst[0]
    largest = lst[0]
    # pdb.set_trace()
    for num in lst:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
            
    # print(smallest)
    # print(largest)

    for i in range(smallest, largest+1):
        # if i not in result:
    #         result.append(i)
    # return result
        if i not in lst:
            print(i)
print(missing_numbers2([1,3,5,7,9]))