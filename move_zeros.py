# def move_zeros(lst):
#     result = []
#     zeros = 0
#     for num in lst:
#         if num == 0:
#             zeros += 1
#         else:
#             result.append(num)

#     return result + [0]*zeros

# print(move_zeros([1,2,3,4,0,3,0,5,0,3]))

def move_zeros(lst):
    result = []
    count = 0
    for num in lst:
        if num != 0:
            result.append(num)
        else:
            count += 1
    for i in range(count):
        result.append(0)
    return result
print(move_zeros([1,2,3,4,0,3,0,5,0,3]))