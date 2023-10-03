def dac_max(arr, start, end):
  max = -1

  if (start >= end - 2):
    if (arr[start] > arr[start + 1]):
      return arr[start]
    else:
      return arr[start + 1]
  
  max = dac_max(arr, start +1, end)

  if (arr[start] > max):
    return arr[start]
  else:
    return max

def dac_min(arr, start, end):
  min = 0
  if (start >= end - 2):
    if (arr[start] < arr[start + 1]):
      return arr[start]
    else:
      return arr[start + 1]
  
  min = dac_min(arr, start+1, end)

  if (arr[start] < min):
    return arr[start]
  else:
    return min

# array initiaization
arr = [4, 12, 23, 9, 21, 1, 35, 2, 24]

max = dac_max(arr, 0, 9)
min = dac_min(arr, 0, 9)

print(arr)
print(max)
print(min)