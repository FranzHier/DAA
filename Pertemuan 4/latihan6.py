# Latihan Binary Search
# Binary search memerlukan data agar sudah diurut terlebih dahulu

def selectSort_ascending(arr):
    for i in range(0, len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
def binarySearch(list, item):
    first = 0
    last = len(list) - 1
    
    while first <= last:
        midpoint = (first + last) // 2 #Divide and forcibly convert to integer
        if list[midpoint] == item:
            return True
        else:
            if item < list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return False

list = [89, 12, 57, 16, 25]
selectSort_ascending(list)
print(binarySearch(list, 12))
