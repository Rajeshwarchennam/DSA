#Problem Link -  https://bit.ly/3JPcoOx

def frogJump(n: int, heights: list[int]) -> int:

    # Write your code here.
    if n == 1:
        return 0
    dp = [0]*(n)
    dp[1] = abs(heights[1] - heights[0])
    for i in range(2, n):
        dp[i] = min(dp[i-1] + abs(heights[i]-heights[i-1]), dp[i-2] + abs(heights[i]-heights[i-2]))
    return dp[n-1]

if __name__ == "__main__":
    n = 6
    heights = [30, 10, 60, 10, 60, 50]
    print(frogJump(n, heights))