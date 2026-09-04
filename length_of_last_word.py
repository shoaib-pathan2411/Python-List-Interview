def length_of_last_word(str1):
    str1 = str1.split()
    # print(str1)
    # print(len(str1))
    size = len(str1)
    if size == 1:
        return len(str1)
    last_word = str1[-1]
    print(len(last_word))



length_of_last_word("python django mysql")