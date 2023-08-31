# to apply Binary Search on 2-D arrays
# Rules:- 1. Integers in each row are sorted from left to right 
#         2. First integer of each row  > last integer of the previous row 

arr = [[1,2,3],[4,5,6],[7,8,9]]
Code:
def search2Darray(array, target):
  # to find the number of rows and columns
  m = len(arr)
  n = len(arr[0])
# iand j represent the initial and last value of the array
  i,j = 0, (m*n) -1
  while i< j:
    # First find the middle of the array
    mid_index = i + (j-i)/2
    mid_value = arr[mid_index//n][mid_index%n]
  if target == mid_value:
    return True
  elif target < mid_value:
    j = mid_index - 1
# Increasing our search area towards the left side of our mid-value 
  else:
    i = mid_index + 1
# Increasing our search area towards  the right side of mid-value 
  return False 
  
