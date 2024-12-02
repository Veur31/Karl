def selection_sort(arr): #Function for selection Sort
    counter = 1 #this is a counter for counting how many swapped had happened
    n = len(arr) #this will just get the length of the array
    for i in range(n): #for loop for iterating throught the entire arr(len)
        min_index = i #the minumun index for now is the first element
        for j in range(i+1,n): #this loop is reponsible for swapping elements, also we put i + 1 here because we will start in the 
                                #second element in the array
            if arr[j] < arr[min_index]: #Now we will check every element in the array if its less than the first element
                min_index = j #if its less thant he first element then we will update our minimun_index to that element
        arr[i], arr[min_index] = arr[min_index], arr[i] #this is where swapping is happening
        print(f"Array in every swapped ({counter}): {arr}") #this will show how many swapped had happened
        counter += 1 #this is a counter
    print()
    return arr 
arr = [10,3,5,7,1,8]
print(f"Original array: {arr}\nSorted, using Selection Sort: {selection_sort(arr)}")
