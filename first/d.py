def check_first_sentence_is_second(first, second):
    words_first = first.split()
    dict_first = {}
    for word in words_first:
        dict_first[word] = dict_first.get(word, 0) + 1

    words_second = second.split()
    dict_second = {}
    for word in words_second:
        dict_second[word] = dict_second.get(word, 0) + 1

    for word in dict_second:
        if word not in words_first or dict_second[word] > dict_first[word]:
            return False
    return True
