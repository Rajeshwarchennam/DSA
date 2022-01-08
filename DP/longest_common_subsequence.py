def longest_common_subsequence(text1: str, text2: str) -> int:
    m = len(text1)
    n = len(text2)
    lcs = [[0]*(n+1) for i in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if text1[i-1] == text2[j-1]:
                lcs[i][j] = 1 + lcs[i-1][j-1]
            else:
                lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])
    return lcs[m][n]

if __name__ == "__main__":
    text1 = "abcde"
    text2 = "ace"
    print(longest_common_subsequence(text1, text2))