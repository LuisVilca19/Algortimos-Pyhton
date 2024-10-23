def countSort(arr, max):
    output = [0 for i in range(len(arr))]
    count = [0 for i in range(max)]

    for i in arr:
        count[i] +=1

    for i in range(1, max):
        count[i] += count[i-1]
    
    for i in range(len(arr)):
        output[count[arr[i]]-1] = arr[i]
        count[arr[i]] -= 1

    return output

arr = [5, 2, 7, 4, 3, 1, 8, 9, 13, 12]
max = max(arr) #Determinamos el numero mayor
arreglo = countSort(arr, max+1)
print(arreglo)