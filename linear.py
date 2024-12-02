def linear(target, arr):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
arr = [1,2,3,4]
target = 3
print(linear(target, arr)) 