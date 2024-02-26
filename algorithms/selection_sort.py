def selection_sort(arr):
    for i in range(len(arr)): # iterate through the array
        min_index = i # assume the first element is the smallest
        for j in range(i+1, len(arr)): # iterate through the rest of the array
            if arr[min_index] > arr[j]: # if the current element is smaller than the smallest element
                min_index = j # update the index of the smallest element
        arr[i], arr[min_index] = arr[min_index], arr[i] # swap the smallest element with the first element
    return arr


array = [5,3,6,2,10]
print(selection_sort(array))