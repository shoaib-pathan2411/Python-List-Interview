def count_occurrences(lst, num):
    count = 0
    for item in lst:
        if item == num:
            count = count + 1

    return count
print(count_occurrences([1,2,3,4,2,3,3,4,2,45,2,3], 3))
print(count_occurrences([1,2,3,4,5,2,6,2,3,4,5,6], 2))