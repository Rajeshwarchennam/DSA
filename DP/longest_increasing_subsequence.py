def longest_increasing_subsequence(nums: list[int]) -> int:
    n = len(nums)
    lis = [1]*n
    #lis[i] contains the value of subsequence ending at nums[i]
    for i in range(1,n):
        for j in range(i):
            if nums[i] > nums[j] and lis[i] < lis[j]+1:
                lis[i] = lis[j]+1
    return max(lis)

if __name__ == "__main__":
    nums = [10,9,2,5,3,7,101,18]
    print(longest_increasing_subsequence(nums))