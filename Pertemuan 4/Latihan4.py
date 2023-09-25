# latihan Selection Sort

def selectSort_ascending(arr):
    for i in range(0, len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
def selectSort_descending(arr):
    for i in range(len(arr)-1, 0, -1):
        max_index = i
        for j in range(0, i, 1):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]    
     
list = [89, 12, 57, 16, 25]
print(list)
selectSort_ascending(list)
print(list)
list = [89, 12, 57, 16, 25]
selectSort_descending(list)
print(list)