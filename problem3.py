n=int(input("Enter the number: "))
list1=[]
list2=[]
for i in range(1,n+1):
    list1.append(int(input("Enter a number: ")))


for i in range(n):
    if list1[i]>=500:
        break
    if list1[i]==150:
        continue
    if list1[i]%5==0:
        list2.append(list1[i])

print("the numbers are", list2)