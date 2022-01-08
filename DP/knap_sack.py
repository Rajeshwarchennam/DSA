#https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/

def knapSack(W: int, wt: list[int], val: list[int]):
    n = len(wt)
    dp = [[0]*(W+1) for i in range(n+1)]
    for i in range(1,n+1):
        for w in range(1, W+1):
            if wt[i-1] > w:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(val[i-1]+dp[i-1][w-wt[i-1]], dp[i-1][w])
    return dp[n][W]

if __name__ == "__main__":
    val = [60, 100, 120]
    wt = [10, 20, 30]
    W = 50
    print(knapSack(W, wt, val))