n=int(input("Enter the number: "))
list1=[]
list2=[]
for i in range(1,n+1):
    list1.append(int(input("Enter a number: ")))

list1.sort()

if n%2!=0:
    median=list1[n//2]
else:
    median=(list1[n//2]+list1[(n+1)//2])/2

print("the median is:", median)