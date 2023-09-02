# Here every consequence number is compared and swapped by an order 
# Time complexity: O(n^2)
# In the best case when the array is already sorted constant time complexity 
# We can say for every n elements in an array we have (n-1) iterations 

Implementation:
def bubleSort(arr):
  for i in range(len(arr)):
    for j in range(0,n-1-i):
      if arr[j] > arr[j+1]:
        arr[j],arr[j+1] = arr[j+1],arr[j]
  return arr




      

