def CountInversion(arr):
    icount = 0
    if len(arr) <= 1:
        return icount

    mid = len(arr)//2       # Finding the mid of the array
    Left = arr[:mid]        # Dividing the array elements
    Right = arr[mid:]       # Into 2 halves

    icount += CountInversion(Left)
    icount += CountInversion(Right)
    i = j = k = 0

    while i < len(Left) and j < len(Right):
        if Left[i] < Right[j]:
            arr[k] = Left[i]
            i += 1
        else:
            arr[k] = Right[j]
            j += 1
            icount += mid - i
        k += 1
        
    while i < len(Left):
        arr[k] = Left[i]
        i += 1
        k += 1
    while j < len(Right):
        arr[k] = Right[j]
        j += 1
        k += 1
    
    return icount

arr = [1, 20, 6, 4, 5]
print(CountInversion(arr))