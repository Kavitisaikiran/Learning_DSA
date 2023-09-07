This is an Inplace sort algorithm
not a stable algorithm
When the array is highly unsorted we generally use QuickSort

_Approach:_
1.) Let the first element be the pivot element
2.) j pointer stores the element greater than the pivot and starts from the first index 
3.) i pointer stores the element smaller than the pivot 

if j is greater > than the pivot the loop continues 
else case i is called and i = i + 1 and the elements are swapped from i , i+1

**Note:** First the i pointer is updated and then swapping happens 
4.) Lastly the current arr[i] is swapped with pivot element 
We can see the elements left of the pivot are always smaller and right of the pivot are greater than pivot elements 

_Implementation_:

