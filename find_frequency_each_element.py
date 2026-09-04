def find_freauency_each_element(lst):
    freq = {}
    for ele in lst:
        if ele in freq:
            freq[ele] += 1
        else:
            freq[ele] = 1

    return freq
print(find_freauency_each_element([1,2,3,4,56,2,4,5,6,2,4,67,4]))
