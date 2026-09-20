def locate(arr,query):
  start=0
  end=len(arr)-1

  while start<=end:
    mid= (start+end)//2
    if(arr[mid]==query):
      return mid
    elif(arr[mid]>query):
      end= mid-1
    else:
      start=mid+1
  return -1 


arr=[13,11,8,7,4,3,0]
query=7
result= locate(arr,query)
 
print(result)
