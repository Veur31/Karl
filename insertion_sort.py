def insertion_sort(arr): #function for insertion sort
    counter = 1 #counter for tracing each step
    for i in range(1,len(arr)): #we start at the second element of the array which is 6
        
        key = arr[i] #now the key will be 6 because it is the first iteration of the for loop
        print()
        print(f"This is the key: {key}")
        j =i - 1 # we have a j variable for comparing it to the key (1-1 = 0) 0 will  be stored in the j varaible (8)
        while j >= 0 and key < arr[j]: #we will enter the while loop as long as we satisfy the statement 
            print(f"Array: {arr}")
            arr[j+1] = arr[j] # we see that 6 < 8, so will move j to the next index
            print(f"We move {arr[j]} from the index {j} to next index")
            j-= 1 #this line of code is responsible for exiting the while loop
        arr[j+1] = key #we know that j now is -1, this line of code is responsible for inserting the key element which is 
                        # 6 to the index 0 (-1+1 = 0)

        print(f"{key} at index {j+1}")
        print(f"Tracing each step ({counter}): {arr}") #this is responsible for keeping the trace
        counter += 1
    print()
    return arr

arr = [8,6,2,3,9,10]
print(f"Original array: {arr}\nSorted array, using Insertion Sort: {insertion_sort(arr)}")
