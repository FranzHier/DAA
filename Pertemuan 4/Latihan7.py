# Latihan Interpolation Search

def selectSort_ascending(arr):
    for i in range(0, len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def interpSearch(list, value):
    high = len(list) - 1
    low = 0
    while value >= list[low] and value <= list[high] and low <= high:
        probe = low + (((high -low) * (value - list[low])) // (list[high] - list[low]))
        
        if list[probe] == value:
            return True
        elif list[probe] < value:
            low = probe + 1
        elif list[probe] > value:
            high = probe - 1    
    return False
            
list = [89, 12, 57, 16, 25]
selectSort_ascending(list)
print(interpSearch(list, 57))
            