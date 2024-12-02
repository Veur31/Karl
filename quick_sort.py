def quick_sort(arr): #Creating a function for quicksort
    if len(arr) <= 1: 
        return arr #if the array is 1 or less than one then it will return the array
    pivot = arr[0] #The last element of the array will be stored in the pivot variable
    left  = [x for x in arr if x  < pivot] #all the elements that is less than the pivot will store in the left variable
                                            #where it will loop using the for loop(and list comrehension)
    middle =  [x for x in arr if x == pivot] # now this will be usefull especially in recusion
    right =  [x for x in arr if x  > pivot]#all the elements that is greater than the pivot will store in the right variable
                                            #where it will loop using the for loop(and list comrehension)
    return quick_sort(left) + middle + quick_sort(right) #this will recursively call(left and right) the function until it is all sorted
arr = [10,7,8,9,1,5]
print(f"Original array: {arr}\nSorted, using Quick Sort: {quick_sort(arr)}")
