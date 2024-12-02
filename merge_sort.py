def merge_sort(arr): #function for merge sort
    if len(arr) >1: #this indented line of codes will run as long as it satisfy the condition
        mid = len(arr) // 2 #this is responsible for finding the middle element
        left_half = arr[:mid] #slicing the array into two the left side, and
        right_half = arr[mid:] #the right side
        print(f"\nLeft halve: {left_half}\nRight halve: {right_half}")
       
        merge_sort(left_half) #recursive calling the function,
        merge_sort(right_half) #until it satisfy the condition

        i = j = k = 0 #iniializing this 3 variables into zero, this will be useful especially in incrementing later on
                        #"moving into next index"

        while i < len(left_half) and j < len(right_half): #this while loop will run as long as it satisfy the condition
            print(f"Comparing the two halves: {left_half[i]} to {right_half[j]}")
            if left_half[i] < right_half[j]: #as we know that we initialize the variable i and j into zero 
                                                #this will compare the first element in the both halves
                arr[k] = left_half[i] #we know that we aslo intialize the variable k to 0 so if the left havle is less than the
                                        #right halve then the number in the left havle which is the first element in that halve will    
                                        #stored in the first index of arr[k] (original array)
                print(f"Left halve {left_half[i]} is stored in the arr[{k}] 'index'")
                i += 1 #now we increment i because we will know use the second element
            else: #this is else statement, this will run if we can't satisfy the if statement, meaning if the right halve is greater 
                    #than the left halve then,
                arr[k] = right_half[j] #we place it in index 0 of the original array
                print(f"Right halve {right_half[j]} is stored in the arr[{k}] 'index'")
            
                j += 1 #we increment j because now we will use the second element
            k+=1 #now we will increment k because we know that index 0 is already occupied
        while i <len(left_half): #this indented line of codes will check if the left halve still have elements left, if there is
            print(f"Placing remaining 'left' {left_half[i]} in array [{k}]")
            arr[k] = left_half[i] #it will be added to the array
            i += 1 #needs to be incremented because we need to move to the next index
            k += 1#needs to be incremented because we need to move to the next index
        while j <len(right_half): #this indented line of codes will check if the left halve still have elements left, if there is
            print(f"Placing remaining 'right' {right_half[j]} in array [{k}]")
            arr[k] = right_half[j] #it will be added to the array
            j += 1 #needs to be incremented because we need to move to the next index
            k += 1#needs to be incremented because we need to move to the next index
        print(F"Array: {arr}")
        print()
    return arr

arr = [20,17,15,3,5,9,30]
print(f"Original array: {arr}\nSorted array, using Merge Sort: {merge_sort(arr)}")