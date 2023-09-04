1.) Delete the element and store it in some temp space or any other array
continue tis process n times 
the returned array is sorted array

Time Complexity: O(n*logn)

Building of Min Heap:
1. write the given array in its tree form 
2. check the leaf nodes with their parent nodes and swap with them 
3. repeat the process till root node
the tree we get will be the min Heap

Time comlpexity for this will be O(n)

Pseudocode: 
def builheap(arr,n):
  startindex = n//2 -1
  for i in range(startindex, -1,-1):  ///here we go backwards 
    heapify(arr,n,i)
def heapify(arr,n,i):
  smallest = i  # parent node or first element  root element 
  l = 2*i +1 ///to acess left  elements of tree
  r = 2*i -1 /// to access right elemtns of tree 
  if arr[l] < arr[smallest]:
    smallest = l
elif arr[r] < arr[smallest]:
    smallest = r
    heapify(arr,n,smallest) # recursion to heapify the new root and continue the process 
