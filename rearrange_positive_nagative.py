def rearrange_positive_nagative(lst):
    pos = []
    neg = []
    for num in lst:
        if num >= 0:
            pos.append(num)
    # for num in lst:
    #     if num < 0:
    #         neg.append(num)
        else:
            neg.append(num)

    return pos + neg

print(rearrange_positive_nagative([3, -1, 4, -2, 0, -5]))

def rearrange_positive_nagative(lst):
    result = []
    result1 = []
    for num in lst:
        if num >= 0:
            result.append(num)
        else:
            result1.append(num)
    for num in result1:
        result.append(num)
    return result

print(rearrange_positive_nagative([3, -1, 4, -2, 0, -5]))