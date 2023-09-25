#latihan Bubble Sort

list = [100, 20, 60, 90, 40, 30, 10]

def bubbleSort(arr):
    n = len(arr)
    
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    
    # Traverse through all array elements
    for i in range(n-1):
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            return

bubbleSort(list)
print("Sorted array is:")
for i in range(len(list)):
    print("% d" % list[i], end=" ")