#Practice - https://www.geeksforgeeks.org/nearly-sorted-algorithm/


from heapq import heappop, heappush, heapify

def sortK(arr, n, k):
    heap = arr[:k+1]
    heapify(heap)
    targetIndex = 0
    for remainingElements in range(k+1, n):
        arr[targetIndex] = heappop(heap)
        heappush(heap, arr[remainingElements])
        targetIndex += 1
    
    while heap:
        arr[targetIndex] = heappop(heap)
        targetIndex += 1

if __name__ == "__main__":
    k = 3
    arr = [2, 1, 3]
    n = len(arr)
    sortK(arr, n, k)
    print(arr)