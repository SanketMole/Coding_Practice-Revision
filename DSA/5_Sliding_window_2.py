# Fruit into Basket

# You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

# You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.

# Eg: Input: fruits = [0,1,2,2]
# Output: 3
# Explanation: We can pick from trees [1,2,2].
# If we had started at the first tree, we would only pick from trees [0,1].

def fruit_into_basket(arr):
    treeTypesMap = []
    maxi = 0 
    start = 0 
    for end in range(len(arr)):
        if len(treeTypesMap) < 2 and arr[end] not in treeTypesMap:
            treeTypesMap.append(arr[end])
            maxi = max(maxi, end-start+1) 
        elif arr[end] in treeTypesMap:
            maxi = max(maxi, end-start+1)
        else:
            treeTypesMap = []
            treeTypesMap.append(arr[end-1])
            treeTypesMap.append(arr[end])
            start = end - 1 
            while(arr[start] == arr[start-1]):
                start -= 1
            maxi = max(maxi, end-start+1)
    return int(maxi)     

if __name__ == "__main__":
    trees = [1,2,3,2,2]
    print(fruit_into_basket(trees))
