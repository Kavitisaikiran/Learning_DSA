Here we create a temp space for the first value and then checks it with every value and increase the second loop 
Time complexity = O(n^2)

Implementation:
def insertionSort(arr):
  for i in range(n):
    temp = arr[i]
    for j in range(1,n):
      j = i-1
      while (j>=0 and arr[j] > temp):
        arr[j+1] = arr[j]
        j = j-1
      arr[j+1] = temp
  return arr
