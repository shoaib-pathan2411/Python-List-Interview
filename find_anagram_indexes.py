def find_anagram_indexes(words):
    groups = {}
    for i in range(len(words)):
        word = words[i]
        sorted_words = ''.join(sorted(word))
        print(sorted_words)
        if sorted_words in groups:
            groups[sorted_words].append(i)
        else:
            groups[sorted_words] = [i]

    return groups

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(find_anagram_indexes(words))