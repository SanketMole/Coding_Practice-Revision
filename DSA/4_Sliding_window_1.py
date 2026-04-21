## Maximum Average continuous SubArray I 

# Naive Solution (Brute Force Method)
# TC: O(nk)

def Max_avg_subarray(arr, k):
    maxi = float('-inf')
    for i in range(len(arr)):
        sum = 0
        for j in range(k):
            if not (i+(k-1) > len(arr)-1):      # Last index of current range should not exceed arr's last index
                sum += arr[i+j] 
            else:
                i = len(arr)    # To break outside loop
                break 
        if sum != 0: 
            maxi = max(maxi, sum/k)
    if maxi == float('-inf'):
        return 0
    return maxi

# Sliding Window 
# TC: O(n)

def Max_avg_sliding(arr, k):
    windowSum = 0
    start = 0
    maxi = float('-inf')
    for end in range(len(arr)):
        windowSum += arr[end]
        if(end - start + 1) == k:
            maxi = max(maxi, windowSum/k)
            windowSum -= arr[start]
            start += 1 
    return maxi 

if __name__ == "__main__":
    arr = [1, 12, -5, -6, 50, 3]
    k = 4 
    # print(Max_avg_subarray(arr, k))
    print(Max_avg_sliding(arr, k))