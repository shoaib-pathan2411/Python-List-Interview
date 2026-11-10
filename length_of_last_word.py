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

def find_length_of_last_word(str1):
    words = str1.split()
    if not words:
        return 0
    last_word = words[-1]
    count = 0
    for char in last_word:
        count += 1
    return count
print(find_length_of_last_word("python django mysql"))