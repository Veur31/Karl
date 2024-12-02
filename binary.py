def binary(arr, target):
    low = 0
    high = len(arr)-1
    while low <= high:
        middle = (low+high)//2
 

        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            low = middle + 1
        else:
            high = middle - 1

    return  -1
arr = [1,2,3,4]
target = 4
print(binary(arr, target)) 