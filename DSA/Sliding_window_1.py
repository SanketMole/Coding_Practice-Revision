## Maximum Average continuous SubArray I 

def Max_avg_subarray(arr, k):
    max = float('inf')
    for i in range(len(arr)):
        sum = 0
        for j in range(k):
            if not (i+(k-1) > len(arr)-1):
                sum += arr[i+j] 
            else:
                i = len(arr) 
                j = k 
        if sum != 0: 
            max = max(max, sum)

if __name__ == "__main__":
    arr = [1, 12, -5, -6, 50, 3]
    k = 4 
    print(Max_avg_subarray(arr, k))