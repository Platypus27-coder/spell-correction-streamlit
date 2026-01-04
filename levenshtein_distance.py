import streamlit as st

def minDistance(word1: str, word2: str) -> int:
    m = len(word1)
    n = len(word2)
    # dp[i][j] := min # Of operations to convert word1[0..i) to word2[0..j)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
      dp[i][0] = i

    for j in range(1, n + 1):
      dp[0][j] = j

    for i in range(1, m + 1):
      for j in range(1, n + 1):
        if word1[i - 1] == word2[j - 1]:
          dp[i][j] = dp[i - 1][j - 1]
        else:
          dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

    return dp[m][n]

st.title("Word Correction")
word = st.text_input("Your word: ")

file = open("vocab.txt", "r", encoding = "utf-8")
vocabs = []
for data in file:
    vocabs.append(data.strip().lower())
vocabs = list(set(vocabs))
vocabs.sort()
if st.button("Compute"):
    distances = dict({})
    for vocab in vocabs:
        distance = minDistance(word, vocab)
        distances[vocab] = distance
    sorted_distances = sorted(distances.items(), key=lambda x: x[1])
    if len(sorted_distances) > 0:
        correct_word = sorted_distances[0][0]
        st.write("Correct word: ", correct_word)
    else:
        st.write("No suggestion found")

