This is an Inplace sort algorithm
not a stable algorithm
When the array is highly unsorted we generally use QuickSort
The time complexity of the partition algorithm is O(n)
space complexity :
  1.) worst case = O(n^2)
  2.) best case = O(nlogn)
The time complexity of the quicksort algorithm is O(nlogn)


Approach:
1.) Let the first element be the pivot element
2.) j pointer stores the element greater than the pivot and starts from the first index 
3.) i pointer stores the element smaller than the pivot 

if j is greater > than the pivot the loop continues 
else case i is called and i = i + 1 and the elements are swapped from i , i+1

Note: First the i pointer is updated and then swapping happens 
4.) Lastly the current arr[i] is swapped with pivot element 
We can see the elements left of the pivot are always smaller and right of the pivot are greater than pivot elements 

Implementation:

arr = []
p = 0
q = len(arr)-1
def quickSort(arr,p,q):
  if p<q:
    mid = partition(arr,p,q) # here we divide by calling this function 
  quickSort(arr,p,mid-1) # A recursive call is made and we get the pivot element 
  quickSort(arr,mid+1,q)
  return arr

# Here we define another function that helps us to find the pivot element 

def partition(arr,p,q):
  pivot = arr[p]
  i = p
  for j in range(i+1,q+1):
    if arr[j] <= pivot:
      i = i+1
      arr[i],arr[i+1] = arr[i+1],arr[i]
# Swap between pivot elements and current i element 
  arr[p],arr[i] = arr[i],arr[p]
  return i
# By this we get the pivot position which is used as mid in the main sort function 


Randomized QuickSort:
In general Case, we take the first element as the pivot element but here we take any random element as the pivot remaining procedure remains same 

implementation:
def randomizedquickSort(arr,p,q):
  randompivotindex = random.rand(p,q)

Time complexity remains the same 
 Space complexity is O(1) 



