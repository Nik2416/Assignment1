n=int(input("Enter the number: "))
list1=[]
list2=[]
for i in range(1,n+1):
    list1.append(int(input("Enter a number: ")))

for i in range(n):
    if i%2==0:
        continue
    else:
        list2.append(list1[i])


print("the numbers on odd positions are:", list2)