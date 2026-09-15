def pair_sum(lst, target):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == target:
                # return lst[i], lst[j]
                return i, j

print(pair_sum([1,2,3,4,5,6,7,9], 9))