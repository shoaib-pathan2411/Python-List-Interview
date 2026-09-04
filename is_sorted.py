def is_sorted(lst):
    for num in range(len(lst)-1):
        # print(num)
        # print(lst[num])
        if lst[num] > lst[num+1]:
            return False
        
        # else:
        #     return True
        
    return True

print(is_sorted([1,2,6,2,4,5,3]))
print(is_sorted([1,2,3,4,5,6,7,8,9]))