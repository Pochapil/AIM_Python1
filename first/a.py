def find_word_in_circle(circle, word):
    for i in range(len(circle)):
        if circle[i] == word[0]:
            for j in range(1, len(word)):
                if circle[(i + j) % len(circle)] != word[j]:
                    break
            else:
                return i, 1

            for j in range(1, len(word)):
                if circle[(i - j) % len(circle)] != word[j]:
                    break
            else:
                return i, -1
    return -1
