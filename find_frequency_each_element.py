def find_frequency_each_element(lst):
    freq = {}
    for ele in lst:
        if ele in freq:
            freq[ele] += 1
        else:
            freq[ele] = 1

    return freq
    # for i in freq:
    #     print(f"{i} : {freq[i]}")
print(find_frequency_each_element([1,2,3,4,56,2,4,5,6,2,4,67,4]))
