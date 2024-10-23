def selectionSort(arr): #Selection Sort
    for i in range(len(arr)):
        minimo = i
        for j in range(i+1, len(arr)):
            if(arr[minimo] > arr[j]):
                minimo = j  
        aux = arr[i]
        arr[i] = arr[minimo]
        arr[minimo] = aux
    return arr