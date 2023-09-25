# Latihan Insertion Sort

def insertionSort(arr):
    n = len(arr)
      
    if n <= 1:
        return
 
    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j+1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j+1] = key  # Insert the key in the correct position
        
def insertion(arr):
    if len(arr) <= 1:
        return
    
    for i in range(1, len(arr)):
        j = i
        while arr[j-1] > arr[j] and j > 0:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1

list = [89, 12, 57, 16, 25, 11, 75]
print(list)
insertionSort(list)
print("Sort dengan metode 1: ", list)
list = [89, 12, 57, 16, 25, 11, 75]
insertion(list)
print("Sort dengan metode 2: ", list)
