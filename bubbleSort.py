def bubbleSort(arr):
    for i in range(len(arr)): #Bubble sort
        for j in range(len(arr)-i-1):
            if(arr[j] > arr[j+1]):
                aux = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = aux
    return arr