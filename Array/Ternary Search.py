# Here we divide the given sorted array into 3 parts and continue our search 
# We do 3 iterations for checking the target value i.e., comparing left, mid and right regions 
# Time complexity: O(logn) to base 3

arr = [1,2,3,4,5,6,7,8,9,10]
#  First we need to find two mid-values  of the array
def ternarySeach(arr,target,i,j):
  i = 0
  j = len(arr) -1
  mid1 = i + (j-i)//3 
  mid2 = j - (j-i)//3
  while i <= j:
    if mid1 == target:
      return mid1
    if mid2 == target:
      return mid2
    elif target > mid2:
      return ternarySearch(arr,target,mid2+ 1,j)
    elif target < mid1:
      return ternarySearch(arr, target, i, mid1-1)
    else:
      return ternarySearch(arr, target, mid1+1, mid2-1)
  return []
# by keeping elif rules we searched the right and left most part of array and in the else loop we searched the mid-region of the array
