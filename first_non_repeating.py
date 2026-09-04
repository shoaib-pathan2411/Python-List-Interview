def first_non_repeating(lst):
    for num in lst:
        if lst.count(num) == 1:
            return num

print(first_non_repeating([1,3,1,2,4,2,4,6,3]))