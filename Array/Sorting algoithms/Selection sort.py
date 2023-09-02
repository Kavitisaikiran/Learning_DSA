it assaigns the first element index  as min and checks every element if the arr[i] < min then swaps  a the index after checks it swaps 
after every iteration we get the smallest elemnt as the first element 
we swap only once at a comparsion but at every comparision we check complete array and  after finfind the minimum number we swap it to min 
Time Complexity: O(n^2)

Implementation:
def selectionSort(arr):
  for i in range(n):
    min = i
    for j in range(i+1, n):
      if arr[j] < arr[min]:
        min = j
    arr[i], arr[min] = arr[min] , arr[i]
  return arr   

after comparing until we get minimum value it assaigns the index then after every comparision lastly the value i sswapped  
