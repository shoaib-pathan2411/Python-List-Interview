def left_rotations(str1):
    for i in range(len(str1)):
        # print(str1[i])    
        roated = str1[i:] + str1[:i]
        print(roated)

s = 'abcd'
left_rotations(s)