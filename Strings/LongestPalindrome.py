# Time Complexity - O(n ^ 2)
# Space Complexity - O(1)

def longestPalSubstring(string):
    low = 0
    high = 0
    n = len(string)
    start = 0
    maxLength = 1
    for i in range(n):
        '''
        Count Even palindromic string around that index
        '''
        low = i
        high = i+1
        while low >= 0 and high < n and string[low] == string[high]:
            low -= 1
            high += 1
        #Getting low and high to their previous values as it the last
        #instance where both of them holds palindromic rules at that
        #point
        low += 1
        high -= 1
        if high-low+1 > maxLength:
            start = low
            maxLength = high - low + 1
        
        '''
        Count Odd Palindromic string around that index
        '''
        low = i-1
        high = i+1
        while low >=0 and high < n and string[low] == string[high]:
            low -= 1
            high += 1
        #Getting low and high to their previous values as it the last
        #instance where both of them holds palindromic rules at that
        #point
        low += 1
        high -= 1
        if high-low+1 > maxLength:
            start = low
            maxLength = high - low + 1
    
    return string[start:start+maxLength]

if __name__ == "__main__":
    string = "ejarrajeshwarxrawrajesh"
    print(longestPalSubstring(string))
