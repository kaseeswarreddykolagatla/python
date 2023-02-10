def edidistance(word1, word2, m, n):
    if m == 0:
        return n
    if n == 0:
        return m
    if word1[m-1] == word2[n-1]:
        return editdistance(word1, word2, m-1, n-1)
    return 1 + min(editdistance(word1, word2, m, n-1),
                   editdistance(word1,word2, m-1 n),
                   editdistanc(word1, word2, m-1, n-1))
word1 =input("Enter a word: ")
word2 =input("Enter a word: ")
print(editdistance(word1, word2, len(word1),len(word2)))
