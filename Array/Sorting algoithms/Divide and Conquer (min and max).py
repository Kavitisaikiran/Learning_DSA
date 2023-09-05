This is one of the most used approach for problem-solving and many other applications 
1.) Divide the problem into various  small problems 
2.) Conquer the problems by applying the recursion method
3.) Combine all the solutions into one 
We divide the problem in many ways that the solution made it possible  to find 

Implementation:

def findMin&Max(arr,i,j):
  i = 0
  j = len(arr)-1
  if i == j:
    min_value = arr[i]
    max_value = arr[i]
  if i == j-1:
    if arr[i] < arr[j]:
      min_value = arr[i]
      max_value = arr[j]
    else:
      min_value = arr[j]
      max_value = arr[i]
  else:
     mid = i+ (j-i)//2
     max1,min1 = findMin&Max(arr,i,mid)
     max2,min2 = findMin&Max(arr,mid+1,j)
  
  if max1 < max2:
    max_value = max2
  else:
    max_value = max1
  if min1< min2:
    min_value = min1
 else:
   min_value = min2

return (min_value, max_value)


In recursion we use stack space to call up the functions so the space complexity will be no of functions called i.e., log(n)
TIme complexity for this approach is O(n)
