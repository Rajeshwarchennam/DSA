def LCSubStr(X, Y, m, n):
    LCSuff = [[0]*(n+1) for i in range(m+1)]
    result = 0
    '''
    LCSuff contains longest common suffix for two substrings.
    LCSuff[i][j] = longest suffix of substrings X[0......i-1]
    and Y[0.......j-1]
    '''
    for i in range(1,m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                LCSuff[i][j] = 1 + LCSuff[i-1][j-1]
                result = max(result, LCSuff[i][j])
            else:
                LCSuff[i][j] = 0
    return result

if __name__ == "__main__":
    X = "abcdXy"
    Y = "XYabcde"
    print(LCSubStr(X, Y, len(X), len(Y)))
