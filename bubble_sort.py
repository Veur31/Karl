def bubble_sort(arr): #a function for bubble sort
    num = 1 #this will be useful for counting how many swapped happened, later
    n = len(arr) #this will count the lenght of the array
    for i in range(n): #creating a loop in the entire array
        for j in range(0, n-i-1): #this for loop is responsible for swapping the elements in the array, there is -1 in this loop
                                    #because there is no need to move the last element in the array
            if arr[j] > arr[j+1]: #this is a statement where if the first element or left side is greater than
                                    #the element in adjacent element or the right element then,
                arr[j], arr[j+1] = arr[j+1], arr[j] #they will swap
        print(f"Array in every swapped ({num}): {arr}") #this will show how many swapped happened during the iteration, also
                                                        #we will see how the elements are swapped every iteration
        num += 1 #this will just increment the num variable, so that we can see how many times the swapped happened
    print()
    return arr


arr = [6,8,1,3,2,10]
print()
print(f"Original array: {arr}\nSorted array, using Bubble Sort: {bubble_sort(arr)}")