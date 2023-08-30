# This is applicable only when the array is sorted  in increasing or non-increasing order 
# Here we find the mid element first and start comparing the mind element with the target value and search for right or left from the mid element 
# Once we choose the side to search we use a Recursive call to search for the element 
Time Complexity = O(logn)

# define function

def binarySearch(arr,target,i, j):
  while i <= j:
    mid = i + (j-i)/2
    if arr[mid] = target:
      return mid
    elif arr[mid] > target:
# Here we can conclude we need to search the array on the left side
# By changing the upper limit on array search we call a recursive function with different parameters to limit the search area 
      return binarySearch(arr, target, i, mid-1)
    else:
      return binarySearch(arr, target, mid+1, j)
# Here we changed the lower bound of the search area to search the right side of the array by calling recursive functions

# function calling
binarySearch(arr,target,i,j)
