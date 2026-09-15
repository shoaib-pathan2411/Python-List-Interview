def find_pairs(list1, target):
    for i in range(len(list1)):
        # print('this is firt loop --->', i)
        for j in range(i + 1, len(list1)):
            # print('this is second loop --->', j)
            if list1[i] + list1[j] == target:
                print(list1[i], list1[j])
                print('this is the index position of the first number and --->', i)
                print('this is the index position of the second number and --->', j)

find_pairs([1,2,3,4,5,6,], 11)
find_pairs([1,2,3,4,5,6,], 10)