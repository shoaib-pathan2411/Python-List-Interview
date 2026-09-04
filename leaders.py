# Find All Elements Greater Than Right Side
def leaders(lst):
    result = []
    max_right = lst[-1]
    result.append(max_right)
    # print(max_right)
    # print(result)
    for num in range(len(lst)-2,-1,-1):
        # print(num)
        if lst[num] > max_right:
            result.append(lst[num])
            max_right = lst[num]
    return result[::-1]
print(leaders([16, 17, 4, 3, 5, 2]))

##this is the greater element or num in list for right side
def alpha(lst):
    result1 = []
    for i in range(len(lst)):
        greater_element = []
        for j in range(i+1, len(lst)):
            if lst[j] > lst[i]:
                greater_element.append(lst[j])
        return greater_element
        # result1.append(greater_element)
    # return result1
print(alpha([16, 17, 4, 3, 5, 2]))