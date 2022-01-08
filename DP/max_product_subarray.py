def max_product_subarray(nums: list[int]) -> int:
    result = max(nums)
    currMax, currMin = 1,1
    for i in nums:
        if i == 0:
            currMax, currMin = 1,1
        else:
            currMax, currMin = max(currMax*i, currMin*i, i), min(currMax*i, currMin*i, i)
            result = max(currMax, result)
    return result

if __name__ == "__main__":
    print(max_product_subarray([-2,0,-1]))
    print(max_product_subarray([2,3,-2,4]))