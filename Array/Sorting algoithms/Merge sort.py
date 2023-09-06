Merge Sort:
it is an application of the divide-and-conquer method 
Time complexity of O(nlogn) for both best and worst cases 
Space complexity will be O(m+n) === O(N)
This is a stable algorithm 

divide the array based on mid and conquer each by using recursion i.e., calling the same function using mid parameters at the upper and lower bound 
Combing the outputs is a process called a Merge Procedure:: it gives a sorted array towards moving up to the root node 

Merge Procedure:: 
at the final root node, the left side and right part sub-arrays are fully sorted to sort the array completely :
  1.) We take a new array of the same size, the left subarray is initialized with some pointer (i), and the right subarray with the pointer (j)
  2.) compare i <j and now update i to i+1 
  3.) Compare (i+1) and j  if j is less than i+1 the update j pointer 
  4.) Now again compare i+1 and j+1 .. goes on 
5.) We update the pointer of the value that is less than the other and keep the remaining pointer unchanged  and the k pointer is always updated 
time complexity for mergeprocedure is O(m+n)

Implementation::

#  First we need to define the merge procedure :

def mergeProcedure(arr,i,mid,j):
  i = 0
  j= len(arr) -1
  mid = i+(j-i)//2
  n1 = mid-i+1  #number of elements in left sub-array
  n2 = j-mid  #number of elements in the right subarray
  leftarr = [0]*n1
  rightarr = [0]*n2
# copying the elements from main array to the left and right sub array 
  for m in range(n1):
    leftarr[m] = arr[ i+m]
  for n in range(n2):
    rightarr[n] = arr[mid+1+n]
  
  p = q = k =0
  while p<n1 and q<n2:
    if leftarr[p] <= rightarr[q]:
      arr[k] = leftarr[p]
      p = p+1
    else:
      arr[k] = rightarr[q]
      q = q+1
    k = k+1  #outside the if condition
    # fown below if any one of subarray lengths is greater than the other then copy the remaining elements from the subarray after the comparison
  while p<n1:
    arr[k] = leftarr[p]
    k = k+1
  while  q<n2:
    arr[k] = rightarr[q] 
    k = k+1


def mergeSort(arr,i,j):
  if i ==j:
    return arr[i]
  if i<j:
    mid = i+(j-1)//2
    mergeSort(arr,i,mid)
    mergeSort(arr,mid+1,j)
    mergeProcedure(arr,mid,i,j) # used to combine the answers coming from above recursions
  return arr


No of elements in an array will be  = upper bound - lower bound + 1

  


