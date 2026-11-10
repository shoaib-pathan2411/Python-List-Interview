def find_max_addition_from_list(lst):
    # max_sum = 0
    a = lst[0]
    b = lst[1]
    max_sum = a + b
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            current_sum = lst[i] + lst[j]
            if current_sum > max_sum:
                max_sum = current_sum
    return max_sum
print(find_max_addition_from_list([-8, -9, -3, -5]))
print(find_max_addition_from_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# def find_max_addition_from_list(lst):
#     max_sum = float('-inf')  # Initialize max_sum to negative infinity to handle negative numbers
#     for i in range(len(lst)):
#         for j in range(i + 1, len(lst)):
#             current_sum = lst[i] + lst[j]
#             if current_sum > max_sum:
#                 # print(lst[i], lst[j])
#                 max_sum = current_sum
#     return max_sum
# print(find_max_addition_from_list([1, 2, 3, 4, 5, -6, 7, -8, -9]))
# print(find_max_addition_from_list([-8, -9, -3, -5]))